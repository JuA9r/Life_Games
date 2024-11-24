"""
    Life Game program.run

This file contain running Life Game.
"""

import configparser
import sys

import numpy as np

import pygame as pg
from pygame.locals import *


class Generate_cells:
    def __init__(self, x_cell, y_cell):
        self.x_cell = x_cell
        self.y_cell = y_cell
        self.grid = np.random.randint(
            2, size=(self.x_cell, self.y_cell)
        )

    def update(self): ...

    def draw(self, screen): ...

class Life_Game_Display:
    def __init__(self, x_cell, y_cell, cell_size, fps):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Conway's Game of Life")
        self.clock = pg.time.Clock()

    def program_running(self):
        done = False
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True

        pg.quit()
        sys.exit()


def main():
    config = configparser.ConfigParser()
    config.read("config.ini") # Loading config file

    x_cell = int(config["GameSettings"]["x_cell"])
    y_cell = int(config["GameSettings"]["y_cell"])
    cell_size = int(config["GameSettings"]["cell_size"])
    fps = int(config["GameSettings"]["fps"])

    lgd = Life_Game_Display(x_cell, y_cell, cell_size, fps)
    lgd.program_running() # Run the program from the main method


if __name__ == "__main__":
    main()
