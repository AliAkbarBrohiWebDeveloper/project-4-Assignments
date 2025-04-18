import random

words = ["apple", "Banana", "Orange", "Mango", "Pineapple", "Grapes", "chwerry"]
word = random.choice(words)
guesses = []
attempts = 7

print("Welcome to the Hangman Game!")
print("-" * len(word))

while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a valid letter.")
        continue

    if guess in guesses:
        print("You already guessed that letter.")
        continue

    guesses.append(guess)

    if guess in word:
        print("Good Job!")
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")
    
    
    display_word = " ".join([letter if letter in guesses else "_" for letter in word])
    print(display_word)

   
    if "_" not in display_word:
        print(f"Congratulations, you guessed the word: {word}")
        break 

if attempts == 0:
    print(f"Sorry, you ran out of attempts. The word was {word}.")
    
print("Thank you for playing the game!")
