from adventOfCode22.day3 import split_rucksacks
from adventOfCode22.day3 import compartementalize_rucksack
from adventOfCode22.day3 import find_shared_items
from adventOfCode22.day3 import make_priority_dictionary
from adventOfCode22.day3 import calculate_priority
from adventOfCode22.day3 import find_group_rank
from adventOfCode22.day3 import sum_groups_priority

test_dat = '''
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''
rucksacks = split_rucksacks(test_dat)

def test_compartemenalize_rucksack():
    compartments = compartementalize_rucksack(rucksacks[0])
    assert  compartments == ('vJrwpWtwJgWr','hcsFMMfFFhFp')

def test_find_shared_items():
    compartments = compartementalize_rucksack(rucksacks[0])
    shared_items = find_shared_items(compartments)
    assert shared_items == 'p'

def test_make_priority_dictionary():
    priority_dict = make_priority_dictionary()
    assert priority_dict['A'] == 27

def test_calculate_priority():
    assert calculate_priority(rucksacks) == 157

def test_find_group_rank():
    assert find_group_rank(rucksacks[0:3]) == 'r'

def test_sum_groups_priority():
    assert sum_groups_priority(rucksacks) == 70