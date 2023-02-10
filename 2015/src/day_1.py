from src.file_utils import read_file


def final_floor(input):
    return input.count('(') - input.count(')')

def basement_position(input):
    position = 0
    floor = 0
    while floor != -1:
        if (input[position] == '('):
            floor += 1
        else:
            floor -= 1
        position += 1
    
    return position

if __name__ == "__main__":
    input = read_file('/../input/day_1.txt')

    print(final_floor(input))
    print(basement_position(input))
