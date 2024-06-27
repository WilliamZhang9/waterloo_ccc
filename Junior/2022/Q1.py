n = int(input())
t = int(input())

# initialize grid
grid = [[0 for x in range(n)] for y in range(n)]
for i in range(0,t):
    rowStr, colStr = input().split(' ')
    row = int(rowStr) -1
    col = int(colStr) -1
    grid[row][col] = 1

s = []
for i in range(n):
    temp = []
    for j in range(n):
        if i==0 or j==0:
            temp += grid[i][j],
        else:
            temp += 0,
        s += temp,

for i in range(1, n):
    for j in range(1, n):
        if (grid[i][j] == 1):
            s[i][j] = min(s[i][j-1], s[i-1][j],
                        s[i-1][j-1]) + 1
        else:
            s[i][j] = 0
    
# Find the maximum entry and
# indices of maximum entry in S[][]
max_of_s = s[0][0]
max_i = 0
max_j = 0
for i in range(n):
    for j in range(n):
        if (max_of_s < s[i][j]):
            max_of_s = s[i][j]
            max_i = i
            max_j = j

print("Maximum size sub-matrix is: ")
for i in range(max_i, max_i - max_of_s, -1):
    for j in range(max_j, max_j - max_of_s, -1):
        print (grid[i][j], end = " ")
            