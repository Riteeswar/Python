# 3. Check if number divisible by 4 using bitwise

n = int(input("Enter number: "))

if (n & 3) == 0:
    print("Divisible by 4")
else:
    print("Not divisible by 4")