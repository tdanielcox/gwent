import lib as _
import random
import copy
from cards import nr_cards

class Gwent:
	game = {}

	def start(self):
		self.game = {
			'round': 0, 
			'loser': None,
			'current_player': 0,
			'rounds': [
				self.__setup_round(),
				self.__setup_round(),
				self.__setup_round(),
			],
			'players': [
				self.__setup_player(nr_cards), 
				self.__setup_player(nr_cards), 
			], 
		}

		for player_index in range(2):
			self.trade_cycle(player_index)

		for current_round in range(3):
			self.start_round(current_round)

	def trade_cycle(self, player_index):
		_.cls()

		player = self.game['players'][player_index]

		print 'Trading Round'

		title = '\n%s\'s turn' % _.parse_player(player_index)
		self.__print_hand(title, player['cards'])

		for i in range(2):
			suffix = 'st' if i == 0 else 'nd'
			print '\n%i%s trade' % (i + 1, suffix)

			row, col = raw_input('\nWhat card would you like to trade? ').split()
			self.__swap_card(player, int(row), int(col))
			_.cls()
			
			self.__print_hand('\n\nYour cards are now: ', player['cards'])

	def start_round(self, current_round):
		_.cls()

		if (current_round > 0):
			print _.SEPARATOR
			self.__determine_last_round_winner(current_round)

		if (self.game['loser'] != None):
			_.cls()
			print '%s Wins!' % _.parse_player(not self.game['loser'])
		else:
			if (current_round == 0):
				first = _.rand0_1()
				self.game['current_player'] = int(first)

			self.game['round'] = current_round

			for x in range(60):
				_.cls()
				self.__factor_board()
				self.__print_round_info(x)
				self.__start_player_turn()

				player = not self.game['current_player']
				self.game['current_player'] = player

	def __print_round_info(self, iteration):
		player_index = self.game['current_player']
		player = self.game['players'][player_index]
		current_round = self.game['round']

		totals = self.__calculate_round_totals(current_round)
		cards_left = self.__get_cards_left()

		passed = self.__get_passed(current_round)
		player_passed = 'PASSED' if passed[0] == True else ''
		computer_passed = 'PASSED' if passed[1] == True else ''

		if (iteration == 0):
			print 'Round %i started.' % (current_round + 1)
			print '\n%s will go first.' % _.parse_player(player_index)
		else:
			print 'Round %i - Turn %i\n' % (current_round + 1, iteration + 1)
			print '%s: %i (%i cards) %s' % (_.parse_player(_.PLAYER), totals[0], cards_left[0], player_passed)
			print '%s: %i (%i cards) %s' % (_.parse_player(_.COMPUTER), totals[1], cards_left[1], computer_passed)

			print '\n%s\'s Turn' % _.parse_player(player_index)

	def __get_cards_left(self):
		response = []

		for player_index in range(2):
			player = self.game['players'][player_index]
			cards = 0

			for row in player['cards']:
				cards += row.__len__()

			response.append(cards)

		return response

	def __get_passed(self, current_round):
		player_passed = self.game['players'][0]['passed'][current_round]
		computer_passed = self.game['players'][1]['passed'][current_round]

		return [player_passed, computer_passed]

	def __determine_last_round_winner(self, current_round):
		last_round = current_round - 1
		totals = self.__calculate_round_totals(last_round)

		if totals[0] > totals[1]:
			self.__increment_losses(1)
			self.game['rounds'][last_round]['winner'] = _.PLAYER
			print '\nPLayer wins!'
		elif totals[1] > totals[0]:
			self.__increment_losses(0)
			self.game['rounds'][last_round]['winner'] = _.COMPUTER
			print '\nComputer wins!'
		else:
			self.__increment_losses(0)
			self.__increment_losses(1)
			self.game['rounds'][last_round]['winner'] = None
			print '\nTie!'

	def __increment_losses(self, loser):
		losses = self.game['players'][loser]['losses']

		if (losses[0] == False):
			losses[0] = True
		else:
			losses[1] = True
			self.game['loser'] = loser

	def __calculate_round_totals(self, current_round):
		player_score = 0
		computer_score = 0

		player_index = 0

		for board in self.game['rounds'][current_round]['cards']:
			for row in board:
				for card in row:
					if (player_index == 0):
						player_score += card[_.ACTUAL_STRENGTH]
					else:
						computer_score += card[_.ACTUAL_STRENGTH]

			player_index += 1

		return [player_score, computer_score]		

	def __start_player_turn(self):
		player_index = self.game['current_player']
		player = self.game['players'][player_index]
		current_round = self.game['round']

		if (player['passed'][current_round] == False):
			print _.SEPARATOR
			self.__print_board(current_round)
			self.__prompt_player_move()
		else:
			print _.SEPARATOR
			print '\n%s passed.' % _.parse_player(player_index)

	def __prompt_player_move(self):
		player_index = self.game['current_player']
		player = self.game['players'][player_index]

		print _.SEPARATOR

		title = '\n%s\'s Cards' % _.parse_player(player_index)
		self.__print_hand(title, player['cards'])

		print '\nType P to pass this round'
		user_input = raw_input('What card do you want to play? ')

		if (user_input == 'P'):
			self.__run_pass(player_index)
		else:
			row, col = user_input.split()
			self.__play_card(int(row), int(col))

	def __play_card(self, row, index):
		current_round = self.game['round']
		player_index = self.game['current_player']
		player = self.game['players'][player_index]
		card = copy.copy(player['cards'][row][index])

		del player['cards'][row][index]

		if (card[_.ROW] == 3):
			if (card[_.ABILITY] == _.WEATHER):
				self.__run_clear_weather()
		else:
			if (card[_.ABILITY] == _.SPY):
				self.__run_spy(player_index)
				opponent_index = not player_index
				self.game['rounds'][current_round]['cards'][opponent_index][row].append(card)
			elif (card[_.ABILITY] == _.WEATHER):
				opponent_index = not player_index
				self.game['rounds'][current_round]['cards'][player_index][row].append(card)
				self.game['rounds'][current_round]['cards'][opponent_index][row].append(card)
			else:
				self.game['rounds'][current_round]['cards'][player_index][row].append(card)

		print _.SEPARATOR
		print '\nYou played: (%i) %s' % (card[_.BASE_STRENGTH], card[_.NAME])

	def __setup_round(self):
		return {'cards': [[[],[],[]],[[],[],[]]], 'winner': None}

	def __setup_player(self, all_cards):
		cards = self.__setup_cards(all_cards)
		return {'cards': cards[0], 'unused_cards': cards[1], 'points': 0, 'passed': [False, False, False], 'losses': [False, False], 'lost': False}

	def __setup_cards(self, cards):
		for card in cards:
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

		return [ filled, cards ]

	def __print_hand(self, title, cards):
		print title

		x = 0;
		for row in cards:
			y = 0

			try:
				row_title = row[0][1]

				print '\n--- ' + _.parse_row(row_title)
				for card in row:
					display_name = _.parse_display_name(card)
					print '%i-%i: %s' % (x, y, display_name)
					y += 1
				x += 1
			except:
				x += 1
				pass

	def __factor_board(self):
		current_round = self.game['round']
		board = self.game['rounds'][current_round]['cards']

		for x in range(2):
			cards = board[x]

			for row in cards:
				has_weather = False

				for card in row:
					if (card[_.ABILITY] == _.WEATHER):
						has_weather = True

				for card in row:
					if (has_weather):
						if (card[_.ABILITY] == _.HERO):
							pass
						elif (card[_.BASE_STRENGTH] == 0):
							pass
						else:
							card[_.ACTUAL_STRENGTH] = 1
					else:
						card[_.ACTUAL_STRENGTH] = card[_.BASE_STRENGTH]

	def __print_board(self, rnd):
		print '\nThe current board is: '

		board = self.game['rounds'][rnd]['cards']

		for x in range(2):
			cards = board[x]
			total_points = 0

			if (x == _.COMPUTER):
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

	def __swap_card(self, player, row, index):
		old_card = player['cards'][row][index]
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

		print '\nYou drew 2 cards:'

		for card_index in sorted(ordered, reverse=True):
			new_card = player['unused_cards'][card_index]
			new_row = new_card[_.ROW]

			print _.parse_display_name(new_card)

			del player['unused_cards'][card_index]
			player['cards'][new_row].append(new_card)
			player['cards'][new_row].sort()

	def __run_pass(self, player_index):
		current_round = self.game['round']
		self.game['players'][player_index]['passed'][current_round] = True

		print _.SEPARATOR
		print '\n%s passed.' % _.parse_player(player_index)

	def __run_clear_weather(self):
		current_round = self.game['round']
		board = self.game['rounds'][current_round]['cards']

		for player_index in range(2):
			cards = board[player_index]

			x = 0
			for row in cards:
				y = 0
				for card in row:
					if (card[_.ABILITY] == _.WEATHER):
						del cards[x][y]
					y += 1
				x += 1
