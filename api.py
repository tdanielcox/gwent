from flask import Flask

app = Flask(__name__)

game = {}


@app.route("/")
def start_game():
    print "hi"
    game = None
    return "Game started: %s" % str(game)
