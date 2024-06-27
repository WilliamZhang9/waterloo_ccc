n = int(input())
t = int(input())

# initialize grid
matrix = [[1 for x in range(n)] for y in range(n)]
for i in range(0,t):
    rowStr, colStr = input().split(' ')
    row = int(rowStr) -1
    col = int(colStr) -1
    matrix[row][col] = 0

maximum = 0
matrixLeft = [[1 for x in range(n)] for y in range(n)]
matrixUpper = [[1 for x in range(n)] for y in range(n)]
matrixDown = [[1 for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            matrixLeft[i][j] = 0
            matrixUpper[i][j] = 0
            matrixDown[i][j] = 0
        else:
            if i == 0 and j == 0:
                matrixLeft[i][j] = 1
                matrixUpper[i][j] = 1
                matrixDown[i][j] = 1
            elif i == 0:
                matrixLeft[i][j] = matrixLeft[i][j-1]+1
                matrixUpper[i][j] = 1
                matrixDown[i][j] = 1
            elif j == 0:
                matrixLeft[i][j] = 1
                matrixUpper[i][j] = matrixUpper[i-1][j]+1
                matrixDown[i][j] = 1
            else:
                matrixLeft[i][j] = matrixLeft[i][j-1]+1
                matrixUpper[i][j] = matrixUpper[i-1][j]+1
                matrixDown[i][j] = min(matrixLeft[i][j],matrixUpper[i][j],matrixDown[i-1][j-1]+1)
        temp = matrixDown[i][j]
        if temp > maximum:
            maximum = temp
print(maximum)