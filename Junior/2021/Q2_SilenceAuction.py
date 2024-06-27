bidNumber = int(input("how many bids?"))
winnerName = ''
winnerPrice = 0
for i in range(bidNumber):
    name = input("bidder name: ")
    price = int(input("bid price: "))
    if price > winnerPrice:
        winnerPrice = price
        winnerName = name

print(winnerName)
