import string
from src.file_utils import read_file

'''
The only escape sequences used are \\ (which represents a single backslash), \\" (which represents a lone double-quote character), and \\x plus two hexadecimal characters (which represents a single character with that ASCII code).
'''
def character_count(input: str) -> int:
    escape = False
    void_count = 2
    for i in range(0, len(input)):
        c = input[i]
        if c == '\\' and not escape:
            escape = True
        elif escape and (c == '\\' or c == '"'):
            void_count += 1
            escape = False
        elif escape and c == 'x' and i < len(input) - 2 and input[i+1] in string.hexdigits and input[i+2] in string.hexdigits:
            void_count += 3
            escape = False
    return len(input) - void_count


def encoded_character_count(input: str) -> int:
    encoded_characters = { '\\', '"' }
    encode_count = 2
    for i in range(0, len(input)):
        c = input[i]
        if c in encoded_characters:
            encode_count += 1
    return len(input) + encode_count


if __name__ == "__main__":
    input = read_file('/../input/day_8.txt')
    lines = input.splitlines()

    total_length = 0
    total_characters = 0
    total_encoded_characters = 0
    for l in lines:
        total_length += len(l)
        total_characters += character_count(l)
        total_encoded_characters += encoded_character_count(l)
    
    print(total_length - total_characters)
    print(total_encoded_characters - total_length)