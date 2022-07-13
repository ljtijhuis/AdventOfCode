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