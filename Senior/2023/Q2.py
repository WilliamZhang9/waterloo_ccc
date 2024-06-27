# directory is a good data strcture to store min/max values

# this code is finding the minimum total difference in height between pairs of points equidistant 
# from the center for all possible sub-sequences of the original sequence of heights. 

# Algorithm can be used in processing a sequence of numbers: 
#     find the most symetrical groping, 
#     find the dsata is most stable around a centain point
#     cases when Symmetry plays a key role: DNA, cryptography


N = int(input())
heights = list(map(int, input().split()))

# Initialize the output array with large numbers
output = [float('inf')] * N

# Iterate through all potential midpoints for the crops
for midpoint in range(N):
    # Initialize the asymmetric value (accumulator)
    asym_value = 0
    
    # Odd-length crops
    l = r = midpoint
    while l >= 0 and r < N:
        # Calculate the asymmetric value for the crop [l, r]
        asym_value += abs(heights[l] - heights[r])
        length = r - l + 1
        output[length - 1] = min(output[length - 1], asym_value)
        
        l -= 1
        r += 1

    # Even-length crops
    asym_value = 0
    l, r = midpoint, midpoint + 1
    while l >= 0 and r < N:
        # Calculate the asymmetric value for the crop [l, r]
        asym_value += abs(heights[l] - heights[r])
        length = r - l + 1
        output[length - 1] = min(output[length - 1], asym_value)
        
        l -= 1
        r += 1

print(" ".join(map(str, output)))
