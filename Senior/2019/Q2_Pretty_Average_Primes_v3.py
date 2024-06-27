numTestCases = int(input(""))

def isPrimeFuc(num):
	if num == 2:
		return True

	elif num == 1 or num == 0 or num%2 == 0:
		return False
	for count in range(3, int(num/2)+1, 2):
		if (num%count) == 0:
			return False
	return True


def findPrimePair(number):
    result = ""
    for i in range(number, 2, -1):
        if isPrimeFuc(i):
            pairNum = number*2 - i
            if isPrimeFuc(pairNum):
                result = str(i) + ' ' + str(pairNum)
                break
    return result

result = []
for i in range(numTestCases):
    n = int(input(""))
    if isPrimeFuc(n):
        result.append(str(n) + ' ' + str(n))
    else:
        result.append(findPrimePair(n))

for i in result:
    print(i)
