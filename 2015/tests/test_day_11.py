import sys
from pathlib import Path
from typing import List
sys.path.insert(0, str(Path('.\\2015').resolve()))
print(sys.path)

import pytest
from src.day_11 import has_increasing_straight, has_no_forbidden_letters, has_two_pairs, increment_one, next_password


'''
hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
'''
@pytest.mark.parametrize("input, pass_first, pass_second, pass_third", [
    ('hijklmmn', True, False, False),
    ('abbceffg', False, True, True),
    ('abbcegjk', False, True, False),
])
def test_password_rules(input: str, pass_first: bool, pass_second: bool, pass_third: bool):
    assert has_increasing_straight(input) == pass_first and has_no_forbidden_letters(input) == pass_second and has_two_pairs(input) == pass_third

@pytest.mark.parametrize("input, output", [
    ('aaaaaaaa', 'aaaaaaab'),
    ('aaaaaaaz', 'aaaaaaba'),
    ('aaaaaazz', 'aaaaabaa'),
    ('zaaaaazz', 'zaaaabaa'),
    ('zzzzzzzz', 'aaaaaaaa'),
])
def test_increment_one(input: str, output: str):
    assert increment_one(input) == output

'''
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
'''

@pytest.mark.parametrize("input, output", [
    ('abcdefgh', 'abcdffaa'),
    ('ghijklmn', 'ghjaabcc'),
])
def test_next_password(input: str, output: str):
    gen = next_password(input)
    assert next(gen) == output