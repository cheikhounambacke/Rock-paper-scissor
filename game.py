import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images = [rock, paper, scissor]

user_choice = int(input('choose 0 for rock, 1 for paper and 2 for scissor:\n '))
player = images[user_choice]
print(player)


computer_choice = random.randint(0,2)
computer = images[computer_choice]
print(computer)


def game_logic():
    if player == computer:
        print('draw')
    elif user_choice > computer_choice:
        print('you win')
    elif user_choice == 0 and computer_choice == 1:
        print('you lose')
    elif user_choice > 3 and user_choice < 0:
        print('out of range')
    else:
        print('this is not a number')





game_logic()



