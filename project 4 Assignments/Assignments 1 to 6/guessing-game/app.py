# import random

# number=random.randint(1,10)
# print("Guess Number Between 1-10")

# while True:
#     guess=int(input("Enter your guess Number"))
#     if guess<number:
#         print("Too low Number")
#     elif guess> number:
#         print("Too High Number")
#     else:
#         print("Congratulations You got it right")
#         break
import random
number=random.randint(1,10)
print("Guess Number between 1-10")
while True:
  guess=int(input("Enter your Guess Number"))
  if guess<number:
   print("Too low number")
  elif guess>number:
   print("To High number")
  else:
   print("Congratulations to got it right")
   break