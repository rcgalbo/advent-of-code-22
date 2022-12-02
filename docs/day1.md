# Advent Of Code 
## Day 1: Calorie Counting

Each elf is carring caloric food. Each line item is a food calorie count that they are carrying and each elf id demarcated by a new line.
 
Below is some sample data sample data:
```
ex_dat = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''
```
We can also think of this example data as:

```
ex_dat = '1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n'
```

For example we can view this text as 
 
 | Elf | Item Calories | Total Calories |
 | --- | ------------- | -------------- |
 | Elf 1 | 1000+2000+3000 | 6000 |
 | Elf 2 | 4000           | 4000 |
 | Elf 3 | 5000+6000      | 11000 |
 | Elf 4 | 7000+8000+9000 | 24000 |
 | Elf 5 | 1000           | 1000 |

### Part 1: Report the maximum amount of calories carried by an elf

Solution:

1. Split data string on '\n\n' which gives us a list of strings, one for each elf.
2. Loop over this array of strings splitting each string on '\n' so that there is an array of arrays of strings.
3. Loop over each of the sub arrays of strings, converting each string to a numeric type.
4. Sum each array of numbers
5. Return max value