# 16. Insurance Premium Program

health = input("Health (excellent/poor): ")
age = int(input("Age: "))
place = input("City or Village: ")
gender = input("Gender (male/female): ")
policy = int(input("Policy amount: "))

if age < 25 or age > 65:
    print("Person not insured")

else:

    if health=="excellent" and 25<=age<=35 and place=="city" and gender=="male":
        max_amt=200000
        premium=4000

    elif health=="excellent" and 25<=age<=35 and place=="city" and gender=="female":
        max_amt=150000
        premium=3000

    elif health=="poor" and 25<=age<=35 and place=="village" and gender=="male":
        max_amt=100000
        premium=6000

    else:
        max_amt=125000
        premium=5000

    if policy>max_amt:
        print("Policy exceeds limit")
    else:
        premium=(policy/max_amt)*premium
        print("Monthly premium =",premium)