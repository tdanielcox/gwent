from game.Gwent import Gwent
from game import lib as _

gwent = Gwent()

def play_card(row, hand):
    index = 0
    card = hand[row][index]
    gwent.play_card(card[_.ID])

def computer_round_actions(game, current_round, hand, row=0):
    # print 'COMPUTERS TURN'
    # print hand

    try:
        play_card(row, hand)
    except:
        row += 1

        if (row > 2):
            gwent.pass_round(game['current_player'])
        else:
            computer_round_actions(game, current_round, hand, row)


gwent.start(0, computer_round_actions)

# for player_index in range(2):
# 	gwent.trade_cycle(player_index, 2)

for current_round in range(3):
    gwent.start_round(current_round)
