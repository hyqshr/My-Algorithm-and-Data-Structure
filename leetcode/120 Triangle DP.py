def minimumTotal3(triangle):
    if not triangle:
        return
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            print(j,i)
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]
minimumTotal3([[2],[3,4],[6,5,7],[4,1,8,3]])