items = ["eggs", "milk", "bread", "cheese", "cereal"]
prices = [1, 4.5, 2, 4, 6]

for i in range(0, len(items)):
    print(f"I bought {items[i]} for ${prices[i]}")

total_cost = 0
for price in prices:
    total_cost += price

print(f"I spent ${total_cost} at Walmart")

highest_price = prices[0]
lowest_price = prices[0]
highest_index, lowest_index = 0, 0

for i in range(len(prices)):
    if prices[i] > highest_price:
        highest_price = prices[i]
        highest_index = i
    elif prices[i] < lowest_price:
        lowest_price = prices[i]
        lowest_index = i

print(f"The most expensive item was {items[highest_index]} at ${highest_price}")
print(f"The least expensive item was {items[lowest_index]} at ${lowest_price}")