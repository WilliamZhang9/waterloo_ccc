import random
sentence = input("Please enter a sentence: ")
rand = ""
string = []
finString = ""
randStr = ""
distinctWordsDict = {}
level4PlusStr = ""
for i in sentence:
    string += i
for i in range(5):
      randNum = random.randint(0,len(sentence)-1)
      rand += str(randNum) + " "
for i in range(len(sentence)):
    randChar = random.choice(string)
    finString += randChar
print(rand)
print(finString)
for i in range(len(sentence)):
    randStr+= sentence[i]
    randStr += finString[len(sentence)-i-1]
print(randStr)

for i in range(len(randStr)):
    if distinctWordsDict.get(randStr[i]) == None:
        level4PlusStr += randStr[i]
        distinctWordsDict[randStr[i]] = True
       
print(level4PlusStr)