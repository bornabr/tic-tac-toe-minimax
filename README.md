# Tic-Tac-Toe AI with Minimax Algorithm

## Algorithm
Minimax is a kind of backtracking algorithm used in decision-making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally.

In Minimax, the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible, while the minimizer attempts to do the opposite and get the lowest score possible.

Every board state has a value associated with it. In a given state, if the maximizer has the upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state, then it will tend to be some negative value. The values of the board are calculated by some heuristics, which are unique for every type of game.

In this game, the board's score is either 1, 0, or -1 if the winner of the board is the AI player, the game is a tie, or the human player, respectively. If the game is not finished, the board's score is calculated by the next state of the board in which the current player will choose based on his role (minimizer or maximizer) and the scores of all possible next states.

When it is the AI's turn to choose an action, it will call the `ai_action` method. This recursive function tries to find the best action based on scoring all the future states created based on available actions. It will calculate each state's score directly if the game of the current state is finished. However, if the game is unfinished, it will switch call itself to score each possible action, but it will switch the player and change role from maximizer to minimizer (so it assumes that the opponent will select its optimum option).


## Test
```bash
AI player?(X|O|N)
X
_______
| | | |
_______
| | | |
_______
| | | |
_______

AI player X moved!
_______
|X| | |
_______
| | | |
_______
| | | |
_______

Player O move:
1 1
_______
|X| | |
_______
| |O| |
_______
| | | |
_______

AI player X moved!
_______
|X|X| |
_______
| |O| |
_______
| | | |
_______

Player O move:
0 2
_______
|X|X|O|
_______
| |O| |
_______
| | | |
_______

AI player X moved!
_______
|X|X|O|
_______
| |O| |
_______
|X| | |
_______

Player O move:
1 0
_______
|X|X|O|
_______
|O|O| |
_______
|X| | |
_______

AI player X moved!
_______
|X|X|O|
_______
|O|O|X|
_______
|X| | |
_______

Player O move:
2 2
_______
|X|X|O|
_______
|O|O|X|
_______
|X| |O|
_______

AI player X moved!
_______
|X|X|O|
_______
|O|O|X|
_______
|X|X|O|
_______

Result: tie
```
```bash
AI player?(X|O|N)
O
_______
| | | |
_______
| | | |
_______
| | | |
_______

Player X move:
1 1
_______
| | | |
_______
| |X| |
_______
| | | |
_______

AI player O moved!
_______
|O| | |
_______
| |X| |
_______
| | | |
_______

Player X move:
2 0
_______
|O| | |
_______
| |X| |
_______
|X| | |
_______

AI player O moved!
_______
|O| |O|
_______
| |X| |
_______
|X| | |
_______

Player X move:
0 1
_______
|O|X|O|
_______
| |X| |
_______
|X| | |
_______

AI player O moved!
_______
|O|X|O|
_______
| |X| |
_______
|X|O| |
_______

Player X move:
1 0
_______
|O|X|O|
_______
|X|X| |
_______
|X|O| |
_______

AI player O moved!
_______
|O|X|O|
_______
|X|X|O|
_______
|X|O| |
_______

Player X move:
2 2
_______
|O|X|O|
_______
|X|X|O|
_______
|X|O|X|
_______

Result: tie
```