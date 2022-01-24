import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choices = [rock,paper,scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

#Original solution
# if player_choice == computer_choice:
#   result = "Draw"
# elif player_choice > computer_choice:
#   if player_choice == 2 and computer_choice == 0:
#     result = "You lose"
#   else:
#     result = "You win"
# else:
#   if player_choice == 0 and computer_choice == 2:
#     result = "You win"
#   else:
#     result = "You lose"

#instructor solution
if player_choice >= 3 or player_choice < 0:
  print("You typed an invalid number. You lose!")
else:
  print(choices[player_choice])

  if player_choice == 0 and computer_choice == 2:
    result = "You win"
  elif computer_choice == 0 and player_choice == 2:
    result = "You lose"
  elif computer_choice > player_choice:
    result = "You lose"
  elif player_choice > computer_choice:
    result = "You win"
  elif computer_choice == player_choice:
    result = "Draw"
  
  print("Computer chose:")
  print(choices[computer_choice])
  print(result)