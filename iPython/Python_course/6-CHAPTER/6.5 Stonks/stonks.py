stock_prices = [
    34.68, 36.09, 34.94, 33.97, 34.68,
    35.82, 43.41, 44.29, 44.65, 53.56,
    49.85, 48.71, 48.71, 49.94, 48.53,
    47.03, 46.59, 48.62, 44.21, 47.21
]

def price_at(x):
    return stock_prices[x - 1]

def max_price(a, b):
    return max(stock_prices[a - 1 : b])

def min_price(a, b):
    return min(stock_prices[a - 1 : b])

print("Price on day 1:", price_at(1))           
print("Price on day 10:", price_at(10))    

print("Max price from day 1 to 5:", max_price(1, 5)) 
print("Max price from day 6 to 15:", max_price(6, 10))

print("Min price from day 1 to 5:", min_price(11, 15))
print("Min price from day 10 to 20:", min_price(16, 20))