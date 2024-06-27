n = int(input())
t = int(input())
rowPositions = []
colPositions = []
positions = []
maxSquareLenght = 0
for i in range(0,t):
    row, col = input().split(' ')
    rowPositions.append(row)
    colPositions.append(col)
    positions.append([row, col])

rowPositions.sort()
colPositions.sort()

def nearestRowTree(tree):
    nearestLen = 0
    nearestTree = tree
    for i in range(0,t):
       row, col =  positions[i]
       distance = abs(row - tree[0]) + abs(col - tree[1])
       if distance < nearestLen:
           nearestLen = distance
           nearestTree = positions[i]
    return nearestTree

for i in range(0,t):
