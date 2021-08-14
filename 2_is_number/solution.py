""""
Valid Numbers
123" # Integer
"12.3" # Floating point
"-123" # Negative numbers
"-.3" # Negative floating point
"1.5e5" # Scientific notation

invalid numbers
"12a" # No letters
"1 2" # No space between numbers
"1e1.2" # Exponent can only be an integer (positive or negative or 0)

"""
import re

def is_number(st):
    return True if re.fullmatch(r'-?[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+\.?[0-9])|-?\d+\.\d+|-?\b\d+\b', str(st)) else False

if __name__ == "__main__":
    print(is_number(-123))
    print(is_number(12.3))
    print(is_number(-123))
    print(is_number(-123e-12))
    print(is_number("12a"))
    print(is_number("1 2"))
    print(is_number("1e1.2"))
    print(is_number("1.2.23"))
    # print(is_number())
    # print(is_number())
