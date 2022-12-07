from adventOfCode22.day2 import split_lines
from adventOfCode22.day2 import find_game_state
from adventOfCode22.day2 import score_throw
from adventOfCode22.day2 import score_game
from adventOfCode22.day2 import find_right_move
from adventOfCode22.day2 import score_game_part2

test_dat = '''
A Y
B X
C Z
'''

def test_split_lines():
    assert split_lines(test_dat) == [['A','Y'], ['B','X'], ['C','Z']]

def test_find_game_state():
    throws = split_lines(test_dat)
    opp, player = throws[0]
    assert find_game_state(opp, player) == 'Win'

def test_score_throw():
    throws = split_lines(test_dat)
    first_throw = throws[0]
    assert score_throw(first_throw) == 8

def test_score_game():
    throws = split_lines(test_dat)
    assert score_game(throws) == 15

def test_find_game_dict():
    throws = split_lines(test_dat)
    opp, decision = throws[2]
    assert find_right_move(opp, decision) == 'X'

def test_score_game_part2():
    throws = split_lines(test_dat)
    assert score_game_part2(throws) == 12
