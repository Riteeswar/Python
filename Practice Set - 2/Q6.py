# 6. Check positive, negative or zero

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > 0 and b > 0:
    print("Both positive")
elif a < 0 and b < 0:
    print("Both negative")
elif a == 0 or b == 0:
    print("At least one number is zero")
else:
    print("One positive and one negative")