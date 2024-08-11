import numpy as np
import random
import os

class Game2048:
    def __init__(self, grid_size=4):
        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.score = 0
        self.game_over = False
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.grid[x][y] = random.choice([2, 4])
        else:
            self.game_over = True

    def move(self, direction):
        if not self.game_over:
            if direction == 'left':
                self.move_left()
            elif direction == 'right':
                self.move_right()
            elif direction == 'up':
                self.move_up()
            elif direction == 'down':
                self.move_down()
            else:
                print("Invalid direction! Use 'left', 'right', 'up', or 'down'.")
                return

            if not self.game_over:
                self.add_new_tile()
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
                self.display_grid()
                if self.check_game_over():
                    print("Game Over! No more moves left.")
                    self.game_over = True

    def move_left(self):
        new_grid = np.zeros_like(self.grid)
        for i in range(self.grid_size):
            merged_row = self.slide_and_merge(self.grid[i])
            new_grid[i, :] = merged_row
        self.grid = new_grid

    def move_right(self):
        new_grid = np.zeros_like(self.grid)
        for i in range(self.grid_size):
            reversed_row = self.grid[i][::-1]
            merged_row = self.slide_and_merge(reversed_row)
            new_grid[i, :] = merged_row[::-1]
        self.grid = new_grid

    def move_up(self):
        self.grid = self.grid.T  # Transpose the grid
        self.move_left()
        self.grid = self.grid.T  # Transpose back to original orientation

    def move_down(self):
        self.grid = self.grid.T  # Transpose the grid
        self.move_right()
        self.grid = self.grid.T  # Transpose back to original orientation

    def slide_and_merge(self, row):
        new_row = [tile for tile in row if tile != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
                self.score += new_row[i]
        new_row = [tile for tile in new_row if tile != 0] + [0] * (len(row) - len(new_row))
        return new_row

    def check_game_over(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 0:
                    return False
                if j < self.grid_size - 1 and self.grid[i][j] == self.grid[i][j + 1]:
                    return False
                if i < self.grid_size - 1 and self.grid[i][j] == self.grid[i + 1][j]:
                    return False
        return True

    def display_grid(self):
        print("Score:", self.score)
        for row in self.grid:
            print(" ".join("{:4}".format(tile) if tile != 0 else "    " for tile in row))
        print()

def main():
    game = Game2048()
    game.display_grid()

    directions = {'left': 'left', 'right': 'right', 'up': 'up', 'down': 'down'}

    while not game.game_over:
        move = input("Enter direction (left/right/up/down) or 'exit' to quit: ").lower()
        
        if move == 'exit':
            break
        
        if move in directions:
            game.move(move)
        else:
            print("Invalid direction! Use 'left', 'right', 'up', or 'down'.")
    
    print("Game Over! Your final score is:", game.score)

if __name__ == "__main__":
    main()
