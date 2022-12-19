#!/bin/bash

add_day () {
    touch "adventOfCode22/$1.py"
    touch "adventOfCode22/data/$1.txt"
    touch "docs/$1.md"
    touch "tests/test_$1.py"
}

add_day $1