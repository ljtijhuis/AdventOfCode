from src.file_utils import read_file


def houses_visited(input):
    x = 0
    y = 0
    visited = {(0, 0)}
    for d in input:
        if d == '>':
            x += 1
        elif d == '<':
            x -= 1
        elif d == '^':
            y -= 1
        else:
            y += 1
        visited.add((x, y))
    return len(visited)

def houses_visited_with_robot(input):
    c = 0
    x = [0, 0]
    y = [0, 0]
    visited = {(0, 0)}
    for d in input:
        if d == '>':
            x[c] += 1
        elif d == '<':
            x[c] -= 1
        elif d == '^':
            y[c] -= 1
        else:
            y[c] += 1
        visited.add((x[c], y[c]))
        c = (c + 1) % 2
    return len(visited)

if __name__ == "__main__":
    input = read_file('/../input/day_3.txt')
    print(houses_visited(input))
    print(houses_visited_with_robot(input))
