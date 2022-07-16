from src.day_1 import final_floor, basement_position


def test_final_floor():
    test_cases = [
        ('(())', 0),
        ('()()', 0),
        ('(((', 3),
        ('(()(()(', 3),
        ('))(((((', 3),
        ('())', -1),
        ('))(', -1),
        (')))', -3),
        (')())())', -3),
    ]

    for input, expected_output in test_cases:
        assert final_floor(input) == expected_output

def test_basement_position():
    test_cases = [
        (')', 1),
        ('()())', 5),
    ]

    for input, expected_output in test_cases:
        assert basement_position(input) == expected_output

