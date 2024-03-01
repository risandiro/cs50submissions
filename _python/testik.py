stocks = {
    "AAPL": 187.31,
    "MSFT": 124.06,
    "FB": 183.50
    }

keys = []
values = []
for key, value in stocks.items():
    keys.append(key)
    values.append(value)
print("Keys: ", *keys, "Values: ", *values)
