def numberWays(n):
    listResult = [0] * (n + 1)
    listResult[0] = 1
    for i in range(4, n + 1):
        listResult[i] += listResult[i - 4]
    for i in range(5, n + 1):
        listResult[i] += listResult[i - 5]
    return listResult[n]
inputNumber = int(input())
print(numberWays(inputNumber)) 