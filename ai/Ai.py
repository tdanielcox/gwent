from game.lib import util


def play_card(gwent, row, hand):
    index = 0
    card = hand[row][index]
    gwent.play_card(card[util.ID])


def pass_card(gwent):
    gwent.pass_round()


def round_actions(gwent, current_round, hand, row=0):
    try:
        play_card(gwent, row, hand)
    except:
        row += 1

        if row > 3:
            gwent.pass_round()
        else:
            round_actions(gwent, current_round, hand, row)


def trade_actions(gwent, num_cards, hand, row=0):
    try:
        play_card(gwent, row, hand)
    except:
        row += 1

        if row > 2:
            gwent.pass_round()
        else:
            # round_actions(gwent, current_round, hand, row)
            pass


