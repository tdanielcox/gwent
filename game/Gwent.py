import copy
from game.lib.cards import nr_cards
from game.lib.logger import Logger
from game.lib.cli import CLI
from game.lib import util


# Gwent game class
class Gwent:
    def __init__(self, options={}):
        self.game = {}
        self.has_player = True
        self.computer_turn = None
        self.computer_trade_round = None
        self.__enable_logging = True
        self.__last_prompt = None

        if 'enable_logging' in options and options['enable_logging'] is not False:
            enable_logging = options['enable_logging']
        else:
            enable_logging = False

        self.logger = Logger(enable_logging)
        self.cli = CLI(self, self.logger)

    # Create a new game
    def new(self):
        first_player = util.rand0_1()

        self.game = {
            'id': util.generate_uuid(),
            'round': 0,
            'winner': None,
            'current_player': first_player,
            'rounds': [
                self.__setup_round(),
                self.__setup_round(),
                self.__setup_round(),
            ],
            'players': [
                self.__setup_player(nr_cards),
                self.__setup_player(nr_cards),
            ],
            'status': ['round_0_start', 'player_%i_start' % first_player],
            'prompt': None
        }

        return self.game

    # Load an existing game
    def load(self, blob):
        self.game = blob

        if not self.__game_playable():
            self.logger.print_unplayable_game(self)
            return None

        return self.game

    # Start the game
    def start(self, player_count, computer_round_actions=None, computer_trade_actions=None):
        if player_count == 0:
            self.has_player = False
            self.computer_turn = computer_round_actions
            self.computer_trade_round = computer_trade_actions
        else:
            self.computer_turn = computer_round_actions
            self.computer_trade_round = computer_trade_actions

        self.factor_board()

        return self.game

    def start_cli(self, player_count, computer_round_actions=None, computer_trade_actions=None):
        self.start(player_count, computer_round_actions, computer_trade_actions)

        for current_round in range(3):
            self.cli.start_round(current_round)
            self.__set_graveyards(current_round)

            if current_round == 2:
                self.finish_game()

    def ai_turn(self):
        if not self.__game_playable():
            return None

        current_round = self.game['round']
        self.computer_turn(self, current_round, self.game['players'][util.COMPUTER]['cards'])

        return self.game

    def play_card(self, card_id):
        if not self.__game_playable():
            self.logger.print_unplayable_game(self)
            return None

        current_round = self.game['round']
        player_index = self.game['current_player']
        player = self.game['players'][player_index]

        _card = self.__get_card(player['cards'], card_id)
        self.__reset_prompt()

        if _card is not None:
            card = _card[0]
            row = _card[1]
            index = _card[2]
            can_run_medic = False

            del player['cards'][row][index]

            if card[util.ROW] == 3:
                if card[util.ABILITY] == util.WEATHER:
                    self.__run_clear_weather()
                if card[util.ABILITY] == util.SCORCH:
                    self.__run_scorch()
            else:
                if card[util.ABILITY] == util.SPY:
                    self.__run_spy(player_index)
                    opponent_index = not player_index
                    self.game['rounds'][current_round]['cards'][opponent_index][row].append(card)
                elif card[util.ABILITY] == util.WEATHER:
                    opponent_index = not player_index
                    self.game['rounds'][current_round]['cards'][player_index][row].append(card)
                    self.game['rounds'][current_round]['cards'][opponent_index][row].append(card)
                elif card[util.ABILITY] == util.MEDIC:
                    self.game['rounds'][current_round]['cards'][player_index][row].append(card)
                    can_run_medic = self.__run_medic()
                else:
                    self.game['rounds'][current_round]['cards'][player_index][row].append(card)

            self.logger.print_card_played(self, player_index, card)

            self.__set_status('player_%i_play_card' % self.game['current_player'], True)
            self.factor_board()

            if card[util.ABILITY] == util.MEDIC:
                if not can_run_medic:
                    self.game['current_player'] = self.__get_next_player()
            elif card[util.ABILITY] == util.DECOY:
                pass
            else:
                self.game['current_player'] = self.__get_next_player()

            self.__set_status('player_%i_next' % self.game['current_player'])

            if self.game['current_player'] is None:
                self.__factor_round_winner()
                self.__next_round(current_round, self.game['rounds'][current_round]['winner'])
        else:
            print '\nCANNOT FIND THIS CARD'

        return self.game

    def revive_card(self, card_id):
        player_index = self.game['current_player']
        player = self.game['players'][player_index]
        card = None

        i = 0
        index = None
        for _card in player['graveyard']:
            if _card[util.ID] == card_id:
                card = _card
                index = i
            i += 1

        if not card:
            print '\n CANNOT FIND THIS CARD IN GRAVEYARD'
            return

        del player['graveyard'][index]

        player['cards'][card[util.ROW]].append(card)

        return self.play_card(card[util.ID])

    def trade_cycle(self, player_index, num_cards):
        if not self.__game_playable():
            self.logger.print_unplayable_game(self)
            return None

        if player_index == util.COMPUTER and self.computer_turn is not False:
            self.computer_trade_round(self, num_cards, self.game['players'][util.COMPUTER]['cards'])
        elif player_index == util.PLAYER and self.has_player is False:
            self.computer_trade_round(self, num_cards, self.game['players'][util.PLAYER]['cards'])
        else:
            self.cli.prompt_trade_cycle(num_cards)

    def pass_round(self):
        if not self.__game_playable():
            self.logger.print_unplayable_game(self)
            return None

        current_round = self.game['round']
        player_index = self.game['current_player']

        self.__reset_prompt()
        self.logger.print_pass(self, player_index)

        self.game['players'][player_index]['passed'][current_round] = True
        self.game['current_player'] = self.__get_next_player()

        self.factor_board()
        self.__set_status('player_%i_passed' % player_index, True)

        if self.game['current_player'] is None:
            self.__factor_round_winner()
            self.__next_round(self.game['round'], self.game['rounds'][current_round]['winner'])
        else:
            self.__set_status('player_%i_next' % self.game['current_player'])

        return self.game

    def get_cards_left(self):
        response = []

        for player_index in range(2):
            player = self.game['players'][player_index]
            cards = 0

            for row in player['cards']:
                cards += row.__len__()

            response.append(cards)

        return response

    def get_passed(self, current_round):
        player_passed = self.game['players'][util.PLAYER]['passed'][current_round]
        computer_passed = self.game['players'][util.COMPUTER]['passed'][current_round]

        return player_passed, computer_passed

    def calculate_round_totals(self, current_round):
        player_score = 0
        computer_score = 0

        player_index = 0

        for board in self.game['rounds'][current_round]['cards']:
            for row in board:
                for card in row:
                    if player_index == 0:
                        player_score += card[util.ACTUAL_STRENGTH]
                    else:
                        computer_score += card[util.ACTUAL_STRENGTH]

            player_index += 1

        return [player_score, computer_score]

    def swap_card(self, player, card_id):
        _card = self.__get_card(player['cards'], card_id)

        if _card is not None:
            old_card = _card[0]
            row = _card[1]
            index = _card[2]

            order = util.randomize_array(player['unused_cards'])

            new_card = player['unused_cards'][order[0]]
            del player['unused_cards'][order[0]]
            player['unused_cards'].append(old_card)

            new_row = new_card[util.ROW]

            del player['cards'][row][index]
            player['cards'][new_row].append(new_card)
            player['cards'][new_row].sort()

    def factor_board(self):
        scores = []

        for current_round in range(3):
            board = self.game['rounds'][current_round]['cards']
            _scores = {
                'totals': [0, 0],
                'rows': [[0, 0, 0], [0, 0, 0]],
                'cards': [[[], [], []], [[], [], []]]
            }

            for x in range(2):
                rows = board[x]

                for row in rows:
                    has_weather = False
                    boost_modifier = 0
                    pre_bonded = []

                    for card in row:
                        if card[util.ABILITY] == util.WEATHER:
                            has_weather = True

                        if card[util.ABILITY] == util.BOND:
                            pre_bonded.append(card[util.AFFECTS])

                        if card[util.ABILITY] == util.BOOST:
                            boost_modifier += 1

                    bonded = util.get_duplicates(pre_bonded)

                    for card in row:
                        bond_modifier = 1
                        card_boost = copy.copy(boost_modifier)

                        if card[util.AFFECTS] in bonded:
                            bond_modifier = pre_bonded.count(card[util.AFFECTS])
                            card[util.ACTUAL_STRENGTH] = int(card[util.BASE_STRENGTH]) * bond_modifier

                        if card[util.ABILITY] == util.BOOST:
                            card_boost -= 1

                        if has_weather:
                            if card[util.ABILITY] == util.HERO:
                                pass
                            elif card[util.BASE_STRENGTH] == 0:
                                pass
                            else:
                                card[util.ACTUAL_STRENGTH] = bond_modifier + card_boost
                        else:
                            if bond_modifier > 1:
                                card[util.ACTUAL_STRENGTH] += card_boost
                            else:
                                card[util.ACTUAL_STRENGTH] = card[util.BASE_STRENGTH] + card_boost

                        _scores['totals'][x] += card[util.ACTUAL_STRENGTH]
                        _scores['rows'][x][card[util.ROW]] += card[util.ACTUAL_STRENGTH]
                        _scores['cards'][x][card[util.ROW]].append(card[util.ACTUAL_STRENGTH])

            self.game['rounds'][current_round]['scores'] = _scores
            scores.append(_scores)

        return scores

    def determine_last_round_winner(self, current_round):
        last_round = current_round - 1
        totals = self.calculate_round_totals(last_round)
        winner = None

        if totals[util.PLAYER] > totals[util.COMPUTER]:
            self.__increment_losses(util.COMPUTER)
            self.game['rounds'][last_round]['winner'] = util.PLAYER
            self.__set_status('round_%i_player_0_win' % last_round)
            winner = 0
        elif totals[util.COMPUTER] > totals[util.PLAYER]:
            self.__increment_losses(util.PLAYER)
            self.game['rounds'][last_round]['winner'] = util.COMPUTER
            self.__set_status('round_%i_player_1_win' % last_round)
            winner = 1
        else:
            self.__increment_losses(util.PLAYER)
            self.__increment_losses(util.COMPUTER)
            self.game['rounds'][last_round]['winner'] = None
            self.__set_status('round_%i_tie' % last_round)

        self.logger.print_winner(self, winner)

        winner = self.__check_winner()

        if winner is not None or last_round == 2:
            if winner == 'tie':
                self.logger.print_game_winner(self, None)
            else:
                self.logger.print_game_winner(self, self.game['winner'])

        return winner

    def finish_game(self):
        pass

    def __game_playable(self):
        if self.game['round'] > 2:
            return False

        if self.game['winner'] is not None:
            return False

        return True

    def __check_winner(self):
        player_losses = self.game['players'][util.PLAYER]['losses']
        computer_losses = self.game['players'][util.COMPUTER]['losses']
        player_lost = False
        computer_lost = False

        if player_losses[0] is True and player_losses[1] is True:
            player_lost = True

        if computer_losses[0] is True and computer_losses[1] is True:
            computer_lost = True

        if player_lost and computer_lost:
            self.game['winner'] = 'tie'
        elif player_lost:
            self.game['winner'] = util.COMPUTER
        elif computer_lost:
            self.game['winner'] = util.PLAYER

        return self.game['winner']

    def __increment_losses(self, loser):
        losses = self.game['players'][loser]['losses']

        if not losses[0]:
            losses[0] = True
        else:
            losses[1] = True

    def __set_graveyards(self, current_round):
        board = self.game['rounds'][current_round]['cards']

        for player_index in range(2):
            rows = board[player_index]

            for row in rows:
                for card in row:
                    if not card[util.ABILITY] == util.HERO \
                            and not card[util.ABILITY] == util.WEATHER \
                            and not card[util.ABILITY] == util.SCORCH:

                        self.game['players'][player_index]['graveyard'].append(card)

    def __set_status(self, status, reset=False):
        if reset:
            self.game['status'] = []

        self.game['status'].append(status)

        return self.game

    def __set_prompt(self, prompt):
        self.game['prompt'] = prompt

        return self.game

    def __reset_prompt(self):
        self.__last_prompt = self.game['prompt']
        self.game['prompt'] = None

        return self.game

    def __get_next_player(self):
        current_round = self.game['round']
        current_player = self.game['current_player']
        next_player = int(not current_player)
        passed = self.get_passed(current_round)

        if passed[next_player] and passed[current_player]:
            next_player = None
        elif passed[next_player]:
            next_player = current_player

        return next_player

    def __get_card(self, cards, card_id):
        card = None
        card_index = None
        card_row = None

        x = 0
        for row in cards:
            y = 0

            for _card in row:
                if _card[util.ID] == card_id:
                    card = copy.copy(_card)
                    card_index = y
                    card_row = x

                y += 1
            x += 1

        return [card, card_row, card_index] if card is not None else None

    def __factor_round_winner(self):
        current_round = self.game['round']
        return self.determine_last_round_winner(current_round + 1)

    def __next_round(self, current_round, round_winner):
        new_round = current_round + 1

        if new_round > 2:
            return False

        self.game['round'] = new_round
        self.__set_status('round_%i_start' % new_round)
        self.__set_graveyards(current_round)

        if round_winner is not None:
            self.__set_status('player_%i_start' % round_winner)
            self.game['current_player'] = round_winner
        else:
            rand = util.rand0_1()
            self.__set_status('player_%i_start' % rand)
            self.game['current_player'] = rand

        return self.game

    def __setup_round(self):
        return {'cards': [[[], [], []], [[], [], []]], 'scores': {}, 'winner': None}

    def __setup_player(self, all_cards):
        cards = self.__setup_cards(all_cards)
        return {'cards': cards[0], 'unused_cards': cards[1], 'graveyard': [], 'points': 0,
                'passed': [False, False, False], 'losses': [False, False], 'lost': False}

    def __setup_cards(self, _cards):
        cards = copy.deepcopy(_cards)

        for card in cards:
            card.append(util.generate_uuid())
            card.append(card[util.BASE_STRENGTH])

        order = util.randomize_array(cards)
        ordered = order[:10]

        filled = []
        delete = []

        for i in ordered:
            filled.append(cards[i])
            delete.append(i)

        for i in sorted(ordered, reverse=True):
            del cards[i]

        filled = util.sort_cards(filled)

        return [filled, cards]

    def __str_board(self, current_round):
        board = self.game['rounds'][current_round]['cards']
        output = []

        for x in range(2):
            cards = board[x]
            total_points = 0
            row_output = []

            for row in cards:
                row_points = 0
                card_outputs = []

                for card in row:
                    card_output = '%02d:%d' % (card[util.ACTUAL_STRENGTH], card[util.ABILITY])
                    card_outputs.append(card_output)
                    row_points += card[util.ACTUAL_STRENGTH]

                row_output.append('[%03d]%s' % (row_points, ','.join(card_outputs)))
                total_points += row_points

            output.append('{%03d}%s' % (total_points, '|'.join(row_output)))

        print '/'.join(output)

    def __run_spy(self, player_index):
        player = self.game['players'][player_index]
        order = util.randomize_array(player['unused_cards'])
        ordered = order[:2]

        self.logger.print_drew_cards(self, 2)

        for card_index in sorted(ordered, reverse=True):
            new_card = player['unused_cards'][card_index]
            new_row = new_card[util.ROW]

            self.logger.print_card_name(self, new_card)

            del player['unused_cards'][card_index]
            player['cards'][new_row].append(new_card)
            player['cards'][new_row].sort()

    def __run_scorch(self):
        current_round = self.game['round']
        board = self.game['rounds'][current_round]['cards']
        top_points = 0
        scorch_cards = []

        for player_index in range(2):
            rows = board[player_index]

            for row in rows:
                for card in row:
                    if card[util.ABILITY] is not util.HERO and card[util.ACTUAL_STRENGTH] > top_points:
                        top_points = card[util.ACTUAL_STRENGTH]

        for player_index in range(2):
            rows = board[player_index]

            for row in rows:
                for card in row:
                    if card[util.ABILITY] is not util.HERO and card[util.ACTUAL_STRENGTH] == top_points:
                        scorch_cards.append(card[util.ID])

        for player_index in range(2):
            for card_id in scorch_cards:
                card = self.__get_card(board[player_index], card_id)

                if card is not None:
                    row = card[1]
                    index = card[2]

                    del board[player_index][row][index]
                    self.game['players'][player_index]['graveyard'].append(card[0])

    def __run_clear_weather(self):
        current_round = self.game['round']
        board = self.game['rounds'][current_round]['cards']

        for player_index in range(2):
            cards = board[player_index]

            x = 0
            for row in cards:
                y = 0
                for card in row:
                    if card[util.ABILITY] == util.WEATHER:
                        del cards[x][y]
                    y += 1
                x += 1

    def __run_medic(self):
        player_index = self.game['current_player']

        if self.game['players'][player_index]['graveyard'].__len__() > 0:
            self.__set_prompt('player_%i_medic_revival' % player_index)
            return True

        return False

