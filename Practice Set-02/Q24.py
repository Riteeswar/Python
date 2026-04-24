# 24. Quotient and remainder without / or %

n = int(input("Enter number: "))

q = n >> 1
r = n & 1

print("Quotient =", q)
print("Remainder =", r)