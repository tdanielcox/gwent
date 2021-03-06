from game.Gwent import Gwent
from game.lib import util
from mocks import full_game


def test_new_game():
    gwent = Gwent()
    game = gwent.new()
    assert game['players'].__len__() == 2
    assert game['rounds'].__len__() == 3
    assert game['round'] == 0


def test_load_game():
    gwent = Gwent()
    game = gwent.load(full_game())
    assert game['id'] == '5104b41c-a61c-4532-8767-21f77cb68416'
    assert game['players'].__len__() == 2
    assert game['rounds'].__len__() == 3
    assert game['round'] == 0


def test_play_card():
    gwent = Gwent()
    gwent.load(full_game())
    gwent.start(1, None, None)

    # player play Blue Stripes Commando
    game = gwent.play_card('c4acb180-3553-45fc-b649-905dd9a6f75e')
    assert game['rounds'][0]['cards'][util.PLAYER][util.MELEE][0][util.ID] == 'c4acb180-3553-45fc-b649-905dd9a6f75e'
    assert game['rounds'][0]['cards'][util.PLAYER][util.MELEE][0][util.ACTUAL_STRENGTH] == 4
    assert game['rounds'][0]['scores']['cards'][util.PLAYER][util.MELEE][0] == 4
    assert game['rounds'][0]['scores']['rows'][util.PLAYER][util.MELEE] == 4
    assert game['rounds'][0]['scores']['totals'][util.PLAYER] == 4


def test_pass_rounds():
    gwent = Gwent()
    gwent.load(full_game())
    gwent.start(1, None, None)

    # player pass
    game = gwent.pass_round()
    assert game['players'][0]['passed'][0] is True
    assert game['current_player'] is 1
    assert game['round'] is 0

    # opponent pass
    game = gwent.pass_round()
    assert game['players'][1]['passed'][0] is True
    assert game['current_player'] is 0 or 1
    assert game['round'] is 1

    # test scores
    assert game['rounds'][0]['scores']['totals'][util.PLAYER] == 0
    assert game['rounds'][0]['scores']['totals'][util.COMPUTER] == 0


def test_graveyards():
    gwent = Gwent()
    gwent.load(full_game())
    gwent.start(1, None, None)

    # player play Blue Stripes Commando
    game = gwent.play_card('c4acb180-3553-45fc-b649-905dd9a6f75e')

    # opponent play Ves
    gwent.play_card('6e782f42-4aaa-497a-8e01-204216714c7e')

    # player/opponent pass
    gwent.pass_round()
    gwent.pass_round()

    # test graveyards
    assert game['players'][util.PLAYER]['graveyard'][0][util.ID] == 'c4acb180-3553-45fc-b649-905dd9a6f75e'
    assert game['players'][util.COMPUTER]['graveyard'][0][util.ID] == '6e782f42-4aaa-497a-8e01-204216714c7e'

    # reset first player to player
    gwent.game['current_player'] = util.PLAYER

    # player play Blue Stripes Commando
    game = gwent.play_card('64948108-1b28-41e2-9810-193b92418322')

    # opponent play Keira Metz
    gwent.play_card('727481c1-cc45-480f-b171-3683bcfb7335')

    # player/opponent pass
    gwent.pass_round()
    gwent.pass_round()

    # test graveyards
    assert game['players'][util.PLAYER]['graveyard'][1][util.ID] == '64948108-1b28-41e2-9810-193b92418322'
    assert game['players'][util.COMPUTER]['graveyard'][1][util.ID] == '727481c1-cc45-480f-b171-3683bcfb7335'


