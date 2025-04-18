# import random

# def guess_the_number():
#     """"
#     project2 Number Guessing Game in python
#     """
#     number=random.randint(1,10)
#     gues_left=7
#     print("Welcome to the Number  Guessing game")
#     print("I am thinking a Number between 1-10")

#     while gues_left>0:
#         print(f"\n You have {gues_left} guesses left")
#         try:
#             gues=int(input("Take a  Guess of another Number"))
#         except ValueError:
#             print("Invailed Input please enter a  number")
#             continue
#         if gues<number:
#             print("Too Low Number Tell another")
#         elif gues>number:
#             print("Too high Number Tell another")
#         else:
#             print(f"Congratulations You got the correct Number in {7-gues_left +1} tries")
#             return
        
#         gues_left-=1


#         print(f"\n You ran out a guess: The Number Was{number}")

#         guess_the_number()
        



















import random

def guess_the_number():
    """
    Project 2: Number Guessing Game in Python
    """
    number = random.randint(1, 10)
    gues_left = 7
    print("Welcome to the Number Guessing game")
    print("I am thinking of a number between 1 and 10.")

    while gues_left > 0:
        print(f"\nYou have {gues_left} guesses left")
        try:
            gues = int(input("Take a Guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if gues < number:
            print("Too low! Try again.")
        elif gues > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {7 - gues_left + 1} tries!")
            return
        
        gues_left -= 1
    
    # If out of guesses
    print(f"\nYou ran out of guesses! The number was {number}.")

# Call the function to start the game
guess_the_number()

