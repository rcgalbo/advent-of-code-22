from adventOfCode22.day5 import extract_stacks
from adventOfCode22.day5 import extract_instuctions
from adventOfCode22.day5 import parse_input_string
from adventOfCode22.day5 import crane, operate_crane
from adventOfCode22.day5 import operate_crane9001
from adventOfCode22.day5 import get_top_stacks

test_dat = '''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

test_stack_dat = '''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
'''
test_instruction_dat = '''
move 1 from 2 to 1
move 13 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

def test_extract_stacks():
    stacks = extract_stacks(test_stack_dat)
    assert stacks['1'] == ['Z','N']

def test_extract_instructions():
    instructions = extract_instuctions(test_instruction_dat)
    assert instructions == [[1,2,1],[13,1,3],[2,2,1],[1,1,2]]

def test_crane():
    stacks, instructions = parse_input_string(test_dat)
    updated_stacks = crane(stacks, instructions[0])
    assert updated_stacks['1'] == ['Z','N','D']

def test_get_top_stacks():
    stacks, instructions = parse_input_string(test_dat)
    updated_stacks = operate_crane(stacks, instructions)
    assert get_top_stacks(updated_stacks) == 'CMZ'

def test_get_top_stacks9001():
    stacks, instructions = parse_input_string(test_dat)
    updated_stacks = operate_crane9001(stacks, instructions)
    assert get_top_stacks(updated_stacks) == 'MCD'