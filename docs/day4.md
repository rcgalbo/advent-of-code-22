# Advent Of Code
## Day 4: Camp Cleanup
```
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
```
Part 1: In how many assignment pairs does one range fully contain the other?

Solution:
1. Parse the string input into sets
2. Check if either set is a subset of the other
3. Loop over input counting subsets
4. Print out total number of subsets

Part 2: In how many assignment pairs do the ranges overlap?

Solution:
1. Replace `contains_subset` with `is_overlapping`