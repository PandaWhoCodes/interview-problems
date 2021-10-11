def pascal_triangle_row(n):
    triangle = [[1] * i for i in range(1, n + 1)]
    for i in range(1,n):
        for j in range(1,i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle


if __name__ == "__main__":
    triangle = pascal_triangle_row(6)
    # print the triangle properly
    # padding = len(triangle[-1]) -1
    # for row in triangle:
    #     print(" "*padding + ' '.join(str(x) for x in row))
    #     padding -= 1
    
    # print the last line as per the problem
    print(*triangle[-1])

