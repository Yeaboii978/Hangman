import random, hangman
from PyDictionary import PyDictionary

dictionary=PyDictionary()

with open("words.txt", "r") as file:
    word_list = [word.strip() for word in file]

word = random.choice(word_list)

word_length = len(word)
print(f"The word has {word_length} characters.")

hidden_word = ["_"] * len(word)
guesses_remaining = 7
letters_guessed = []
num_guess = 0

while True:
    print(" ".join(hidden_word))    
    print("Letters guessed: ", " ".join(letters_guessed))
    guess = input("Guess a letter: ")
    if len(guess) != 1:
        print("Please enter a single letter.")
        continue
    if guess in letters_guessed:
        print("You already guessed that letter.")
        continue
    letters_guessed.append(guess)
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        print("Incorrect.")
        guesses_remaining -= 1
        num_guess += 1
        print(hangman.hangman_stages[num_guess])
        if guesses_remaining == 0:
            print("You lose.")
            print("The word was:", word)
            break
    if "_" not in hidden_word:
        print(word)
        print("You win!")
        break


