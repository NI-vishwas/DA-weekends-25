house_prices = {"bangalore": 25000,"mangalore":26000,"grapes":78}
# Calculate the total prices of each property
total = 0
for val in house_prices.values():
    total += val

print("The total prices of house prices is:",total)