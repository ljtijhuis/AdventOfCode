
def look_and_say(s: str) -> str:
    i = 0
    current_symbol = None
    current_count = 0
    output = ''
    while i < len(s):
        if current_symbol == None:
            current_symbol = s[i]
            current_count = 1
        elif current_symbol != s[i]:
            output += str(current_count) + current_symbol
            current_symbol = s[i]
            current_count = 1
        else:
            current_count += 1
        i += 1
    output += str(current_count) + current_symbol
    return output 

if __name__ == "__main__":
    input = '1113122113'
    s = input
    for _ in range(0, 40):
        s = look_and_say(s)
    print(len(s))

    s = input
    for _ in range(0, 50):
        s = look_and_say(s)
    print(len(s))