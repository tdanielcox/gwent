from game.Gwent import Gwent
from game import lib as _

def play_card(game, row, hand):
    gwent = Gwent()
    gwent.load(game)

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


