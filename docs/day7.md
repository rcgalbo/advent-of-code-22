# Advent Of Code
# Day 7: No Space Left On Device

## Disclaimer: Solution is heavily borrowed from Joel Grus solution


Input:
```
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
```

Objective: find all direcotiries with a total size of at most 100000, then calculate the sum of their total sizes.