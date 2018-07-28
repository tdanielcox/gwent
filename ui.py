import eel
import json
from game.Gwent import Gwent
from game import lib as _

gwent = Gwent()

eel.init('web')

current_round = 0


def computer_round_actions(game, current_round, hand):
    print 'COMPUTERS TURN'
    print hand

    try:
        card = hand[0][0]
        gwent.play_card(0, 0)
    except:
        gwent.pass_round(_.COMPUTER)


@eel.expose
def start_game():
    game = gwent.start(True, computer_round_actions)

    return json.dumps(game)


# for player_index in range(2):
# 	gwent.trade_cycle(player_index, 2)

# for current_round in range(3):
# 	gwent.start_round(current_round)

@eel.expose
def start_round():
    gwent.start_round(current_round)


# say_hello_py('Python World!')
# eel.say_hello_js('Python World!')   # Call a Javascript function

web_app_options = {
    'mode': 'chrome-app',
    'host': 'localhost',
    'port': 8080,
    'chromeFlags': ["--start-fullscreen"]
}

eel.start('index.html', options=web_app_options)  # Start (this blocks and enters loop)
