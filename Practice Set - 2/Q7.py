# 7. Check if LCM equals one of the numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# GCD
x, y = a, b
while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

if lcm == a or lcm == b:
    print("LCM equals one of the numbers")
else:
    print("LCM is different")