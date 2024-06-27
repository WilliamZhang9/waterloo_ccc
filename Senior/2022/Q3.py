# https://www.geekedu.org/blogs/2022-waterloo-ccc-senior-problem-solution

# Define the maximum value, though it's not used in the translated code directly.
mx = 3e6 + 9

# Read input values n, m, k
n, m, k = map(int, input().split())

# Initialize the ans list to store the sequence
answer = []

# Loop over the range of n
for i in range(n):
    rem = n - i - 1
    current = min(k - rem, m)
    
    # If cur is less than or equal to zero, break out of the loop
    if current <= 0:
        break
    
    # Calculate the value to be appended to answer
    if current > i:
        value = min(m, i + 1)
        current = value
    else:
        value = answer[i - current]
    
    answer.append(value)
    k = k - current

# Check if the sequence is complete and print it, else print -1
if k == 0 and len(answer) == n:
    print(' '.join(map(str, answer)))
else:
    print(-1)
