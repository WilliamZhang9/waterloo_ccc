def total_walking_time(c, friends):
    total_time = 0
    for p, w, d in friends:
        distance = max(0, abs(p - c) - d)
        total_time += distance * w
    return total_time

def find_min_walking_time(friends):
    # Start the binary search between the minimum and maximum positions
    left, right = min(friends)[0], max(friends)[0]
    while left < right:
        mid = (left + right) // 2
        time_mid = total_walking_time(mid, friends)
        time_next = total_walking_time(mid + 1, friends)
        
        # Decide which half to continue searching in
        if time_mid < time_next:
            right = mid
        else:
            left = mid + 1
            
    # The left pointer will be at the optimal position after the search ends
    return total_walking_time(left, friends)

# Input
N = int(input())
friends = []
for _ in range(N):
    P, W, D = map(int, input().split())
    friends.append((P, W, D))

# Output the minimum possible sum of walking times
print(find_min_walking_time(friends))
