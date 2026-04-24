# 25. Decimal to hexadecimal without hex()

n = int(input("Enter number: "))

digits="0123456789ABCDEF"
res=""

while n>0:
    r=n%16
    res=digits[r]+res
    n//=16

print("Hex =",res)