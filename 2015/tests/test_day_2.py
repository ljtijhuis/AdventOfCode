import pytest
from src.day_2 import paper_needed, ribbon_needed

'''
A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
'''

@pytest.mark.parametrize("input, expected_output", [ 
    ('2x3x4', 58),
    ('1x1x10', 43),
])
def test_paper_needed(input, expected_output):
    assert paper_needed(input) == expected_output


'''
A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
'''
@pytest.mark.parametrize("input, expected_output", [ 
    ('2x3x4', 34),
    ('1x1x10', 14),
])
def test_ribbon_needed(input, expected_output):
    assert ribbon_needed(input) == expected_output