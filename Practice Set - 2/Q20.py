# 20. Distributor policy (example logic)

stock = int(input("Stock available: "))
payment = input("Payment done? (yes/no): ")

if stock > 0 and payment == "yes":
    print("Mobile supplied")
elif stock == 0:
    print("Out of stock")
else:
    print("Payment required")