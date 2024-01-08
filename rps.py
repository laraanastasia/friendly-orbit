import random
user_action= input("Enter a choice (rock, paper, sciccors):")
possible_actions= ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print({computer_action})
if user_action == computer_action:
    print(f"Both players selected {user_action}. It´s a tie!")
elif user_action == "rock":
    if computer_action == "paper":
        print(f"Computer wins! {computer_action} beats {user_action}")
    elif computer_action == "scissors":
        print(f"Player wins! {user_action} beats {computer_action}")

elif user_action == "paper": 
    if computer_action == "scissors":
        print(f"computer wins! {computer_action} beats {user_action}")
    elif computer_action == "rock":
        print(f"Player wins! {user_action} beats {computer_action}")

elif user_action == "scissors":
    if computer_action == "rock":
        print(f"computer wins! {computer_action} beats {user_action}")
    elif computer_action == "paper":
        print(f"Player wins! {user_action} beats {computer_action}")