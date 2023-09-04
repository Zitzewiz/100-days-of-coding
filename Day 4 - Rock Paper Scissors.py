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
import random

poses = [rock,paper,scissors]

play_again = "y"

while play_again == "y":
  player_choice_no = int(input("What are you choosing? Rock (1), Paper (2), or Scissors (3)? \n"))
  player_choice = poses[player_choice_no-1]
  print(player_choice)
  
  computer_choice = random.choice(poses)
  print(computer_choice)
  
  if computer_choice == player_choice:
      print("It's a draw.")
  
  elif player_choice == rock:
    if computer_choice == paper:
      print("computer wins")
    if computer_choice == scissors:
      print ("player wins")
  
  elif player_choice == paper:
    if computer_choice == scissors:
      print("computer wins")
    if computer_choice == rock:
      print ("player wins")
  
  elif player_choice == scissors:
    if computer_choice == rock:
      print("computer wins")
    if computer_choice == paper:
      print ("player wins")

  play_again = input("Do you wanto to play again? (y/n) \n")
  
