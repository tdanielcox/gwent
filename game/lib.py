import random

ROUNDS = 3
SEPARATOR = '\n-----------------------'

# players
PLAYER = 0
COMPUTER = 1

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
	if (index == 0):	
		return 'Player'
	elif (index == 1):
		return 'Computer'

def parse_row(index):
	if (index == 0):	
		return 'Melee'
	elif (index == 1):
		return 'Ranged'
	elif (index == 2):
		return 'Seige'
	elif (index == 3):
		return 'Special'

def parse_special(index):
	if (index == 0):
		return 'Bond'
	elif (index == 1):
		return 'Spy'
	elif (index == 2):
		return 'Hero'
	elif (index == 3):
		return 'Boost'
	elif (index == 4):
		return 'Medic'
	elif (index == 5):
		return 'Weather'

def parse_display_name(card):
	if (card[ABILITY] is not None):
		display_name = '(%i) %s [%s]' % (card[ACTUAL_STRENGTH], card[NAME], parse_special(card[ABILITY]))
	else:
		display_name = '(%i) %s' % (card[ACTUAL_STRENGTH], card[NAME])

	return display_name

def randomize_array(array):	
	num = array.__len__()
	array = list(xrange(0, num))
	random.shuffle(array)
	return array

def sort_cards(cards):
	rows = [[],[],[],[]]
	cards.sort()

	for x in cards:
		index = x[1];
		rows[index].append(x)

	return rows

def rand0_1():
	return round(random.uniform(0,1))

def cls():
	print '\n' * 100