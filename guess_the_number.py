import random
from typing import SupportsComplex


rnumber = random.randint(1, 10)

guess = 0
YourNo = None
while YourNo != rnumber:

    YourNo = int(input("Enter the number:"))

    guess += 1

    if rnumber == YourNo:
        print("Congrats You Win!!!, You chose right number")
        print(guess)

    elif rnumber < YourNo:
        print("You chose Big number, please chose small")

    elif rnumber > YourNo:
        print("You chose smaller number please chose bigg")


print(f"You guess the number in {guess} guesses")

score=guess
with open('highscore_guess_the_No.txt') as f:
        highscore=int(f.read())

if highscore>score:
        with open('highscore_guess_the_No.txt','w') as f:
                f.write(str(score))
# with open('highscore_guess_the_No.txt','w') as h:
#     h.write('34')
  