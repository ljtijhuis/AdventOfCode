
from src.file_utils import read_file

'''
It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
'''
def has_n_vowels(s, n = 3):
    found = 0
    for c in s:
        if c in 'aeiou':
            found += 1
        if found == n:
            return True
    return False

'''
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
'''
def has_twice_in_row(s):
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return True
    return False

'''
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
'''
def no_forbidden_strings(s):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for f in forbidden:
        if f in s:
            return False
    return True

def is_nice(s):
    return has_n_vowels(s) and has_twice_in_row(s) and no_forbidden_strings(s)

'''
It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
'''
def has_pair(s):
    pairs = {}
    for i in range(0, len(s)-1):
        pair = s[i:i+2]
        if pair not in pairs:
            pairs.update({pair: [i]})
        else:
            pairs[pair].append(i)
    
    for pair, indeces in pairs.items():
        # just compare the first and last index they occur as they should be furthest apart
        if len(indeces) > 1 and indeces[len(indeces)-1] - indeces[0] > 1:
            return True
    return False

'''
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
'''
def has_repeat(s):
    for i in range(2, len(s)):
        if s[i] == s[i-2]:
            return True
    return False

def new_is_nice(s):
    return has_pair(s) and has_repeat(s)

if __name__ == "__main__":
    input = read_file('/../input/day_5.txt')
    lines = input.split()

    total_nice = 0
    total_new_nice = 0
    for line in lines:
        total_nice += is_nice(line)
        total_new_nice += new_is_nice(line)

    print(total_nice)
    print(total_new_nice)
