import sys
from pathlib import Path
sys.path.insert(0, str(Path('.\\2015').resolve()))
print(sys.path)

import pytest
from src.day_7 import CircuitBoard

'''
Testing on command line:
>>> x = 123
>>> y = 456
>>> d = x & y
>>> e = x | y
>>> f = x << 2
>>> g = y >> 2
>>> h = ~x (this goes wrong because we are not taking into account we are only working with 16 bits)
>>> i = ~y (idem)
>>> d
72
>>> e
507
>>> f
492
>>> g
114
>>> h
-124
>>> i
-457
>>> x
123
>>> y
456
>>> 65535 - (124 -1) (this is the right way of obtaining the 16 bit NOT result)
65412
>>> 65535 - (457 -1)
65079
'''

@pytest.fixture
def circuit_board():
    return CircuitBoard()

'''
For example, here is a simple circuit:
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
'''
@pytest.mark.parametrize("operations, expected_output_values", [ 
    (
        [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i",
        ],
        {
            "d": 72,
            "e": 507,
            "f": 492,
            "g": 114,
            "h": 65412,
            "i": 65079,
            "x": 123,
            "y": 456,
        }
    ),
    (
        [
            "123 -> aa",
            "456 -> bb",
            "aa AND bb -> dd",
        ],
        {
            "dd": 72,
            "aa": 123,
            "bb": 456,
        }
    ),
])
def test_circuit(circuit_board: CircuitBoard, operations: list[str], expected_output_values: dict[str, int]):
    for op in operations:
        circuit_board.add_operation(op)

    for key, value in expected_output_values.items():
        assert circuit_board.get_value(key) == value