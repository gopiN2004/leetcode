def buy_sell_stock(prices):
    min_price=min(prices)
    min_index=prices.index(min_price)
    if min_index==len(prices)-1:
        return 0
    next_index=prices[min_index+1:]
    max_price=max(next_index)
    return max_price-min_price
prices=[7,1,5,3,6,4]
print(buy_sell_stock(prices))