n = int(input())
times = 0
xCoordinates = []
yCoordinates = []
while times < n:
    x,y = input().split(',')
    xCoordinates.append(int(x))
    yCoordinates.append(int(y))
    times += 1
print("{},{}".format(min(xCoordinates)-1, min(yCoordinates)-1))
print("{},{}".format(max(xCoordinates)+1, max(yCoordinates)+1))
