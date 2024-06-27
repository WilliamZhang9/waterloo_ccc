def calculate_fence_area(N, heights, widths):
    total_area = 0
    for i in range(N):
        a = heights[i]
        b = heights[i + 1]
        h = widths[i]
        area = (a + b) / 2 * h
        total_area += area
    return total_area

# Input: Read the number of pieces
N = int(input().strip())

# Input: Read the heights of the pieces
heights = list(map(int, input().strip().split()))

# Input: Read the widths of the pieces
widths = list(map(int, input().strip().split()))

# Calculate the total area of the fence
total_area = calculate_fence_area(N, heights, widths)

# Output the total area of the fence
print(total_area)