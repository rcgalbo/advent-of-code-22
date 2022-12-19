# Advent Of Code
## Day 3: Rucksack Reorganization

Have rucksacks filled with items
```
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```
Each line is a rucksack. Each rucksack is split into two compartments each containing the same amount of items. 

So vJrwpWtwJgWr|hcsFMMfFFhFp is the two compartments of the first string.

The only character that appears in both appartments is p.

Each item has a priority:
- Lowercase item types a through z have priorities 1 through 26.
- Uppercase item types A through Z have priorities 27 through 52.

The example above priority is 16(p), 38(L), 42(P), 22(v), 20(t), 19(s) = 157

Part 1: What is the sum of the priorities of those item types?

Solution:
1. Break string up into compartments
2. Find items shared across both compartments
3. Sum up priority of shared items

Part 2: Misplaced badges

Each group of 3 elves needs to find thier common item which represents their badge.

Find and sum priorities of badges.

Solution:
1. Split strings into list on new line
2. Find common rank element in each group of three strings
3. Find priority of each group rank
4. Sum rank priorities

