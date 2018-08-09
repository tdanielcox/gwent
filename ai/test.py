from sys import path
path.append('..')

from game.Gwent import Gwent
from ai.Ai import round_actions, trade_actions


num_rounds = 1


for x in range(num_rounds):
    gwent = Gwent({'enable_logging': True})
    gwent.new()
    gwent.start_cli(0, round_actions, trade_actions)
