import math
from src.file_utils import read_file


def paper_needed(input):
    [l, w, h] = map(int, input.split('x'))
    total_surface = 2*l*w + 2*w*h + 2*h*l
    smallest_side = min(l*w, w*h, h*l)
    return total_surface + smallest_side

def ribbon_needed(input):
    d = list(map(int, input.split('x')))
    d.sort()
    return d[0]*2 + d[1]*2 + math.prod(d)

input = read_file('/../input/day_2.txt')
lines = input.split()

total_paper = 0
total_ribbon = 0
for line in lines:
    total_paper += paper_needed(line)
    total_ribbon += ribbon_needed(line)

print(total_paper)
print(total_ribbon)
