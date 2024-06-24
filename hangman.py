import random

wordlist = ["meowing", "cats", "dog", "person"]
greeting = print("Welcome to Hangman!")
print("You have 5 guesses and for each correct guess you get another guess.")
# Chooses a random word from the word list
sWord = random.choice(wordlist)
# Creating an empty list for creating a "display word" ex. _ _ t _
dWord = []
# Adds each letter from sWord into a list and adds the correct guess letter
for l in sWord:
        dWord += "_"
print(dWord)

num = 0
gameOver = False

while not gameOver:
    # Asks for input and turns it into a lower case letter
    guess = input("Guess a letter ").lower()
    for position in range(len(sWord)):
        letter = sWord[position]
        if len(guess) == 1:
            if letter == guess:
             dWord[position] = letter
        elif len(guess) == 0:
            print("Please guess a letter")
            num -= 1
        else:
            print("Please only guess a single letter")
    if guess in sWord:
        if num == 0:
            num = 0
            gr = 5 - num
            print("Guesses remaning: " + str(gr))
        else:
            num -= 1
            gr = 5 - num
            print("Guesses remaining: " + str(gr))
    elif guess not in sWord:
        num += 1
        gr = 5 - num
        print("Guesses remaining: " + str(gr))
        if num >= 5:
            gameOver = True
    print(dWord)

    if "_" not in dWord:
        print("Congrats, you guessed the word " + sWord)
        gameOver = True