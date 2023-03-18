
'''
Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
'''
def has_increasing_straight(s: str) -> bool:
    straight_len = 1
    for i in range(1, len(s)):
        if ord(s[i-1]) + 1 == ord(s[i]):
            straight_len += 1
            if straight_len > 2:
                return True
        else:
            straight_len = 1
    return False

'''
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
'''
def has_no_forbidden_letters(s: str) -> bool:
    for c in s:
        if c == 'i' or c == 'o' or c == 'l':
            return False
    return True

'''
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
'''
def has_two_pairs(s: str) -> bool:
    pairs = 0
    i = 1
    while i < len(s):
        if s[i-1] == s[i]:
            pairs += 1
            i += 1
            if pairs > 1:
                return True
        i += 1
    return False

def increment_one(s: str) -> str:
    carry = 1
    i = len(s)-1
    while i >= 0 and carry > 0:
        carry = 0
        next_char_num = ord(s[i]) + 1
        if next_char_num > ord('z'):
            next_char_num = ord('a')
            carry = 1
        s = s[:i] + chr(next_char_num) + s[i+1:]
        i -= 1
    if carry > 0:
        return 'aaaaaaaa'
    return s
        

def next_with_increasing_straight(s: str) -> str:
    while True:
        # TODO I could probably find the next straight quicker, but this is fast enough
        s = increment_one(s)
        while not has_increasing_straight(s):
            s = increment_one(s)
        yield s

def next_no_forbidden_letters(s: str) -> str:
    while True:
        # TODO Same here, I could just update the leftmost forbidden letter to the next one with a's on the right of it
        s = increment_one(s)
        while not has_no_forbidden_letters(s):
            s = increment_one(s)
        yield s

def next_with_two_pairs(s: str) -> str:
    while True:
        # TODO And another optimization could be to just introduce the next pair from right to left
        s = increment_one(s)
        while not has_two_pairs(s):
            s = increment_one(s)
        yield s

def next_password(s: str) -> str:
    inc_straight_gen = next_with_increasing_straight(s)
    two_pairs_gen = next_with_two_pairs(s)
    forbidden_gen = next_no_forbidden_letters(s)
    while True:
        s1 = next(inc_straight_gen)
        s2 = next(two_pairs_gen)
        s3 = next(forbidden_gen)
        while s1 != s2 or s1 != s3:
            if s1 < s2:
                if s1 < s3:
                    s1 = next(inc_straight_gen)
                else:
                    s3 = next(forbidden_gen)
            else:
                if s1 < s2:
                    s1 = next(inc_straight_gen)
                else:
                    s2 = next(two_pairs_gen)
        yield s1

if __name__ == "__main__":
    input = 'hxbxwxba'
    gen = next_password(input)
    print(next(gen))
    print(next(gen))