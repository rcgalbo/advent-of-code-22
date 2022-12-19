from adventOfCode22.day6 import parse_char_str
from adventOfCode22.day6 import is_unique_code
from adventOfCode22.day6 import find_marker
from adventOfCode22.day6 import find_start_of_message

test_dat = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

test_dat_robust = [
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
]

def test_parse_char_str():
    char_list = parse_char_str(test_dat)
    assert char_list[0:4] == ['m','j','q','j']

char_list = parse_char_str(test_dat)

def test_is_unique_code():
    assert is_unique_code(char_list[0:4]) == False

def test_find_marker():
    assert find_marker(char_list) == 7

def test_find_markers():
    signals = [parse_char_str(signal) for signal in test_dat_robust]
    markers = [find_marker(signal) for signal in signals]
    assert markers == [5,6,10,11] 

def test_find_start_of_message():
    signals = [parse_char_str(signal) for signal in test_dat_robust]
    markers = [find_start_of_message(signal) for signal in signals]
    assert markers == [23,23,29,26]