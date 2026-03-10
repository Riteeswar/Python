# 5. Evaluate expression using nested if

n1 = int(input("Enter n1: "))
o1 = input("Enter operator1 (+,-,*): ")
n2 = int(input("Enter n2: "))
o2 = input("Enter operator2 (+,-,*): ")
n3 = int(input("Enter n3: "))

if o1 == '+':
    temp = n1 + n2
elif o1 == '-':
    temp = n1 - n2
else:
    temp = n1 * n2

if o2 == '+':
    result = temp + n3
elif o2 == '-':
    result = temp - n3
else:
    result = temp * n3

print("Result =", result)