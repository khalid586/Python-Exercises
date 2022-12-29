stockPrices = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}
q = int(input("Enter your query(1 for printing stockprices and 2 for adding stockPrice: "))
sm = 0
if q == 1:
    for k in stockPrices:
        sm = 0
        for i in stockPrices[k]:
            sm += i
        print(f"{k} ==> avg = {sm/len(stockPrices[k])}")
