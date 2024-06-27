numTestCases = int(input(""))

def isPrimeFuc(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break
    return isPrime


def findAllPrimes(number):
    result = []
    upperLimit = number*2
    for i in range(3, upperLimit):
        isPrime = isPrimeFuc(i)
        if isPrime: 
            result.append(i)
    return result


def findPrimePair(number):
    primes = findAllPrimes(number)
    foundResult = False
    result = ""
    for a in primes:
        if foundResult:
            break

        for b in primes:
            if(a + b) == n *2:
                result = str(a) + ' ' + str(b)
                foundResult = True
                break
    return result

result = []
for i in range(numTestCases):
    n = int(input(""))
    result.append(findPrimePair(n))

for i in result:
    print(i)
