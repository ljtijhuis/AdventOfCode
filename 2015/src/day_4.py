import hashlib

def find_first_hash(input, extra_zero = False):
    i = 0
    check = '000000' if extra_zero else '00000'
    while True:
        hash = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
        if hash.startswith(check):
            return i
        i += 1

if __name__ == "__main__":
    input = 'ckczppom'
    print(find_first_hash(input))
    print(find_first_hash(input, True))