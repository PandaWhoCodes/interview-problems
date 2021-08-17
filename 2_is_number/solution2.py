import re

def is_number(st):
    return True if re.fullmatch(r'-?[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+\.?[0-9])|-?\d+\.\d+|-?\b\d+\b', str(st)) else False

if __name__ == "__main__":
    print(is_number(-123))