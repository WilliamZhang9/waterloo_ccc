secret = ""
direction = ""
result = []
while True:
    secret = input("input secret number: ")
    if secret == "99999":
        break
    firstDigit = int(secret[0])
    secondDigit = int(secret[1])
    steps = secret[2:]
    sum = firstDigit + secondDigit
    if sum % 2 != 0:
        direction = 'left'
        
    elif sum % 2 == 0 and sum != 0:
        direction = 'right'
    
    result.append("{} {}".format(direction, steps))

for i in result:
    print(i)
