import random

print("Computers turn Rock(r) Paper(p) Scissors(s)?")

def gamesys(comp ,you):
 if comp == you:
    return None

 elif comp == 'r':
    if you == 's':
        return False
    elif you == 'p':
        return True

 elif comp == 'p':
    if you == 'r':
        return False
    elif you == 's':
        return True

 elif comp == 's':
    if you == 'p':
        return False
    elif you == 'r':
        return True

b = random.randint(1,3)
if b == 1:
    comp = 'r'
elif b == 2:
    comp = 'p'
elif b == 3:
    comp = 's'

you = input("Your Turn! Choose one Rock(r) Paper(p) Scissors(s)?")


print(f"Computer Chose : {comp}")
print(f"You Chose : {you}")

c = gamesys(comp, you)

if c == None:
    print("Its an Tie")
elif c :
    print("You Win!")
else :
    print("You Lose!")