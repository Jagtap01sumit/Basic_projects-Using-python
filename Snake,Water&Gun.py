import random                         #import

print("snake(1) ,water(2), gun(3)?")
Your_choise = int(input("chose one of them :"))
if Your_choise == 1:
    print("Your chose snake!!")
elif Your_choise == 2:
    print("Your choise is water!!")
elif Your_choise == 3:
    print("Your choise is Gun")
else:
    print("Error, Chose Between 1,2 or 3 only !!!!")
comp = random.randint(1, 3)             #Random Number in 1,2,3
print(comp)
if comp == 1:
    print("computer's choise snake!!")
elif comp == 2:
    print("computer's choise is water!!")
elif comp == 3:
    print("computer's  choise is Gun")


if comp == Your_choise:
    print("Match Tie!!")
elif comp == 1 and Your_choise == 2:
    print("Yor lose!!")
elif comp == 2 and Your_choise == 1:
    print("Your win")
elif comp == 2 and Your_choise == 3:
    print("Your lose")
elif comp == 3 and Your_choise == 2:
    print("Your win!!")
elif comp == 3 and Your_choise == 1:
    print("Yor lose!!")
elif comp == 1 and Your_choise == 3:
    print("You lose")
