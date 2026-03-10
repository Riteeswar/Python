# 8. Toggle case using bitwise

s = input("Enter word: ")
result = ""

for ch in s:
    result += chr(ord(ch) ^ 32)

print("Toggled word:", result)