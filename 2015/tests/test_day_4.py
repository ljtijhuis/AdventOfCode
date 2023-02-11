import sys
from pathlib import Path
sys.path.insert(0, str(Path('.\\2015').resolve()))

import pytest
from src.day_4 import find_first_hash

'''
If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
'''

@pytest.mark.parametrize("input, expected_output", [ 
    ('abcdef', 609043),
    ('pqrstuv', 1048970),
])
def test_find_first_hash(input, expected_output):
    assert find_first_hash(input) == expected_output