def test_card_abilities():
    gwent = Gwent()
    gwent.load(full_game())
    gwent.start(1, None, None)

    # player play Blue Stripes Commando
    game = gwent.play_card('c4acb180-3553-45fc-b649-905dd9a6f75e')
    assert game['rounds'][0]['cards'][util.PLAYER][util.MELEE][0][util.ACTUAL_STRENGTH] == 4

    # opponent play Ves
    gwent.play_card('6e782f42-4aaa-497a-8e01-204216714c7e')
    assert game['rounds'][0]['cards'][util.COMPUTER][util.MELEE][0][util.ACTUAL_STRENGTH] == 5

    # player play Blue Stripes Commando (bonded)
    game = gwent.play_card('64948108-1b28-41e2-9810-193b92418322')
    assert game['rounds'][0]['cards'][util.PLAYER][util.MELEE][0][util.ACTUAL_STRENGTH] == 8
    assert game['rounds'][0]['cards'][util.PLAYER][util.MELEE][1][util.ACTUAL_STRENGTH] == 8

    # opponent play Biting Frost (weather)
    game = gwent.play_card('00673012-3f0b-4dd3-8d95-aabaaf4765ac')
    assert game['rounds'][0]['cards'][util.PLAYER][util.MELEE][0][util.ACTUAL_STRENGTH] == 2
    assert game['rounds'][0]['cards'][util.PLAYER][util.MELEE][1][util.ACTUAL_STRENGTH] == 2
    assert game['rounds'][0]['cards'][util.COMPUTER][util.MELEE][0][util.ACTUAL_STRENGTH] == 1

    # player play Catapult
    game = gwent.play_card('5f6ed576-3791-4d54-82b4-dc06e302955d')
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][0][util.ACTUAL_STRENGTH] == 8

    # opponent play Keira Metz
    gwent.play_card('727481c1-cc45-480f-b171-3683bcfb7335')
    assert game['rounds'][0]['cards'][util.COMPUTER][util.RANGED][0][util.ACTUAL_STRENGTH] == 5

    # player play Kaedweni Siege Expert (boost)
    game = gwent.play_card('7894d713-bc7d-403e-aab5-868e5b12c685')
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][0][util.ACTUAL_STRENGTH] == 9

    # opponent play Crinfrid Reavers Dragon Hunter
    gwent.play_card('65311fe9-c124-4deb-b75c-fc5361135ee6')
    assert game['rounds'][0]['cards'][util.COMPUTER][util.RANGED][1][util.ACTUAL_STRENGTH] == 5

    # player play Catapult (bonded)
    game = gwent.play_card('f8402a3b-6f35-4600-852c-cb6af929bc19')
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][0][util.ACTUAL_STRENGTH] == 17
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][1][util.ACTUAL_STRENGTH] == 1
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][2][util.ACTUAL_STRENGTH] == 17

    # opponent play Crinfrid Reavers Dragon Hunter
    gwent.play_card('b89597a8-0fc4-45e5-9498-e5aa8fdd9c67')
    assert game['rounds'][0]['cards'][util.COMPUTER][util.RANGED][0][util.ACTUAL_STRENGTH] == 5
    assert game['rounds'][0]['cards'][util.COMPUTER][util.RANGED][1][util.ACTUAL_STRENGTH] == 10
    assert game['rounds'][0]['cards'][util.COMPUTER][util.RANGED][2][util.ACTUAL_STRENGTH] == 10

    # player play Kaedweni Siege Expert (boost)
    game = gwent.play_card('e4e229b0-16d7-41f2-a6b1-9b4746561e55')
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][0][util.ACTUAL_STRENGTH] == 18
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][1][util.ACTUAL_STRENGTH] == 2
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][2][util.ACTUAL_STRENGTH] == 18
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][3][util.ACTUAL_STRENGTH] == 2

    # opponent play Torrential Rain (weather)
    game = gwent.play_card('b6cfe466-e543-412c-9199-9060baa21e01')
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][0][util.ACTUAL_STRENGTH] == 4
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][1][util.ACTUAL_STRENGTH] == 2
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][2][util.ACTUAL_STRENGTH] == 4
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][3][util.ACTUAL_STRENGTH] == 2

    # test player scores
    assert game['rounds'][0]['scores']['rows'][util.PLAYER][util.MELEE] == 4
    assert game['rounds'][0]['scores']['cards'][util.PLAYER][util.SIEGE][0] == 4
    assert game['rounds'][0]['scores']['rows'][util.PLAYER][util.SIEGE] == 12
    assert game['rounds'][0]['scores']['totals'][util.PLAYER] == 16

    # test computer scores
    assert game['rounds'][0]['scores']['rows'][util.COMPUTER][util.RANGED] == 25
    assert game['rounds'][0]['scores']['cards'][util.COMPUTER][util.RANGED][0] == 5
    assert game['rounds'][0]['scores']['cards'][util.COMPUTER][util.RANGED][1] == 10

    # player play clear weather (weather)
    gwent.play_card('2dbee300-6ee9-49a9-b0e0-8207c9e14c76')
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][0][util.ACTUAL_STRENGTH] == 18
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][1][util.ACTUAL_STRENGTH] == 2
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][2][util.ACTUAL_STRENGTH] == 18
    assert game['rounds'][0]['cards'][util.PLAYER][util.SIEGE][3][util.ACTUAL_STRENGTH] == 2

    # test player scores
    assert game['rounds'][0]['scores']['rows'][util.PLAYER][util.MELEE] == 16
    assert game['rounds'][0]['scores']['cards'][util.PLAYER][util.SIEGE][0] == 18
    assert game['rounds'][0]['scores']['rows'][util.PLAYER][util.SIEGE] == 40
    assert game['rounds'][0]['scores']['totals'][util.PLAYER] == 56






