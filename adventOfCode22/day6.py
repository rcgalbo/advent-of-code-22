def parse_char_str(input_str: str) -> list[str]:
    char_list = [c for c in input_str]
    return char_list

def is_unique_code(search_stack: list[str]) -> bool:
    if len(set(search_stack)) == 4:
        return True
    return False

def is_unique_message(search_stack: list[str]) -> bool:
    if len(set(search_stack)) == 14:
        return True
    return False

def find_marker(char_list: list[str]) -> int:
    for i in range(4,len(char_list)):
        search_stack = char_list[i-4:i]
        if is_unique_code(search_stack):
            return i
    return 0

def find_start_of_message(char_list: list[str]) -> int:
    for i in range(14,len(char_list)):
        search_stack = char_list[i-14:i]
        if is_unique_message(search_stack):
            return i
    return 0

if __name__ == '__main__':
    with open('data/day6.txt') as f:
        input_str = f.read()
    char_list = parse_char_str(input_str)
    # part 1 solution
    print(find_marker(char_list))
    # part 2 solution
    print(find_start_of_message(char_list))