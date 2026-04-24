# 27. Hexadecimal to decimal (manual)

h=input("Enter hex: ")

digits="0123456789ABCDEF"
value=0

for ch in h:
    value=value*16+digits.index(ch)

print("Decimal =",value)