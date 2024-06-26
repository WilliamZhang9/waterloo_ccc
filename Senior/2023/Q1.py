# find the pattern and build the formula


# Read the number of columns
C = int(input())

# Read the rows of tiles
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

# Initialize tape length to 0
tape_length = 0

# Count black tiles
count_black_tiles = row1.count(1) + row2.count(1);

adjections = 0
col_number = len(row1)

for col in range(col_number):
    if col < col_number -1 and row1[col] == 1 and row1[col+1] == 1:
        adjections = adjections+1
    if row1[col] == 1 and row2[col] == 1 and col%2==0:
        adjections = adjections+1
    if col < col_number -1 and row2[col] == 1 and row2[col+1] == 1:
        adjections = adjections+1
        
# Output the tape length
print(count_black_tiles*3-adjections*2)
