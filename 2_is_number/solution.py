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
from collections import defaultdict
def is_number(num):
    allowed = ("-",".","e","1","2","3","4","5","6","7","8","9","0")
    freq = defaultdict(int)
    exponent = False
    num = str(num).lower()
    if "-" in num and "e" not in num and num[0] != "-":
        return False

    for char in num:
        freq[char] += 1
        if char == "e":
            exponent = True
        if char not in allowed:
            return False
        elif exponent and char == "-" and freq[char]>2:
            return False
        elif  char== "." and freq[char]>1:
            return False
        elif char =="." and exponent:
            return False
    return True


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
