

def parse_data(data_string: str) -> list[int]:
    # step 1
    elf_calorie_strings = data_string.split('\n\n')
    # step 2
    elf_calories_arrays = [calories.split('\n') for calories in elf_calorie_strings]
    # step 3
    elf_calories = []
    for calorie_array in elf_calories_arrays:
        new_elf_calories = []
        for calorie_count in calorie_array:
            if calorie_count != '':
                new_elf_calories.append(int(calorie_count))
        elf_calories.append(new_elf_calories)
    elf_calories = [sum(calorie_list) for calorie_list in elf_calories]
    return elf_calories


    

if __name__ == "__main__":
    with open('data/day1.txt') as dat:
        elf_string = dat.read()
        elf_calories = parse_data(elf_string)
        print(max(elf_calories)) # part 1 solution
        elf_calories.sort(reverse=True)
        print(sum(elf_calories[0:3])) # part 2 solution