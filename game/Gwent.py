import lib as _
import random
import copy
from cards import nr_cards
from logger import Logger


class Gwent:
    def __init__(self, options={}):
        self.game = {}
        self.__has_player = True
        self.__computer_turn = None
        self.__cli_output = True
        self.__enable_logging = True \

        if 'enable_logging' in options and options['enable_logging'] is True:
            enable_logging = True
        else:
            enable_logging = False

        self.logger = Logger(enable_logging)

    def new(self):
        first_player = _.rand0_1()

        self.game = {
            'id': _.generate_uuid(),
            'round': 0,
            'loser': None,
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
            'status': ['round_0_start', 'player_%i_start' % first_player]
        }

        return self.game

    def load(self, blob):
        self.game = blob

        return self.game

    def start(self, player_count, computer_round_actions):
        if player_count == 0:
            self.__has_player = False
            self.__computer_turn = computer_round_actions
        elif player_count == 1:
            self.__computer_turn = computer_round_actions

        self.__factor_board()

        return self.game

    def trade_cycle(self, player_index, num_cards):
        player = self.game['players'][player_index]

        print 'Trading Round'

        title = '\n%s\'s turn' % _.parse_player(player_index)
        self.logger.print_hand(self, title, player['cards'])

        for i in range(num_cards):
            suffix = 'st' if i == 0 else 'nd'
            print '\n%i%s trade' % (i + 1, suffix)

            card_id = raw_input('\nWhat card would you like to trade? ')
            self.__swap_card(player, card_id)
            self.logger.print_hand(self, '\n\nYour cards are now: ', player['cards'])

    def start_round(self, current_round):
        if current_round > 0:
            self.__determine_last_round_winner(current_round)

        if self.game['loser'] is not None:
            self.logger.print_winner(self, not self.game['loser'])
        else:
            self.game['round'] = current_round

            for x in range(60):
                passed = self.get_passed(current_round)
                if passed[0] and passed[1]:
                    break

                self.start_iteration(current_round, x)

        if current_round == 2:
            self.__finish_game()

    def start_iteration(self, current_round, current_iteration):
        board_scores = self.__factor_board()
        player_index = self.game['current_player']

        self.logger.print_round_info(self, current_iteration)

        if player_index == _.COMPUTER and self.__computer_turn is not False:
            self.__computer_turn(self.game, current_round, self.game['players'][_.COMPUTER]['cards'])
        elif player_index == _.PLAYER and self.__has_player is False:
            self.__computer_turn(self.game, current_round, self.game['players'][_.PLAYER]['cards'])
        else:
            self.__start_player_turn()

        if current_iteration == 5:
            exit()

        return self.game

    def ai_turn(self):
        current_round = self.game['round']
        self.__computer_turn(self.game, current_round, self.game['players'][_.COMPUTER]['cards'])

        return self.game

    def play_card(self, card_id):
        current_round = self.game['round']
        player_index = self.game['current_player']
        player = self.game['players'][player_index]

        _card = self.__get_card(player['cards'], card_id)

        if _card is not None:
            card = _card[0]
            row = _card[1]
            index = _card[2]

            del player['cards'][row][index]

            if card[_.ROW] == 3:
                if card[_.ABILITY] == _.WEATHER:
                    self.__run_clear_weather()
                if card[_.ABILITY] == _.SCORCH:
                    self.__run_scorch()
            else:
                if card[_.ABILITY] == _.SPY:
                    self.__run_spy(player_index)
                    opponent_index = not player_index
                    self.game['rounds'][current_round]['cards'][opponent_index][row].append(card)
                elif card[_.ABILITY] == _.WEATHER:
                    opponent_index = not player_index
                    self.game['rounds'][current_round]['cards'][player_index][row].append(card)
                    self.game['rounds'][current_round]['cards'][opponent_index][row].append(card)
                else:
                    self.game['rounds'][current_round]['cards'][player_index][row].append(card)

            self.logger.print_card_played(self, player_index, card)

            self.__set_status('player_%i_play_card' % self.game['current_player'], True)
            self.__factor_board()
            self.game['current_player'] = self.__get_next_player()
            self.__set_status('player_%i_next' % self.game['current_player'])

            if self.game['current_player'] is None:
                self.__factor_round_winner()
                self.__next_round(current_round, self.game['rounds'][current_round]['winner'])
        else:
            print '\nCANNOT FIND THIS CARD'

        return self.game

    def pass_round(self, player_index):
        current_round = self.game['round']

        self.__run_pass(player_index)
        self.game['current_player'] = self.__get_next_player()

        self.__factor_board()
        self.__set_status('player_%i_passed' % player_index, True)

        if self.game['current_player'] is None:
            self.__factor_round_winner()
            self.__next_round(self.game['round'], self.game['rounds'][current_round]['winner'])
        else:
            self.__set_status('player_%i_next' % self.game['current_player'])

        return self.game

    def __set_status(self, status, reset=False):
        if reset:
            self.game['status'] = []

        self.game['status'].append(status)

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
                if _card[_.ID] == card_id:
                    card = copy.copy(_card)
                    card_index = y
                    card_row = x

                y += 1
            x += 1

        return [card, card_row, card_index] if card is not None else None

    def __finish_game(self):
        pass

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
        player_passed = self.game['players'][_.PLAYER]['passed'][current_round]
        computer_passed = self.game['players'][_.COMPUTER]['passed'][current_round]

        return [player_passed, computer_passed]

    def __factor_round_winner(self):
        current_round = self.game['round']
        return self.__determine_last_round_winner(current_round + 1)

    def __determine_last_round_winner(self, current_round):
        last_round = current_round - 1
        totals = self.calculate_round_totals(last_round)
        winner = None

        if totals[_.PLAYER] > totals[_.COMPUTER]:
            self.__increment_losses(_.COMPUTER)
            self.game['rounds'][last_round]['winner'] = _.PLAYER
            self.__set_status('round_%i_player_0_win' % last_round)
            winner = 0
        elif totals[_.COMPUTER] > totals[_.PLAYER]:
            self.__increment_losses(_.PLAYER)
            self.game['rounds'][last_round]['winner'] = _.COMPUTER
            self.__set_status('round_%i_player_1_win' % last_round)
            winner = 1
        else:
            self.__increment_losses(_.PLAYER)
            self.__increment_losses(_.COMPUTER)
            self.game['rounds'][last_round]['winner'] = None
            self.__set_status('round_%i_tie' % last_round)

        self.logger.print_winner(self, 0)

        return winner

    def __increment_losses(self, loser):
        losses = self.game['players'][loser]['losses']

        if not losses[0]:
            losses[0] = True
        else:
            losses[1] = True
            self.game['loser'] = loser

    def calculate_round_totals(self, current_round):
        player_score = 0
        computer_score = 0

        player_index = 0

        for board in self.game['rounds'][current_round]['cards']:
            for row in board:
                for card in row:
                    if player_index == 0:
                        player_score += card[_.ACTUAL_STRENGTH]
                    else:
                        computer_score += card[_.ACTUAL_STRENGTH]

            player_index += 1

        return [player_score, computer_score]

    def __start_player_turn(self):
        player_index = self.game['current_player']
        player = self.game['players'][player_index]
        current_round = self.game['round']

        if not player['passed'][current_round]:
            print _.SEPARATOR
            # self.logger.print_board(self, current_round)
            self.__str_board(current_round)
            self.__prompt_player_move()
        else:
            print _.SEPARATOR
            print '\n%s passed.' % _.parse_player(player_index)

    def __prompt_player_move(self):
        player_index = self.game['current_player']
        player = self.game['players'][player_index]

        print _.SEPARATOR

        title = '\n%s\'s Cards' % _.parse_player(player_index)
        self.logger.print_hand(self, title, player['cards'])

        print '\nType P to pass this round'
        user_input = raw_input('What card do you want to play? ')

        if user_input == 'P':
            self.__run_pass(player_index)
        else:
            card_id = user_input
            self.play_card(card_id)

    def __next_round(self, current_round, round_winner):
        new_round = current_round + 1

        if new_round > 2:
            return False

        self.game['round'] = new_round
        self.__set_status('round_%i_start' % new_round)

        if round_winner is not None:
            self.__set_status('player_%i_start' % round_winner)
            self.game['current_player'] = round_winner
        else:
            rand = _.rand0_1()
            self.__set_status('player_%i_start' % rand)
            self.game['current_player'] = rand

        return self.game

    def __setup_round(self):
        return {'cards': [[[], [], []], [[], [], []]], 'scores': {}, 'winner': None}

    def __setup_player(self, all_cards):
        cards = self.__setup_cards(all_cards)
        return {'cards': cards[0], 'unused_cards': cards[1], 'points': 0, 'passed': [False, False, False],
                'losses': [False, False], 'lost': False}

    def __setup_cards(self, _cards):
        cards = copy.deepcopy(_cards)

        for card in cards:
            card.append(_.generate_uuid())
            card.append(card[_.BASE_STRENGTH])

        order = _.randomize_array(cards)
        ordered = order[:10]

        filled = []
        delete = []

        for i in ordered:
            filled.append(cards[i])
            delete.append(i)

        for i in sorted(ordered, reverse=True):
            del cards[i]

        filled = _.sort_cards(filled)

        return [filled, cards]

    def __factor_board(self):
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
                        if card[_.ABILITY] == _.WEATHER:
                            has_weather = True

                        if card[_.ABILITY] == _.BOND:
                            pre_bonded.append(card[_.AFFECTS])

                        if card[_.ABILITY] == _.BOOST:
                            boost_modifier += 1

                    bonded = _.get_duplicates(pre_bonded)

                    for card in row:
                        bond_modifier = 1
                        card_boost = copy.copy(boost_modifier)

                        if card[_.AFFECTS] in bonded:
                            bond_modifier = pre_bonded.count(card[_.AFFECTS])
                            card[_.ACTUAL_STRENGTH] = int(card[_.BASE_STRENGTH]) * bond_modifier

                        if card[_.ABILITY] == _.BOOST:
                            card_boost -= 1

                        if has_weather:
                            if card[_.ABILITY] == _.HERO:
                                pass
                            elif card[_.BASE_STRENGTH] == 0:
                                pass
                            else:
                                card[_.ACTUAL_STRENGTH] = bond_modifier + card_boost
                        else:
                            if bond_modifier > 1:
                                card[_.ACTUAL_STRENGTH] += card_boost
                            else:
                                card[_.ACTUAL_STRENGTH] = card[_.BASE_STRENGTH] + card_boost

                        _scores['totals'][x] += card[_.ACTUAL_STRENGTH]
                        _scores['rows'][x][card[_.ROW]] += card[_.ACTUAL_STRENGTH]
                        _scores['cards'][x][card[_.ROW]].append(card[_.ACTUAL_STRENGTH])

            self.game['rounds'][current_round]['scores'] = _scores
            scores.append(_scores)

        return scores

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
                    card_output = '%02d:%d' % (card[_.ACTUAL_STRENGTH], card[_.ABILITY])
                    card_outputs.append(card_output)
                    row_points += card[_.ACTUAL_STRENGTH]

                row_output.append('[%03d]%s' % (row_points, ','.join(card_outputs)))
                total_points += row_points

            output.append('{%03d}%s' % (total_points, '|'.join(row_output)))

        print '/'.join(output)

    def __swap_card(self, player, card_id):
        _card = self.__get_card(player['cards'], card_id)

        if _card is not None:
            old_card = _card[0]
            row = _card[1]
            index = _card[2]

            order = _.randomize_array(player['unused_cards'])

            new_card = player['unused_cards'][order[0]]
            del player['unused_cards'][order[0]]
            player['unused_cards'].append(old_card)

            new_row = new_card[_.ROW]

            del player['cards'][row][index]
            player['cards'][new_row].append(new_card)
            player['cards'][new_row].sort()

    def __run_spy(self, player_index):
        player = self.game['players'][player_index]
        order = _.randomize_array(player['unused_cards'])
        ordered = order[:2]

        self.logger.print_drew_cards(self, 2)

        for card_index in sorted(ordered, reverse=True):
            new_card = player['unused_cards'][card_index]
            new_row = new_card[_.ROW]

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
                    if card[_.ABILITY] is not _.HERO and card[_.ACTUAL_STRENGTH] > top_points:
                        top_points = card[_.ACTUAL_STRENGTH]

        for player_index in range(2):
            rows = board[player_index]

            for row in rows:
                for card in row:
                    if card[_.ABILITY] is not _.HERO and card[_.ACTUAL_STRENGTH] == top_points:
                        scorch_cards.append(card[_.ID])

        for player_index in range(2):
            for card_id in scorch_cards:
                card = self.__get_card(board[player_index], card_id)

                if card is not None:
                    row = card[1]
                    index = card[2]

                    del board[player_index][row][index]
                    #todo: add to graveyard

    def __run_pass(self, player_index):
        current_round = self.game['round']
        self.game['players'][player_index]['passed'][current_round] = True

        self.logger.print_pass(Gwent, player_index)

    def __run_clear_weather(self):
        current_round = self.game['round']
        board = self.game['rounds'][current_round]['cards']

        for player_index in range(2):
            cards = board[player_index]

            x = 0
            for row in cards:
                y = 0
                for card in row:
                    if card[_.ABILITY] == _.WEATHER:
                        del cards[x][y]
                    y += 1
                x += 1
