# Read the input
M = int(input())
N = int(input())
K = int(input())

# Initialize the row and column paint counts
row_paints = [0] * (M + 1)
col_paints = [0] * (N + 1)

# Process the choices
for _ in range(K):
    choice, index = input().split()
    index = int(index)
    if choice == 'R':
        row_paints[index] += 1
    else:  # choice == 'C'
        col_paints[index] += 1

# Count the gold cells
gold_cells = 0
for i in range(1, M + 1):
    for j in range(1, N + 1):
        if (row_paints[i] + col_paints[j]) % 2 == 1:
            gold_cells += 1

# Output the result
print(gold_cells)
