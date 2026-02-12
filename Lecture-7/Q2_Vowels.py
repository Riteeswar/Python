def vowel_consonant (s):
    vowel = 0
    consonant = 0
    vowels = "aeiouAEIOU"
    for i in s:
        if i in vowels:
            vowel += 1
        else:
            consonant += 1
    return (f"There are {vowel} vowels are present and there are {consonant} consonants are present")

s = input("Enter a string : ")
print(vowel_consonant(s))