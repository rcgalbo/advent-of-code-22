from adventOfCode22.day4 import parse_input_string
from adventOfCode22.day4 import parse_line
from adventOfCode22.day4 import contains_subset
from adventOfCode22.day4 import is_overlapping

test_dat = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def test_parse_line():
    assert parse_line("2-4,6-8") == ({2,3,4},{6,7,8})

def test_parse_input_string():
    assert parse_input_string(test_dat)[0] == ({2,3,4},{6,7,8})

def test_contains_subset():
    sections = parse_input_string(test_dat)
    assert contains_subset(sections[0]) == False

def test_is_overlapping():
    sections = parse_input_string(test_dat)
    assert is_overlapping(sections[2]) == True  