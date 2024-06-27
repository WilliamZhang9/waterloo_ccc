m = int(input())
n = int(input())
k = int(input())
paints = []
for i in range(0,k):
    paints.append(input())

# initialize grid
grid = [['b']*m]*n
print(grid)
for index in range(0, k):
    [direction, numStr] = paints[index].split()
    num = int(numStr)
    # print('direction - {}, number - {}'.format(direction, numStr))
    if direction == 'R':
        for c in range(0, m):
           print("c={}, num={}, grid[num-1][c]={}".format(c, num, grid[num-1][c]))
        #    print(grid)
           grid[num-1][c] = 'g' if grid[num-1][c] == 'b' else 'b'
    elif direction == 'C':
        for c in range(0, n):
           grid[c][num-1] = 'g' if grid[c][num-1] == 'b' else 'b'

    print(grid)

# paints = b b b
#          b b b
#          b b b
   

        #     if paints[num-1][c] == 'b':
        #         paints[num-1][c] = 'g'
        #     else:
        #         paints[num-1][c] = 'b'

