import configparser
import sys
import numpy as np
import pygame as pg


class Cells:
    def __init__(self, x_cell, y_cell) -> None:
        self.x_cell = x_cell
        self.y_cell = y_cell
        self.grid = np.random.randint(2, size=(self.y_cell, self.x_cell))

    def draw_grid(self, screen, cell_size) -> None:
        """Draw the grid in the window."""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                color = (0, 255, 0) if cell == 1 else (255, 0, 255)  # Green for live, magenta for dead
                pg.draw.rect(
                    screen, color,
                    (x * cell_size, y * cell_size, cell_size, cell_size)
                )
                pg.draw.rect(
                    screen, (100, 100, 100),  # Border color
                    (x * cell_size, y * cell_size, cell_size, cell_size), 1
                )

    def __update__(self) -> None:
        new_grid = np.copy(self.grid)
        for y in range(self.y_cell):
            for x in range(self.x_cell):
                neighbors = np.sum(
                    self.grid[max(0, y-1):min(self.y_cell, y+2),
                              max(0, x-1):min(self.x_cell, x+2)]
                ) - self.grid[y, x]

                if self.grid[y, x] == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[y, x] = 0
                elif self.grid[y, x] == 0 and neighbors == 3:
                    new_grid[y, x] = 1

        self.grid = new_grid


class Life_Game_Display:
    def __init__(self, x_cell, y_cell, cell_size, fps) -> None:
        pg.init()
        self.x_cell = x_cell
        self.y_cell = y_cell
        self.cell_size = cell_size
        self.fps = fps

        self.screen = pg.display.set_mode((self.x_cell * self.cell_size, self.y_cell * self.cell_size))
        pg.display.set_caption("Conway's Game of Life")
        self.clock = pg.time.Clock()
        self.life_game = Cells(x_cell, y_cell)

    def program_running(self) -> None:
        done = False
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True

            self.screen.fill((0, 0, 0))  # Clear screen
            self.life_game.__update__()
            self.life_game.draw_grid(self.screen, self.cell_size)
            pg.display.flip()
            self.clock.tick(self.fps)

        pg.quit()
        sys.exit()


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    x_cell = int(config["GameSettings"]["x_cell"])
    y_cell = int(config["GameSettings"]["y_cell"])
    cell_size = int(config["GameSettings"]["cell_size"])
    fps = int(config["GameSettings"]["fps"])

    lgd = Life_Game_Display(x_cell, y_cell, cell_size, fps)
    lgd.program_running()


if __name__ == "__main__":
    main()