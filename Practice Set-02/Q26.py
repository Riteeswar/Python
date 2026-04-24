# 26. Decimal to binary without bin()

n = int(input("Enter number: "))
res=""

while n>0:
    res=str(n%2)+res
    n//=2

print("Binary =",res)