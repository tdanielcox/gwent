from game.Gwent import Gwent
from game import lib as _
from Ai import computer_round_actions

gwent = Gwent()
gwent.new(0, computer_round_actions)

# for player_index in range(2):
# 	gwent.trade_cycle(player_index, 2)

for current_round in range(3):
    gwent.start_round(current_round)
