import json
from flask import Flask, request
from game.Gwent import Gwent
from ai.Ai import computer_round_actions
from db import create_table, save_game, get_game

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route("/start-game", methods=['POST'])
def api_start_game():
    gwent = Gwent()
    gwent.new()
    game = gwent.start(1, computer_round_actions)
    game = save_game(game, True)

    return json.dumps(game)


@app.route("/get-game", methods=['GET'])
def api_get_game():
    game_id = request.args.get('game_id')
    print game_id
    game = get_game(game_id)

    return json.dumps(game)


@app.route("/play-card", methods=['POST'])
def api_play_card():
    game_id = request.args.get('game_id')
    request_data = request.get_json()
    card_id = request_data['card_id']

    game = get_game(game_id)

    gwent = Gwent()
    gwent.load(game)
    gwent.start(1, computer_round_actions)
    game = gwent.play_card(card_id)
    game = save_game(game)

    return json.dumps(game)
