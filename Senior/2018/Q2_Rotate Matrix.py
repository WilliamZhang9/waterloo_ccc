

# Function to rotate the matrix
# 90 degree clockwise
def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

def isValidMatrix(A):
    return A[0][0] < A[0][1] and A[1][0] > A[0][0] and A[1][1] > A[1][0] and A[1][1] > A[0][1]
   
def printResult(A):
    for row in A:
        print(' '.join(map(str, row)))

n = int(input())
matrix = []
count = 0
while count < n:
    count += 1
    list_of_strings = input().split()
    matrix.append(list(map(int, list_of_strings)))

rotateCount = 0
while rotateCount <= 3:
    rotateCount +=1
    if isValidMatrix(matrix):
        printResult(matrix)
    else:
        rotate90Clockwise(matrix)

