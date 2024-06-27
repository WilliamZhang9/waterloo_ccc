def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

word = input()
temp = ''
countL = 0
countM = 0
countS = 0
for i in word:
    if i == 'L':
        countL += 1
    elif i == 'M':
        countM += 1
    else:
        countS +=1

wordList = list(word)
for i in range(0, len(word)):
    if i < countL:
     if wordList[i] == 'L':
        continue
     


    
 
pos1, pos2  = 1, 3
print(swapPositions(wordList, pos1-1, pos2-1))