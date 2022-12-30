import statistics

stockPrices = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}
q = int(input("Enter your query(1 for printing stock prices and 2 for adding stockPrice: "))
sm = 0
if q == 1:
    for stock, pricelist in stockPrices.items():
        print(f"{stock} ==> {pricelist} ==> avg = {round(statistics.mean(pricelist),2)}")
else:
    stock = input("Enter the name of the stock you want to input: ")
    value = input("Enter the value of the stock")
    if stock in stockPrices:
        stockPrices[stock].append(value)
    else:
        stockPrices[stock] = value

