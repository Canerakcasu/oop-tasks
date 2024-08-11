Game2048

Game2048 is a Python implementation of the popular 2048 game. The goal of the game is to combine tiles with the same value to create a tile with the number 2048. The game ends when there are no more valid moves available.

Features

- Play the classic 2048 game in the terminal.
- Support for moving tiles in four directions: left, right, up, and down.
- Score tracking and display.
- Game over detection when no more moves are possible.

Installation

1. Make sure you have Python installed on your system. This code is compatible with Python 3.x.
2. Clone or download the repository to your local machine.
3. Navigate to the directory containing game2048.py.

Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where game2048.py is located.
3. Run the game with the following command:

    python game2048.py

4. Use the following commands to move the tiles:
    - left to move tiles left
    - right to move tiles right
    - up to move tiles up
    - down to move tiles down
5. Enter exit to quit the game.

How It Works

- Initialization: The game starts with a 4x4 grid filled with zeros. Two tiles (2 or 4) are added randomly to the grid.
- Movement: Tiles can be moved in four directions. Tiles of the same value combine when moved together, and the score is updated accordingly.
- Game Over: The game ends when there are no more empty cells and no adjacent tiles with the same value.

Code Overview

- Game2048 Class: Handles the game logic, including tile movement, merging, and game over conditions.
- add_new_tile() Method: Adds a new tile (2 or 4) to an empty cell.
- move() Method: Moves tiles in the specified direction and updates the grid.
- slide_and_merge() Method: Slides tiles to the edge and merges tiles with the same value.
- check_game_over() Method: Checks if there are no more valid moves.
- display_grid() Method: Displays the current state of the grid and the score.

Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or fixes.

License

This project is licensed under the MIT License. See the LICENSE file for details.
