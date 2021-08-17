def rotate(mat):
    new_mat = []
    for curr, i in enumerate(range(len(mat)-1,-1,-1)):
        temp = [mat[len(mat)-1-j][curr] for j in range(len(mat))]
        new_mat.append(temp)
    return new_mat




if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    # mat = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    print(rotate(mat))