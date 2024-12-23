# **Conway's Game of Life**

- This project implements Conway's Game of Life using Python and Pygame. 
- Conway's Game of Life is a cellular automaton devised by mathematician John Conway.
- It simulates the evolution of a grid of cells based on simple rules.

## **Execution Environment**
- **Python**: 3.13 
- **pygame**: 2.6.1
- **numpy**:  2.1.3

---

## Table of Contents
- [How to Run](#how-to-run)
- [Features](#features)
- [Configuration](#configuration)
- [How to Play](#how-to-play)
- [Dependencies](#dependencies)
- [License](#license)

## How to Run
1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip:
   ```bash
   pip install pygame numpy
   ```
3. Configure the game settings in the `config.ini` file (see [Configuration](#configuration)).
4. Run the program:
   ```bash
   python run.py
   ```

## Features
- **Interactive Grid**: Toggle cells on or off by clicking or dragging the mouse.
- **Pause and Resume**: Press the `SPACE` key to pause or resume the simulation.
- **Dynamic Updates**: The grid updates in real-time following Conway's rules when unpaused.

## Configuration
The game settings are defined in a `config.ini` file. Here is an example of the configuration:

```ini
[GameSettings]
x_cell = 50       # Number of cells in the x-direction
y_cell = 50       # Number of cells in the y-direction
cell_size = 10    # Pixel size of each cell
fps = 10          # Frames per second for simulation
```

### Parameters
- **x_cell**: Number of cells along the horizontal axis.
- **y_cell**: Number of cells along the vertical axis.
- **cell_size**: Size of each cell in pixels.
- **fps**: Speed of the simulation in frames per second.

## How to Play
1. **Start**: Launch the game and see an empty grid.
2. **Add Cells**: Left-click or drag the mouse to activate cells in the grid.
3. **Pause/Resume**: Press the `SPACE` key to toggle between paused and running states.
4. **Watch the Evolution**: Observe how the cells evolve according to the rules of Conway's Game of Life.

### Conway's Rules
1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Dependencies
- Python 3.x
- Pygame
- NumPy 

Install dependencies with:
```bash
pip install pygame numpy
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
