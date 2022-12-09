import string

def split_rucksacks(rucksacks: str) -> list[str]:
    split_rucksacks = rucksacks.split('\n')
    return [rucksack for rucksack in split_rucksacks if rucksack != '']

def compartementalize_rucksack(rucksack: str) -> tuple[str, str]:
    split_location = len(rucksack) // 2
    compartment1, compartment2 = rucksack[0:split_location], rucksack[split_location:]
    return (compartment1, compartment2)

def find_shared_items(compartments: tuple[str, str]) -> str:
    compartment1, compartment2 = compartments
    set1, set2 = set(compartment1), set(compartment2)
    shared = set1.intersection(set2)
    return list(shared)[0]

def make_priority_dictionary() -> dict[str, int]:
    letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    priority_dict = {}
    for i, letter in enumerate(letters):
        priority_dict[letter] = i+1
    return priority_dict

def calculate_priority(rucksacks: list[str]) -> int:
    priorities = []
    priority_dict = make_priority_dictionary()
    for rucksack in rucksacks:
        compartments = compartementalize_rucksack(rucksack)
        shared_items = find_shared_items(compartments)
        priorities.append(priority_dict[shared_items])
        

    return sum(priorities)

def find_group_rank(rucksacks: list[str]) -> str:
    rucksack_sets = [set(rucksack) for rucksack in rucksacks]
    sack1, sack2, sack3 = rucksack_sets
    rank = sack1.intersection(sack2).intersection(sack3)
    return list(rank)[0]

def sum_groups_priority(rucksacks: list[str]) -> int:
    priorities = []
    priority_dict = make_priority_dictionary()
    for i in range(0, len(rucksacks), 3):
        rank = find_group_rank(rucksacks[i:i+3])
        priority = priority_dict[rank]
        priorities.append(priority)
    return sum(priorities)

if __name__ == '__main__':
    with open('data/day3.txt') as f:
        rucksacks = split_rucksacks(f.read())
    print(calculate_priority(rucksacks))
    print(sum_groups_priority(rucksacks))