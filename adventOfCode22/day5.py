def parse_input_string(input_string: str) -> tuple[dict[str, list[int]], list[list[int]]]:
    stack_str, instruction_str = input_string.split('\n\n')
    stacks = extract_stacks(stack_str)
    instructions = extract_instuctions(instruction_str)
    return (stacks, instructions)

def extract_stacks(input_string: str) -> dict[str,int]:
    rows = input_string.split('\n')
    rows = [row for row in rows if row != '']
    stack_number_string = rows.pop()
    stack_number = stack_number_string.split(' ')
    stack_number = [stack_num for stack_num in stack_number if stack_num != '']
    stacks = {}
    # initialize stacks
    for stack_num in stack_number:
        stacks[stack_num] = []
    # extract stack elements from string and append to list
    for row in rows:
        iterable = list(range(1,len(row),4))
        for stack_num, i in zip(stack_number, iterable):
            if row[i] != ' ':
                stacks[stack_num].append(row[i])
    # properly order stacks
    for stack_num in stack_number:
        stacks[stack_num].reverse()
    return stacks

def extract_instuctions(instruction_str: str) -> list[list[int]]:
    instructions = instruction_str.split('\n')
    instructions = [instruction for instruction in instructions if instruction != '']

    numerical_instructions = []
    for instruction in instructions:
        numerical_instruction = []
        instruction_list = instruction.split(' ')
        for text in instruction_list:
            if text.isdigit():
                numerical_instruction.append(int(text))
        numerical_instructions.append(numerical_instruction)
    return numerical_instructions

def crane(stacks: dict[str, list[int]], instruction: list[int]) -> dict[str, list[int]]:
    num_crates, from_stack, to_stack = instruction
    from_stack, to_stack = str(from_stack), str(to_stack)
    # move crates
    for i in range(num_crates):
        stacks[to_stack].append(stacks[from_stack].pop())
    
    return stacks

def operate_crane(stacks: dict[str, list[int]], instructions: list[list[int]]):
    for instruction in instructions:
        stacks = crane(stacks, instruction)
    return stacks

def get_top_stacks(stacks: dict[str, list[int]]):
    stack_ids = stacks.keys()
    top_stacks = []
    for stack_id in stack_ids:
        top_stacks.append(stacks[stack_id].pop())
    return ''.join(top_stacks)

def operate_crane9001(stacks: dict[str, list[int]], instructions: list[list[int]]):
    for instruction in instructions:
        stacks = crane9001(stacks, instruction)
    return stacks

def crane9001(stacks: dict[str, list[int]], instruction: list[int]) -> dict[str, list[int]]:
    num_crates, from_stack, to_stack = instruction
    from_stack, to_stack = str(from_stack), str(to_stack)
    # move crates
    crates_to_move = stacks[from_stack][-num_crates:]
    # remove crates from old stack
    stacks[from_stack] = stacks[from_stack][:-num_crates]
    # stack crates on new stack
    stacks[to_stack] = stacks[to_stack] + crates_to_move
    
    return stacks

if __name__ == "__main__":
    with open('data/day5.txt') as f:
        input_string = f.read()
    stacks, instructions = parse_input_string(input_string)
    updated_stacks = operate_crane(stacks, instructions)
    # part 1 solution
    print(get_top_stacks(updated_stacks))
    
    stacks, instructions = parse_input_string(input_string)
    updated_stacks9001 = operate_crane9001(stacks, instructions)
    # part 2 solution
    print(get_top_stacks(updated_stacks9001))

