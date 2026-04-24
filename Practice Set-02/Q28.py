# 28. Binary to decimal

b=input("Enter binary: ")

value=0

for ch in b:
    value=value*2+int(ch)

print("Decimal =",value)