def max_profit(prices):
    if not prices or len(prices)<2:
        return 0
    min_prices=prices[0]
    max_profit=0
    for price in prices[1:]:
        profit=price-min_prices
        if profit>max_profit:
            max_profit=profit
        if price<min_price:
            min_price=price
    return max_profit

if __name__=="__main__":
    prices=[800,300,600,200,100]
    print(max_profit(prices))

    prices=[800,300,200,100,0]
    print(max_profit(prices))

  


