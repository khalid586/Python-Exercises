# You are given following list of stocks and their prices in last 3 days,
#
# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc)
# then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering
# 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

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
    value = float(input("Enter the value of the stock: "))
    if stock in stockPrices:
        stockPrices[stock].append(value)
    else:
        stockPrices[stock] = [value]

    for stock, stockPrice in stockPrices.items():
        print(f"{stock} ==> {stockPrice}")

