def rotate_circle(mat, n, circle_no=1):
    start = circle_no - 1
    end = n - circle_no
    temp = mat[start][start]
    for i in range(start, end+1):
        for j in range(start + 1, end+1):
            if i == start:
                temp, mat[i][j] = mat[i][j], temp
                # mat[i][j] = temp
            elif j == end:
                temp, mat[i][j] = mat[i][j], temp
    for i in range(end, start-1, -1):
        for j in range(end-1, start-1, -1):
            if i == end:
                mat[i][j], temp = temp, mat[i][j]
            elif j == start:
                mat[i][j], temp = temp, mat[i][j]
    print(*[x for x in mat], sep="\n")
        
                
    
    


if __name__ == "__main__":
    mat = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    print(*[x for x in mat], sep="\n")
    print()
    rotate_circle(mat, 4, 1)
