# Advent Of Code
## Day 5: Supply Stacks

### Part 1:
```
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
```

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:
```
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
```
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:
```
        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
```
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:
```
        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
```
Finally, one crate is moved from stack 1 to stack 2:
```
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
```
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

Problem 1: After the rearrangement procedure completes, what crate ends up on top of each stack?

Solution:

1. Parse data into stacks and directions
    - Use legitimate stacks for each stack
    - parse instrutions into 3 integer lsit of `[#_of_crates, from_stack, to_stack]`
2. Write crane function to make crates moves from instructions
3. Loop over instructions making all crate moves
4. Return letter code of crate characters at top of each stack

### Part 2:

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:
```
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
```
Moving a single crate from stack 2 to stack 1 behaves the same as before:
```
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
```
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:
```
        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
```
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:
```
        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
```
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:
```
        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
```
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.


Part 2: Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

Solution:
1. Write new function `crane9001` to remove items from stack in order and place on top of new stack

Notes: The stack variable was mutated somewhere in the code and had to have the data reparsed. Would not deploy this code to prod even thought I got the right answer. TODO(rcgalbo): figure out source of mutation.