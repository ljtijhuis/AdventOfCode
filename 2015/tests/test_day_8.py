import sys
from pathlib import Path
sys.path.insert(0, str(Path('.\\2015').resolve()))
print(sys.path)

import pytest
from src.day_8 import character_count, encoded_character_count

'''
For example:

"" is 2 characters of code (the two double quotes), but the string contains zero characters.
"abc" is 5 characters of code, but 3 characters in the string data.
"aaa\\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
"\\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \\" (which represents a lone double-quote character), and \\x plus two hexadecimal characters (which represents a single character with that ASCII code).

Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
'''

@pytest.mark.parametrize("input, code_length, characters", [
    ('""', 2, 0),
    ('"abc"', 5, 3),
    ('"aaa\\"aaa"', 10, 7),
    ('"\\x27"', 6, 1),
])
def test_character_count(input: str, code_length: int, characters: int):
    assert len(input) == code_length and character_count(input) == characters


'''
"" encodes to "\\"\\"", an increase from 2 characters to 6.
"abc" encodes to "\\"abc\\"", an increase from 5 characters to 9.
"aaa\"aaa" encodes to "\\"aaa\\\\\\"aaa\\"", an increase from 10 characters to 16.
"\\x27" encodes to "\\"\\\\x27\\"", an increase from 6 characters to 11.
'''
@pytest.mark.parametrize("input, code_length, characters", [
    ('""', 2, 6),
    ('"abc"', 5, 9),
    ('"aaa\\"aaa"', 10, 16),
    ('"\\x27"', 6, 11),
])
def test_encoded_character_count(input: str, code_length: int, characters: int):
    assert len(input) == code_length and encoded_character_count(input) == characters