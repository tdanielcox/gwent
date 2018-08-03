import lib as _


class Logger:
    def __init__(self, enable_logging):
        self.enable_logging = enable_logging

    def print_round_info(self, Gwent, iteration):
        if not self.enable_logging:
            return None

        player_index = Gwent.game['current_player']
        player = Gwent.game['players'][player_index]
        current_round = Gwent.game['round']

        totals = Gwent.calculate_round_totals(current_round)
        cards_left = Gwent.get_cards_left()

        passed = Gwent.get_passed(current_round)
        player_passed = 'PASSED' if passed[0] == True else ''
        computer_passed = 'PASSED' if passed[1] == True else ''

        _.cls()

        if iteration == 0:
            print 'Round %i started.' % (current_round + 1)
            print '\n%s will go first.' % _.parse_player(player_index)
        else:
            print 'Round %i - Turn %i\n' % (current_round + 1, iteration + 1)
            print '%s: %i (%i cards) %s' % (_.parse_player(_.PLAYER), totals[0], cards_left[0], player_passed)
            print '%s: %i (%i cards) %s' % (_.parse_player(_.COMPUTER), totals[1], cards_left[1], computer_passed)

            print '\n%s\'s Turn' % _.parse_player(player_index)

    def print_hand(self, Gwent, title, cards):
        if not self.enable_logging:
            return None

        print title

        x = 0
        for row in cards:
            y = 0

            try:
                row_title = row[0][1]

                print '\n--- ' + _.parse_row(row_title)
                for card in row:
                    display_name = _.parse_display_name(card)
                    card_id = card[_.ID]
                    print '%s: %s' % (card_id, display_name)
                    y += 1
                x += 1
            except:
                x += 1
                pass

    def print_winner(self, Gwent, player_index):
        if not self.enable_logging:
            return None

        _.cls()

        if player_index == 0:
            print '\nPlayer wins!'
        elif player_index == 1:
            print '\nComputer wins!'
        else:
            print '\nTie!'

    def print_board(self, Gwent, current_round):
        if not self.enable_logging:
            return None

        print '\nThe current board is: '

        board = Gwent.game['rounds'][current_round]['cards']

        for x in range(2):
            cards = board[x]
            total_points = 0

            if x == _.COMPUTER:
                print '\n---'

            print '\n%s:' % _.parse_player(x)

            for row in cards:
                row_points = 0
                card_outputs = []

                for card in row:
                    display_name = _.parse_display_name(card)
                    card_outputs.append(display_name)
                    row_points += card[_.ACTUAL_STRENGTH]

                output = ' | '.join(card_outputs)

                print '[%i] %s' % (row_points, output)
                total_points += row_points

            print 'Points: %i' % total_points

    def print_drew_cards(self, Gwent, num_cards):
        if not self.enable_logging:
            return None

        print '\nYou drew %i cards:' % num_cards

    def print_pass(self, Gwent, player_index):
        if not self.enable_logging:
            return None

        print _.SEPARATOR
        print '\n%s passed.' % _.parse_player(player_index)

    def print_card_name(self, Gwent, new_card):
        if not self.enable_logging:
            return None

        print _.parse_display_name(new_card)

    def print_card_played(self, Gwent, player_index, card):
        if not self.enable_logging:
            return None

        player_label = 'You' if player_index == 0 else 'Computer'

        print _.SEPARATOR
        print '\n%s played: (%i) %s' % (player_label, card[_.BASE_STRENGTH], card[_.NAME])

