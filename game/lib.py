import random

ROUNDS = 3
SEPARATOR = '\n-----------------------'

# players
PLAYER = 0
COMPUTER = 1

# rows
MELEE = 0
RANGED = 1
SEIGE = 2
SPECIAL = 3

# abilities
BOND = 0
SPY = 1
HERO = 2
BOOST = 3
MEDIC = 4
WEATHER = 5

# card array
NAME = 0
ROW = 1
BASE_STRENGTH = 2
ABILITY = 3
ACTUAL_STRENGTH = 4

def parse_player(index):
	if (index == PLAYER):	
		return 'Player'
	elif (index == COMPUTER):
		return 'Computer'

def parse_row(index):
	if (index == MELEE):	
		return 'Melee'
	elif (index == RANGED):
		return 'Ranged'
	elif (index == SEIGE):
		return 'Seige'
	elif (index == SPECIAL):
		return 'Special'

def parse_special(index):
	if (index == BOND):
		return 'Bond'
	elif (index == SPY):
		return 'Spy'
	elif (index == HERO):
		return 'Hero'
	elif (index == BOOST):
		return 'Boost'
	elif (index == MEDIC):
		return 'Medic'
	elif (index == WEATHER):
		return 'Weather'

def parse_display_name(card):
	if (card[ABILITY] is not None):
		return '(%i) %s [%s]' % (card[ACTUAL_STRENGTH], card[NAME], parse_special(card[ABILITY]))
	else:
		return '(%i) %s' % (card[ACTUAL_STRENGTH], card[NAME])

def randomize_array(array):	
	num = array.__len__()
	array = list(xrange(0, num))
	random.shuffle(array)
	return array

def sort_cards(cards):
	rows = [[],[],[],[]]
	cards.sort()

	for card in cards:
		rows[card[ROW]].append(card)

	return rows

def rand0_1():
	return round(random.uniform(0,1))

def cls():
	print '\n' * 100