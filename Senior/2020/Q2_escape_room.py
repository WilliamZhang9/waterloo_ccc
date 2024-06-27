m = int(input())
n = int(input())

def escapeRoom(grid):
    visited = set()
    queue = [(1,1)]
    canEscape = False

    while queue:
        curr = queue.pop(0)
        if curr == (m, n):
            return True
        x, y = curr
        for a in range(1, grid[x - 1][y - 1] + 1):
            if grid[x - 1][y - 1] % a == 0:
                b = grid[x - 1][y - 1] // a
                if (a <= m) and (b <= n):
                    next_pos = (a, b)
                    if next_pos not in visited:
                        queue.append(next_pos)
                        visited.add(next_pos)
                        if next_pos == (m, n):
                            canEscape = True
                            break
                if (b <= m) and (a <= n):
                    next_pos = (b, a)
                    if next_pos not in visited:
                        queue.append(next_pos)
                        visited.add(next_pos)
                        if next_pos == (m, n):
                            canEscape = True
                            break
    return canEscape

inputGrid = []
for i in range(m):
    rowValue = [int(x) for x in input().split()]
    inputGrid.append(rowValue)

    
if escapeRoom(inputGrid):
    print('yes')
else:
    print('no')
        
    
    