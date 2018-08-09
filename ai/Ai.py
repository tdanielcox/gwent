from game.lib import util
import random


def setup_cards(hand):
    cards = []
    for row in hand:
        for card in row:
            cards.append(card)

    return cards


def choose_card(cards):
    pass_modifier = 0

    num_cards = cards.__len__()
    rand = random.randint(0, num_cards + pass_modifier)

    return cards[rand]


def play_card(gwent, hand):
    cards = setup_cards(hand)
    card = choose_card(cards)

    if card is None:
        raise Exception('No card found')

    gwent.play_card(card[util.ID])


def round_actions(gwent, current_round, hand):
    try:
        play_card(gwent, hand)
    except:
        gwent.pass_round()


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


