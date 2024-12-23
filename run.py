"""
    Conway's Game of Life.run

This file contains running Conway's Game of Life.
"""

import configparser
import numpy as np
import pygame as pg
from pygame.locals import *
import sys


class Cells:
    def __init__(self, x_cell, y_cell) -> None:
        self.x_cell = x_cell
        self.y_cell = y_cell
        self.grid = np.zeros((self.y_cell, self.x_cell), dtype=int)

    def draw_grid(self, screen, cell_size) -> None:
        """Draw the grid in the window"""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                color = (0, 255, 0) if cell == 1 else (0, 0, 0)
                pg.draw.rect(
                    screen,
                    color,
                    (x * cell_size, y * cell_size, cell_size, cell_size)
                )

                pg.draw.rect(
                    screen,
                    (50, 50, 50),
                    (x * cell_size, y * cell_size, cell_size, cell_size), 1
                )

    def toggle_cell(self, x, y) -> None:
        self.grid[y, x] = 1 if self.grid[y, x] == 0 else 0

    def update(self) -> None:
        new_grid = np.copy(self.grid)
        for y in range(self.y_cell):
            for x in range(self.x_cell):
                neighbors = np.sum(
                    self.grid[
                        max(0, y-1):min(self.y_cell, y+2),
                        max(0, x-1):min(self.x_cell, x+2)
                    ]
                ) - self.grid[y, x]

                if self.grid[y, x] == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[y, x] = 0
                elif self.grid[y, x] == 0 and neighbors == 3:
                    new_grid[y, x] = 1

        self.grid = new_grid


class LifeGameDisplay:
    def __init__(self, x_cell, y_cell, cell_size, fps) -> None:
        pg.init()
        self.x_cell = x_cell
        self.y_cell = y_cell
        self.cell_size = cell_size
        self.fps = fps

        self.screen = pg.display.set_mode(
            (self.x_cell * self.cell_size, self.y_cell * self.cell_size)
        )
        pg.display.set_caption("Conway's Game of Life")
        self.clock = pg.time.Clock()
        self.life_game = Cells(x_cell, y_cell)

    def running(self) -> None:
        """main loop"""
        _running = True
        paused = True

        while _running:
            mouse_pressed = pg.mouse.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    _running = False

                if (event.type == pg.MOUSEBUTTONDOWN and event.button == 1) or \
                   (event.type == pg.MOUSEMOTION and mouse_pressed[0]):
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    cell_x = mouse_x // self.cell_size
                    cell_y = mouse_y // self.cell_size
                    if 0 <= cell_x < self.x_cell and 0 <= cell_y < self.y_cell:
                        self.life_game.toggle_cell(cell_x, cell_y)
                        print(
                            f"\ncoordinate={mouse_x, mouse_y} \
                            \ncell={cell_x, cell_y}"
                        )

                    if event.type == pg.MOUSEMOTION:
                        pass
                        # print(mouse_x, mouse_y)

                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    paused = not paused

            self.screen.fill((0, 0, 0))

            if not paused:
                self.life_game.update()

            self.life_game.draw_grid(self.screen, self.cell_size)
            pg.display.flip()
            self.clock.tick(self.fps)

        pg.quit()
        if sys.exit:
            print(f"\n{"-"*20}\nEnd of Program")


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    x_cell = int(config["GameSettings"]["x_cell"])
    y_cell = int(config["GameSettings"]["y_cell"])
    cell_size = int(config["GameSettings"]["cell_size"])
    fps = int(config["GameSettings"]["fps"])

    game_display = LifeGameDisplay(x_cell, y_cell, cell_size, fps)
    game_display.running()


if __name__ == "__main__":
    main()