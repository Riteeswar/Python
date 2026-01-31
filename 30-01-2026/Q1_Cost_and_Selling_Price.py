# Write a program that takes as input the cost and the selling price of an item, prints whether the sale resulted in a
# profit or loss, and prints the profit/loss incurred.

a = float(input("Enter the cost of the item : "))
b = float(input("Enter the selling price of the item : "))
if(a > b):
    print(f"The item is in sale and it is a profit of {a - b}")
else:
    print(f"The item is not in sale and it is a loss of {b - a}")