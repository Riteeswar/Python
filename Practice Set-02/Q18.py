# 18. Library fine

days = int(input("Days late: "))

if days <= 5:
    fine = days * 0.5
elif days <= 10:
    fine = days * 1
elif days <= 30:
    fine = days * 5
else:
    print("Membership cancelled")
    exit()

print("Fine =", fine)