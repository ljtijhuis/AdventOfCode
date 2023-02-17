import sys
from pathlib import Path
from typing import List
sys.path.insert(0, str(Path('.\\2015').resolve()))
print(sys.path)

import pytest
from src.day_9 import shortest_route, longest_route

'''
For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

'''

@pytest.mark.parametrize("input, shortest_length, longest_length", [
    (['London to Dublin = 464', 'London to Belfast = 518', 'Dublin to Belfast = 141'], 605, 982),
])
def test_shortest_route(input: List[str], shortest_length, longest_length: int):
    assert shortest_route(input) == shortest_length
    assert longest_route(input) == longest_length