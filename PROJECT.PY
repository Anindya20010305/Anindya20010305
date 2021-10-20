import random

#  Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose R
    elif comp == 'R':
        if you=='P':
            return True
        elif you=='S':
            return False
    
    # Check for all possibilities when computer chose P
    elif comp == 'P':
        if you=='S':
            return True
        elif you=='R':
            return False
    
    # Check for all possibilities when computer chose S
    elif comp == 'S':
        if you=='R':
            return True
        elif you=='P':
            return False

print("Comp Turn: Rock(R) Paper(P) or Siccor(S)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'R'
elif randNo == 2:
    comp = 'P'
elif randNo == 3:
    comp = 'S'

you = input("Your Turn: Rock(R) Paper(P) or Siccor(S)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")