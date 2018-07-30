import sqlite3
import json


def db_conn():
    db = sqlite3.connect('data/dbgames')
    cursor = db.cursor()

    return db, cursor


def db_cleanup(db):
    db.close()


def create_table():
    db, cursor = db_conn()
    cursor.execute('CREATE TABLE IF NOT EXISTS games(id STRING PRIMARY KEY, blob TEXT)')
    db.commit()
    db.close()


def get_game(game_id):
    db, cursor = db_conn()
    cursor.execute('SELECT blob FROM games WHERE id = :id', {'id': game_id})
    data = cursor.fetchone()
    game = json.loads(data[0])
    db_cleanup(db)

    return game


def save_game(game, is_new=False):
    game_id = game['id']
    json_game = json.dumps(game)

    db, cursor = db_conn()
    if is_new:
        cursor.execute('INSERT INTO games (id, blob) VALUES (?, ?)', [game_id, json_game])
    else:
        cursor.execute('UPDATE games SET blob = ? WHERE id = ?', [json_game, game_id])

    db.commit()
    db_cleanup(db)

    return game
