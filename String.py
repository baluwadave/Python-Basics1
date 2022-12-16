#Program to reverse a string
gfg = "ulaB evadaW"
print(gfg[::-1])

#print the Stock price of day1 and day 3

stock_price=[25,28,30,22,35,55]
bsw =stock_price[0],stock_price[2]
print(bsw)
for i in range (len(stock_price)):
    if stock_price[i] == 30:
        print(i)



#print all element stock_price
for price in stock_price:
    print(price)

stock_price.insert(2,777)
print(stock_price)
stock_price.pop(1)

print(stock_price)










