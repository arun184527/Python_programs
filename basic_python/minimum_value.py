prices = {"apple": 50, "banana": 20, "orange": 40}
min_key = list(prices.keys())[0]
min_val = prices[min_key]
for k, v in prices.items():
    if v < min_val:
        min_val = v
        min_key = k
print(min_key, min_val)