# Problem Set 2, hangman.py
# Name: Chagam Riteeswar Reddy
# Collaborators: Riteeswar, Vamsi Krishna, Bhavesh
# Time spent: 2 days

# Hangman Game
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "_ "
    return result

def get_available_letters(letters_guessed):
    available = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter
    return available

def hangman(secret_word):
    print("Welcome to Hangman!")
    print("The word has", len(secret_word), "letters.")

    guesses = 6
    letters_guessed = []

    while guesses > 0:
        print("\nYou have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Enter a single letter.")
            continue
        if guess in letters_guessed:
            print("You already guessed that letter.")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:",
                  get_guessed_word(secret_word, letters_guessed))
            guesses -= 1

        if is_word_guessed(secret_word, letters_guessed):
            print("\nCongratulations, you won!")
            return

    print("\nSorry, you ran out of guesses.")
    print("The word was:", secret_word)

def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] == "_":
            if other_word[i] in my_word:
                return False
        elif my_word[i] != other_word[i]:
            return False
    return True

def show_possible_matches(my_word):
    matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)
    if matches:
        print("Possible matches:", " ".join(matches))
    else:
        print("No matches found")

def hangman_with_hints(secret_word):
    print("Welcome to Hangman with hints!")
    print("The word has", len(secret_word), "letters.")
    guesses = 6
    letters_guessed = []

    while guesses > 0:
        print("\nYou have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Enter a letter (* for hint): ").lower()

        if guess == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input.")
            continue

        if guess in letters_guessed:
            print("Already guessed.")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Wrong guess:", get_guessed_word(secret_word, letters_guessed))
            guesses -= 1

        if is_word_guessed(secret_word, letters_guessed):
            print("\nYou won!")
            return

    print("\nYou lost. The word was:", secret_word)


if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman(secret_word)

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)