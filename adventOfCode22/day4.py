def parse_line(line: str) -> tuple[set[int],set[int]]:
    elf1, elf2 = line.split(',')
    elf1_start, elf1_end = (int(i) for i in elf1.split('-'))
    elf2_start, elf2_end = (int(i) for i in elf2.split('-'))
    return (set(range(elf1_start, elf1_end+1)), set(range(elf2_start, elf2_end+1)))

def parse_input_string(input_string: str) -> list[tuple[set[int],set[int]]]:
    lines = [line for line in input_string.split('\n') if line != '']
    sections = [parse_line(line) for line in lines]
    return sections

def contains_subset(sets: tuple[set[int], set[int]]) -> bool:
    elf1, elf2 = sets
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        return True
    return False

def is_overlapping(sets: tuple[set[int], set[int]]) -> bool:
    elf1, elf2 = sets
    if elf1.intersection(elf2) != set():
        return True
    return False

if __name__ == "__main__":
    with open('data/day4.txt') as f:
        input_string = f.read()
    sections = parse_input_string(input_string)
    # part 1
    print(sum(contains_subset(section) for section in sections))
    # part 2
    print(sum(is_overlapping(section) for section in sections))