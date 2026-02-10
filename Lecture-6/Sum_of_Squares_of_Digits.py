a = int(input("Enter an integer: "))
sum = 0
while(a!=0):
    last = a%10
    sum += (last*last)
    a //= 10
print(sum)