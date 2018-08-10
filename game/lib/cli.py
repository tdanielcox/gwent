from game.lib import util


class CLI:
    def __init__(self, Gwent, Logger):
        self.gwent = Gwent
        self.logger = Logger

    def start_round(self, current_round):
        if self.gwent.game['winner'] is None:
            self.gwent.game['round'] = current_round

            for x in range(60):
                passed = self.gwent.get_passed(current_round)
                if passed[0] and passed[1]:
                    break

                self.start_iteration(current_round, x)

    def start_iteration(self, current_round, current_iteration):
        board_scores = self.gwent.factor_board()
        player_index = self.gwent.game['current_player']

        self.logger.print_round_info(self.gwent, current_iteration)

        if player_index == util.COMPUTER and self.gwent.computer_turn is not False:
            self.gwent.computer_turn(self.gwent, current_round, self.gwent.game['players'][util.COMPUTER]['cards'])
        elif player_index == util.PLAYER and self.gwent.has_player is False:
            self.gwent.computer_turn(self.gwent, current_round, self.gwent.game['players'][util.PLAYER]['cards'])
        else:
            self.prompt_player_move()

        # if current_iteration == 5:
        #     exit()

        return self.gwent.game

    def prompt_trade_cycle(self, num_cards):
        player = self.gwent.game['players'][util.PLAYER]

        print 'Trading Round'

        title = '\n%s\'s turn' % util.parse_player(util.PLAYER)
        self.logger.print_hand(self.gwent, title, player['cards'])

        for i in range(num_cards):
            suffix = 'st' if i == 0 else 'nd'
            print '\n%i%s trade' % (i + 1, suffix)

            card_id = raw_input('\nWhat card would you like to trade? ')
            self.gwent.swap_card(player, card_id)
            self.logger.print_hand(self.gwent, '\n\nYour cards are now: ', player['cards'])

    def prompt_player_move(self):
        player_index = self.gwent.game['current_player']
        player = self.gwent.game['players'][player_index]
        current_round = self.gwent.game['round']

        print util.SEPARATOR

        if not player['passed'][current_round]:
            self.logger.print_board(self.gwent, current_round)

            title = '\n%s\'s Cards' % util.parse_player(player_index)
            self.logger.print_hand(self.gwent, title, player['cards'])

            print '\nType P to pass this round'
            user_input = raw_input('What card do you want to play? ')

            if user_input == 'P':
                self.gwent.pass_round()
            else:
                card_id = user_input
                self.gwent.play_card(card_id)

        else:
            print util.SEPARATOR
            print '\n%s passed.' % util.parse_player(player_index)






