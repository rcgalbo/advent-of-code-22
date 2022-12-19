# Advent Of Code
## Day 6: Tuning Trouble

### Part 1: 

```
mjq|jpqm|gbljsphdztnvjfqwrcgsmlb
   |---_|
123|4567|89
   |---_|     
```
Sub routine should report 7 since that is the end position of the first 4 unique characters.

Here are a few more examples:
```
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11
```
Problem 1: Identify the position where the four most recently recieved characters were all different

Solution:
1. Parse string input into list of characters
2. Create `search_stack` starting with first 4 elements of character list
3. If `len(set(search_stack)) == 4` return position else search_stack.pop(0) and append next character
4. Repeat until position of unique 4 digit code has been identified
5. Return position

### Part 2:
```
mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
```

Problem 2: How many characters need to be processed before the first start-of-message marker is detected?

Solution:
1. Create `find_start_of_message` & `is_unique_message` functions to check if each individual 14 element seach stack is uinique
2. Return index of end of first unique stack as start of message