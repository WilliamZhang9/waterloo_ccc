numTestCases = int(input(""))

def isPrimeFuc(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    return isPrime


def findAllPrimes(upperLimit):
    result = []
    for i in range(3, upperLimit):
        isPrime = True
        if i > 23:
            for k in range(2, 24):
                if i % k == 0:
                    isPrime = False
                    continue

        if isPrime == False:
            continue

        isPrime = isPrimeFuc(i)
        if isPrime: 
            result.append(i)
    return result


def findPrimePair(number):
    foundResult = False
    result = ""
    for a in primes:
        if foundResult:
            break

        for b in primes:
            if(a + b) == number *2:
                result = str(a) + ' ' + str(b)
                foundResult = True
                break
    return result


primes = findAllPrimes(2000000)

result = []
for i in range(numTestCases):
    n = int(input(""))
    result.append(findPrimePair(n))

for i in result:
    print(i)
