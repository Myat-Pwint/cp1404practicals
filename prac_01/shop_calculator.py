total_price = 0

total_item = int(input("Number of items: "))
while total_item < 0:
    print("Invalid number of items!")
    total_item = int(input("Number of items: "))

for i in range(total_item):
    item_price = float(input(f"Price of item: {i+1} : $"))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {total_item} items is ${total_price:.2f}")

