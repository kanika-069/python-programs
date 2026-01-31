#ROCK PAPER SCISSORS GAME
import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice1=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice1==0:
    print(rock)
    choice2=random.randint(0,2)
    if choice2==0:
        print("Computer chose :\n",rock)
        print("\nDraw")
    elif choice2==1:
        print("Computer chose :\n",paper)
        print("\nYou Lose.")
    else:
        print("Computer chose :\n",scissors)
        print("\nYou Won.")
elif choice1==1:
    print(paper)
    choice2=random.randint(0,2)
    if choice2==0:
        print("Computer chose :\n",rock)
        print("\nYou Won.")
    elif choice2==1:
        print("Computer chose :\n",paper)
        print("\nDraw.")
    else:
        print("Computer chose :\n",scissors)
        print("\nYou Lose.")
elif choice1==2:
    print(scissors)
    choice2=random.randint(0,2)
    if choice2==0:
        print("Computer chose :\n",rock)
        print("\nYou Lose.")
    elif choice2==1:
        print("Computer chose :\n",paper)
        print("\nYou Won.")
    else:
        print("Computer chose :\n",scissors)
        print("\nDraw.")
else:
    print("Invalid Choice.")