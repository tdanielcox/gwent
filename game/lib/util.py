import random
import uuid

ROUNDS = 3
SEPARATOR = '\n-----------------------'

# players
PLAYER = 0
COMPUTER = 1

# rows
MELEE = 0
RANGED = 1
SIEGE = 2
SPECIAL = 3

# abilities
NONE = 0
BOND = 1
SPY = 2
HERO = 3
BOOST = 4
MEDIC = 5
WEATHER = 6
SCORCH = 7
DECOY = 8

# card array
NAME = 0
ROW = 1
BASE_STRENGTH = 2
ABILITY = 3
AFFECTS = 4
IMAGE_PATH = 5
ID = 6
ACTUAL_STRENGTH = 7


def parse_player(index):
    if index == PLAYER:
        return 'Player'
    elif index == COMPUTER:
        return 'Computer'


def parse_row(index):
    if index == MELEE:
        return 'Melee'
    elif index == RANGED:
        return 'Ranged'
    elif index == SIEGE:
        return 'Siege'
    elif index == SPECIAL:
        return 'Special'


def parse_special(index):
    if index == NONE:
        return None
    if index == BOND:
        return 'Bond'
    elif index == SPY:
        return 'Spy'
    elif index == HERO:
        return 'Hero'
    elif index == BOOST:
        return 'Boost'
    elif index == MEDIC:
        return 'Medic'
    elif index == WEATHER:
        return 'Weather'


def parse_display_name(card):
    if card[ABILITY] is not 0:
        return '(%i) %s [%s]' % (card[ACTUAL_STRENGTH], card[NAME], parse_special(card[ABILITY]))
    else:
        return '(%i) %s' % (card[ACTUAL_STRENGTH], card[NAME])


def randomize_array(array):
    num = array.__len__()
    array = list(xrange(0, num))
    random.shuffle(array)
    return array


def sort_cards(cards):
    rows = [[], [], [], []]
    cards.sort()

    for card in cards:
        rows[card[ROW]].append(card)

    return rows


def rand0_1():
    return int(round(random.uniform(0, 1)))


def cls():
    print '\n' * 5


def generate_uuid():
    return str(uuid.uuid4())


def get_duplicates(array):
    seen = set()
    dup = []

    for x in array:
        if x in seen:
            dup.append(x)

        seen.add(x)

    return dup
