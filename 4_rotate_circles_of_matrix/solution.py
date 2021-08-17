def rotate_circle(mat, n, circle_no=1):
    start = circle_no - 1
    end = n - circle_no
    temp = mat[start][start]
    for i in range(start, end+1):
        for j in range(start + 1, end+1):
            if i == start or j == end:
                temp, mat[i][j] = mat[i][j], temp
    for i in range(end, start-1, -1):
        for j in range(end-1, start-1, -1):
            if i == end or j == start:
                mat[i][j], temp = temp, mat[i][j]
    return mat
        
                
    
    


if __name__ == "__main__":
    # mat = [
    #     [1,2,3,4],
    #     [5,6,7,8],
    #     [9,10,11,12],
    #     [13,14,15,16]
    # ]
    base_mul = 4
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(input().split())
    rotations = int(input())
    if rotations < 0:
        for x in range(base_mul*(n - 1) + rotations):
            mat = rotate_circle(mat, n, 1)
    else:
        for x in range(rotations):
            mat = rotate_circle(mat, n, 1)
    for x in range(n):
        print(*mat[x])