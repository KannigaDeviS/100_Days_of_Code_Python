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
userSign =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
sign = [rock, paper, scissors]
lengthOfSign = len(sign)

if userSign > lengthOfSign - 1 :
    print("You typed an invalid number, you lose!")
else:
    print(sign[userSign])
    print("Computer chose:")
    computerChoice = random.randint(0,lengthOfSign-1)
    #computerChoice=0
    print(sign[computerChoice])

    if userSign==computerChoice or userSign<0:
        print("It's a draw")
    else :
        if (userSign == 0 and computerChoice==1) or (userSign == 1 and computerChoice == 2) or (userSign == 2 and computerChoice == 0):
            print("You lose!")
        elif (userSign == 0 and computerChoice == 2) or (userSign == 1 and computerChoice == 0) or (userSign == 2 and computerChoice == 1):
            print("You win!")
