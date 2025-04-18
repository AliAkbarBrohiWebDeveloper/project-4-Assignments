import random

game_choices=["rock","paper","Scissors"]

player_choice=input("Enter: ,rock ,paper ,Scissors").lower()
computer_choice=random.choice(game_choices)
if player_choice==computer_choice:
    print(f"same choices both {player_choice} so Its tie")

elif player_choice== "rock" and computer_choice=="Scissors":
    print(f"PLayers Wins {player_choice} beats {computer_choice}")

elif player_choice=="paper" and computer_choice=="rock":
    print(f"Players Wins {player_choice} beats {computer_choice}")

elif player_choice=="Scissors" and computer_choice=="paper":
    print(f"Players Wins {player_choice} beats {computer_choice}")
    
else :
    print(f"Computer Wins {computer_choice} beats {player_choice}")



