sameGroupConstrains = []
diffGroupConstrains = []
groupIndex = {}

x = int(input())
for i in range(0,x):
    sameGroupNames = input().split(' ')
    sameGroupConstrains.append(sameGroupNames)

y = int(input())
for i in range(0,y):
    diffGroupNames = input().split(' ')
    diffGroupConstrains.append(diffGroupNames)

g = int(input())
for i in range(0,g):
    name1, name2, name3 = input().split(' ')
    groupIndex[name1] = i
    groupIndex[name2] = i
    groupIndex[name3] = i

numOfViolate = 0
for i in range(0,x):
   student1 = sameGroupConstrains[i][0]
   student2 = sameGroupConstrains[i][1]
   if groupIndex[student1] != groupIndex[student2]:
       numOfViolate += 1


for i in range(0,y):
   student1 = diffGroupConstrains[i][0]
   student2 = diffGroupConstrains[i][1]
   if groupIndex[student1] == groupIndex[student2]:
       numOfViolate += 1

print(numOfViolate)