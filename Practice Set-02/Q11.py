# 11. Day of week from date

d = int(input("Day: "))
m = int(input("Month: "))
y = int(input("Year: "))

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

n = (d + m + y) % 7

print("Day =", days[n])