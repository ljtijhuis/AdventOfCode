import sys
from pathlib import Path
sys.path.insert(0, str(Path('.\\2015').resolve()))

import pytest
from src.day_5 import has_n_vowels, has_twice_in_row, no_forbidden_strings, is_nice, has_pair, has_repeat, new_is_nice

'''
A nice string is one with all of the following properties:
It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
'''
@pytest.mark.parametrize("input, expected_output", [ 
    ('aei', True),
    ('xazegov', True),
    ('aeiouaeiouaeiou', True),
    ('ai', False),
    ('xazegv', False),
    ('mnlklpz', False),
])
def test_has_n_vowels(input, expected_output):
    assert has_n_vowels(input) == expected_output

'''
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
'''
@pytest.mark.parametrize("input, expected_output", [ 
    ('xx', True),
    ('abcdde', True),
    ('aabbccdd', True),
    ('x', False),
    ('abcde', False),
])
def test_has_twice_in_row(input, expected_output):
    assert has_twice_in_row(input) == expected_output

'''
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
'''
@pytest.mark.parametrize("input, expected_output", [ 
    ('ab', False),
    ('cd', False),
    ('pq', False),
    ('xy', False),
    ('axb', True),
    ('cxd', True),
    ('pxq', True),
    ('xay', True),
])
def test_no_forbidden_strings(input, expected_output):
    assert no_forbidden_strings(input) == expected_output

'''
For example:
ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
'''
@pytest.mark.parametrize("input, expected_output", [ 
    ('ugknbfddgicrmopn', True),
    ('aaa', True),
    ('jchzalrnumimnmhp', False),
    ('haegwjzuvuyypxyu', False),
    ('dvszwmarrgswjxmb', False),
])
def test_is_nice(input, expected_output):
    assert is_nice(input) == expected_output

'''
It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
'''
@pytest.mark.parametrize("input, expected_output", [ 
    ('xyxy', True),
    ('aabcdefgaa', True),
    ('aaa', False),
    ('aaaa', True),
])
def test_has_pair(input, expected_output):
    assert has_pair(input) == expected_output

'''
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
'''
@pytest.mark.parametrize("input, expected_output", [ 
    ('xyx', True),
    ('abcdefeghi', True),
    ('aaa', True),
])
def test_has_repeat(input, expected_output):
    assert has_repeat(input) == expected_output

'''
qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
'''
@pytest.mark.parametrize("input, expected_output", [ 
    ('qjhvhtzxzqqjkmpb', True),
    ('xxyxx', True),
    ('uurcxstgmygtbstg', False),
    ('ieodomkazucvgmuy', False),
])
def test_new_is_nice(input, expected_output):
    assert new_is_nice(input) == expected_output