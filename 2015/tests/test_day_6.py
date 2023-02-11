import sys
from pathlib import Path
sys.path.insert(0, str(Path('.\\2015').resolve()))

import pytest
from src.day_6 import Grid, GridController, BrightnessGrid

@pytest.fixture
def grid():
    return Grid()

@pytest.fixture
def brightness_grid():
    return BrightnessGrid()

@pytest.fixture
def grid_controller(grid):
    return GridController(grid)

@pytest.fixture
def brightness_grid_controller(brightness_grid):
    return GridController(brightness_grid)

def test_turn_on(grid):
    grid.turn_on(10, 10, 12, 12) # 9 lights are turned on
    grid.turn_on(10, 10, 11, 11) # Nothing extra is turned on
    grid.turn_on(12, 12, 13, 13) # 3 extra lights are turned on
    grid.turn_on(1, 1, 2, 2) # 4 extra are turned on

    assert grid.total_count() == 16

def test_toggle(grid):
    grid.toggle(10, 10, 12, 12) # 9 lights are turned on
    grid.toggle(10, 10, 11, 11) # 4 are turned off
    grid.toggle(12, 12, 13, 13) # 3 extra lights are turned on, 1 is turned off
    grid.toggle(1, 1, 2, 2) # 4 extra are turned on

    assert grid.total_count() == 11

def test_turn_off(grid):
    grid.turn_on(10, 10, 12, 12) # 9 lights are turned on
    grid.turn_off(10, 10, 11, 11) # 4 are turned off
    grid.turn_off(12, 12, 13, 13) # 1 is turned off
    grid.turn_off(1, 1, 2, 2) # Nothing happens

    assert grid.total_count() == 4

'''
    10  11  12  13  14
10           x
11           x
12   x   x       x   x
13           x   x   x
14           x   x   x
'''
def test_controller(grid_controller):
    assert grid_controller.total_count() == 0
    grid_controller.run_command('turn on 10,10 through 12,12')
    assert grid_controller.total_count() == 9
    grid_controller.run_command('turn off 10,10 through 11,11')
    assert grid_controller.total_count() == 5
    grid_controller.run_command('toggle 12,12 through 14,14')
    assert grid_controller.total_count() == 12


################################################
# Now let's do the same for our brightess grid #
################################################
def test_brightness_turn_on(brightness_grid):
    brightness_grid.turn_on(10, 10, 12, 12) # brightness + 9
    brightness_grid.turn_on(10, 10, 11, 11) # brightness + 4
    brightness_grid.turn_on(12, 12, 13, 13) # brightness + 4
    brightness_grid.turn_on(1, 1, 2, 2) # brightness + 4

    assert brightness_grid.total_count() == 21

def test_brightness_toggle(brightness_grid):
    brightness_grid.toggle(10, 10, 12, 12) # brightness + 18
    brightness_grid.toggle(10, 10, 11, 11) # brightness + 8
    brightness_grid.toggle(12, 12, 13, 13) # brightness + 8
    brightness_grid.toggle(1, 1, 2, 2) # brightness + 8

    assert brightness_grid.total_count() == 42

def test_brightness_turn_off(brightness_grid):
    brightness_grid.turn_on(10, 10, 12, 12) # brightness + 9
    brightness_grid.turn_on(10, 10, 12, 12) # brightness + 9
    brightness_grid.turn_off(10, 10, 11, 11) # brightness - 4
    brightness_grid.turn_off(10, 10, 11, 11) # brightness - 4
    brightness_grid.turn_off(10, 10, 11, 11) # nothing happens
    brightness_grid.turn_off(12, 12, 13, 13) # brightness -1
    brightness_grid.turn_off(1, 1, 2, 2) # Nothing happens

    assert brightness_grid.total_count() == 9

def test_brightness_controller(brightness_grid_controller):
    assert brightness_grid_controller.total_count() == 0
    brightness_grid_controller.run_command('turn on 10,10 through 12,12')
    assert brightness_grid_controller.total_count() == 9
    brightness_grid_controller.run_command('turn on 10,10 through 12,12')
    assert brightness_grid_controller.total_count() == 18
    brightness_grid_controller.run_command('turn off 10,10 through 11,11')
    assert brightness_grid_controller.total_count() == 14
    brightness_grid_controller.run_command('turn off 10,10 through 11,11')
    assert brightness_grid_controller.total_count() == 10
    brightness_grid_controller.run_command('turn off 10,10 through 11,11')
    assert brightness_grid_controller.total_count() == 10
    brightness_grid_controller.run_command('toggle 12,12 through 14,14')
    assert brightness_grid_controller.total_count() == 28