import tkinter as tk
import tkinter.messagebox as msgbox
import random
import numpy as np
import os


class Game2048GUI:
    def __init__(self, root, grid_size=4):
        self.root = root
        self.root.title("Game 2048")

        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.score = 0
        self.game_over = False
        self.high_score = 0

        self.setup_ui()

        self.add_new_tile()
        self.add_new_tile()

    def setup_ui(self):
        self.tiles = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                tile = tk.Label(self.root, text="", width=4, height=2, font=('Helvetica', 32, 'bold'), bd=5,
                                relief="raised")
                tile.grid(row=i, column=j, padx=5, pady=5)
                row.append(tile)
            self.tiles.append(row)

        self.score_label = tk.Label(self.root, text="Score: 0", font=('Helvetica', 24), fg="#444")
        self.score_label.grid(row=self.grid_size + 1, column=0, columnspan=self.grid_size, padx=10, pady=10, sticky="w")

        self.high_score_label = tk.Label(self.root, text=f"High Score: {self.high_score}", font=('Helvetica', 18),
                                         fg="#444")
        self.high_score_label.grid(row=self.grid_size + 2, column=0, columnspan=self.grid_size, padx=10, pady=5,
                                   sticky="w")

        self.author_label = tk.Label(self.root, text="Author: canerakcasu", font=('Helvetica', 14), fg="#444")
        self.author_label.grid(row=self.grid_size + 3, column=0, columnspan=self.grid_size, padx=10, pady=5, sticky="w")

    def update_ui(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                tile_value = self.grid[i][j]
                if tile_value == 0:
                    self.tiles[i][j].config(text="", bg="#cdc1b4", fg="#444")  # Empty cell color and text color
                else:
                    self.tiles[i][j].config(text=str(tile_value), bg=self.get_tile_color(tile_value),
                                            fg="#444")  # Tile color and text color
        self.score_label.config(text=f"Score: {self.score}")
        self.high_score_label.config(text=f"High Score: {self.high_score}")

    def get_tile_color(self, value):
        colors = {
            2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
            32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
            512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }
        return colors.get(value, "#ff0000")  # Default red for unexpected values

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.grid[x][y] = random.choice([2, 4])
            self.update_ui()
        else:
            self.game_over = True
            self.show_game_over_dialog()

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
                self.update_ui()
                if self.check_game_over():
                    self.game_over = True
                    self.show_game_over_dialog()

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
        self.grid = self.grid.T
        self.move_left()
        self.grid = self.grid.T

    def move_down(self):
        self.grid = self.grid.T
        self.move_right()
        self.grid = self.grid.T

    def slide_and_merge(self, row):
        new_row = [tile for tile in row if tile != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
                self.score += new_row[i]
                if self.score > self.high_score:
                    self.high_score = self.score
        new_row = [tile for tile in new_row if tile != 0] + [0] * (len(row) - len(new_row))
        new_row = new_row[:self.grid_size]
        new_row += [0] * (self.grid_size - len(new_row))
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

    def show_game_over_dialog(self):
        choice = msgbox.askquestion("Game Over",
                                    f"Game Over! Your final score is: {self.score}\n\nDo you want to play again?")
        if choice == 'yes':
            self.reset_game()
        else:
            self.root.destroy()

    def reset_game(self):
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        self.score = 0
        self.game_over = False
        self.add_new_tile()
        self.add_new_tile()
        self.update_ui()


def main():
    root = tk.Tk()
    game = Game2048GUI(root)

    def handle_key_event(event):
        key_mapping = {
            'a': 'left', 'd': 'right', 'w': 'up', 's': 'down',
            'Left': 'left', 'Right': 'right', 'Up': 'up', 'Down': 'down'
        }
        if event.keysym in key_mapping:
            game.move(key_mapping[event.keysym])
        else:
            print("Invalid key! Use arrow keys or 'WASD'.")

    root.bind("<Key>", handle_key_event)
    root.mainloop()


if __name__ == "__main__":
    main()
