from sys import path
path.append('..')

from game.Gwent import Gwent
from ai.Ai import round_actions, trade_actions


for x in range(5000):
    gwent = Gwent({'enable_logging': True})
    gwent.new()
    gwent.start_cli(1, round_actions, trade_actions)
