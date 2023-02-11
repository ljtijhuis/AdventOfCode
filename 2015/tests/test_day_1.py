import sys
from pathlib import Path
sys.path.insert(0, str(Path('.\\2015').resolve()))

import pytest
from src.day_1 import final_floor, basement_position

@pytest.mark.parametrize("input, expected_output", [ 
    ('(())', 0),
    ('()()', 0),
    ('(((', 3),
    ('(()(()(', 3),
    ('))(((((', 3),
    ('())', -1),
    ('))(', -1),
    (')))', -3),
    (')())())', -3),
])
def test_final_floor(input, expected_output):
    assert final_floor(input) == expected_output

@pytest.mark.parametrize("input, expected_output", [ 
    (')', 1),
    ('()())', 5),
])
def test_basement_position(input, expected_output):
    assert basement_position(input) == expected_output

