prices = input("unesi cene:").split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input("naziv:").split(",")
budget_per_item = int(input("budzet:"))

affordable_items = []
cant_afford = 0
total_needed = 0


# Write your code below


for i in range(len(prices)):
    if prices[i] <= budget_per_item:
        total_needed+=prices[i]
        affordable_items.append(items[i])
    else:
        cant_afford+=1

print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
