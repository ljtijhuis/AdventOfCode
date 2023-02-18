import sys
from pathlib import Path
from typing import List
sys.path.insert(0, str(Path('.\\2015').resolve()))
print(sys.path)

import pytest
from src.day_10 import look_and_say

'''
1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
'''

@pytest.mark.parametrize("input, output", [
    ('1', '11'),
    ('11', '21'),
    ('21', '1211'),
    ('1211', '111221'),
    ('111221', '312211'),
])
def test_look_and_say(input: str, output: str):
    assert look_and_say(input) == output