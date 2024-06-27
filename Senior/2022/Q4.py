n, c = map(int, input().split())  # Read input for n and c
count = [0] * c  # Initialize count array
points = list(map(int, input().split()))  # Read the positions of points

# Count the occurrences of each point
for x in points:
    count[x] += 1

# Compute the cumulative sum of counts
sum = [count[0]]
for i in range(1, c):
    sum.append(sum[-1] + count[i])

def point(a, b):
    if a <= b:
        return sum[b] - (sum[a - 1] if a > 0 else 0)
    else:
        return sum[b] + (sum[c - 1] - sum[a - 1])

# Calculate the answer
answer = n * (n - 1) * (n - 2) // 6
for i in range(c):
    opposite = (i + c // 2) % c
    total = point((i + 1) % c, opposite)
    answer -= count[i] * total * (total - 1) // 2
    answer -= count[i] * (count[i] - 1) // 2 * total
    answer -= count[i] * (count[i] - 1) * (count[i] - 2) // 6

if c % 2 == 0:
    for i in range(c // 2):
        opposite = i + c // 2
        answer += count[i] * (count[i] - 1) // 2 * count[opposite]
        answer += count[i] * count[opposite] * (count[opposite] - 1) // 2

print(answer)
