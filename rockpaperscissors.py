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

user_choice = input("Enter your choice (Rock, Paper or Scissors)\n")
possible_actions = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_actions)
game_images = [rock, paper, scissors]

if user_choice== "rock" :
    print(game_images[0])
elif user_choice== "paper":
    print(game_images[1])
elif user_choice== "scissors":
    print(game_images[2])

print(f"\nYou chose {user_choice}!!\n\nComputer chose {computer_choice}!!\n")


if  computer_choice =="rock":
    print(game_images[0])
elif computer_choice =="paper":
    print(game_images[1])
elif  computer_choice =="scissors":
    print(game_images[2])

if user_choice == computer_choice:
    print("Its a draw!!")

elif user_choice=="rock".lower():
    if computer_choice=="scissors":
      print("Rock smashes scissors. You win!!")
    else:
      print("Paper covers rock! You lose")

elif user_choice == "paper".lower():
    if computer_choice == "rock":
         print("Paper covers rock! You win!")
    else:
         print("Scissors cuts paper! You lose.")

elif user_choice == "scissors".lower():
     if computer_choice == "paper":
         print("Scissors cuts paper! You win!")
     else:
         print("Rock smashes scissors! You lose.")
