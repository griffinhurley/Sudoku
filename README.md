# Sudoku
This code creates and solves sudoku games.
## Usage
In terminal type: python3
Then play using the following commands. 

```python
from sudoku import Sudoku
# Initializes class
game=Sudoku() 
# Starts a new game and prints the board
game.start_game() 
# Places the value 3 in first row second column and prints updated board.
game.move(1,2,3) 
# Solves game and prints solution
game.solution() 
```
