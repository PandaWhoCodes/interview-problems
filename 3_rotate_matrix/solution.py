import numpy as np
if __name__ == "__main__":
    mat = np.array([[1,2,3],[4,5,6],[7,8,9]], int)
    x = int(input("No of rotations (negative integer for clockwise rotations)"))
    print(np.rot90(mat, x))