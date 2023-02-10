
from src.file_utils import read_file

'''
Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. 
The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. 
Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. 
The lights all start turned off.
'''

class GridInterface:
    def turn_on(self, x1: int, y1: int, x2: int, y2: int) -> None:
        pass
    def turn_off(self, x1: int, y1: int, x2: int, y2: int) -> None:
        pass
    def toggle(self, x1: int, y1: int, x2: int, y2: int) -> None:
        pass
    def total_count(self) -> int:
        pass


class Grid(GridInterface):
    def __init__(self) -> None:
        self.lights_on = set[tuple]()

    def turn_on(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights_on.add((x, y))

    def turn_off(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights_on.discard((x, y))

    def toggle(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y) in self.lights_on:
                    self.lights_on.discard((x, y))
                else:
                    self.lights_on.add((x, y))

    def total_count(self):
        return len(self.lights_on)

class BrightnessGrid(GridInterface):
    def __init__(self) -> None:
        self.lights_on = dict[tuple, int]()

    def turn_on(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights_on[(x, y)] = self.lights_on.get((x, y), 0) + 1

    def turn_off(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights_on[(x, y)] = max(0, self.lights_on.get((x, y), 0) - 1)

    def toggle(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights_on[(x, y)] = self.lights_on.get((x, y), 0) + 2

    def total_count(self):
        sum = 0
        for b in self.lights_on.values():
            sum += b
        return sum

class GridController:
    def __init__(self, grid: GridInterface) -> None:
        self.grid = grid

    def total_count(self):
        return self.grid.total_count()

    def run_command(self, cmd: str):
        words = cmd.split(' ')
        if cmd.startswith("turn on"):
            x1, y1 = words[2].split(",")
            x2, y2 = words[4].split(",")
            self.grid.turn_on(int(x1), int(y1), int(x2), int(y2))
        elif cmd.startswith("turn off"):
            x1, y1 = words[2].split(",")
            x2, y2 = words[4].split(",")
            self.grid.turn_off(int(x1), int(y1), int(x2), int(y2))
        elif cmd.startswith("toggle"):
            x1, y1 = words[1].split(",")
            x2, y2 = words[3].split(",")
            self.grid.toggle(int(x1), int(y1), int(x2), int(y2))
            

if __name__ == "__main__":
    input = read_file('/../input/day_6.txt')
    lines = input.splitlines()
    grid = Grid()
    brightness_grid = BrightnessGrid()
    controller = GridController(grid)
    brightness_controller = GridController(brightness_grid)
    for line in lines:
        controller.run_command(line)
        brightness_controller.run_command(line)

    print(controller.total_count())
    print(brightness_controller.total_count())