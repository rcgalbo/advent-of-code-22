# Advent Of Code 
## Day 2: Rock Paper Scissors

Encrypted strategy guide.

Example data:

```
A Y
B X
C Z
```

The first column key (opponent column)
A: Rock
B: Paper
C: Scissors

Second column key (player column)
X: Rock
Y: Paper
Z: Scissors

Scoring rules:
1 for A, X
2 for B, Y
3 for C, Z

(0 if loss, 3 if drawm, 6 if won)

This eaxample data strategyu guide predicts and recommends the following:

- In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
- In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
- The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

### Part 1: What would your total score be if everything goes exactly according to your strategy guide?

Solution:

1. Split lines of test data into array of lists of len 2. Each list containting `['opponent', 'player']` 
2. Find the game state meanin if player won, lost, or tied
3. Score an individual throw meaning one row of data
4. Iterate through the data taking the sum of each row score

### Part 2: 

A: X: Rock
B: Y: Paper
C: Z: Scissors

X: Loose
Y: Draw
Z: Win

Now X means loose, Y means draw, Z means win. Need to find the right combination of rock, paper, and scissors to make make the instruction of loose, draw, win be true.

Find the total score if everything has to follow the strategy guide.

Solution:

1. Split string into list of lists each containing opponent throw and instruction to win or loose
2. Create a function to find the right move that was specified in the instrucions
3. Convert instructions into game throws and score using previous scoring function