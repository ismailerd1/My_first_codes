import random

number = random.randint(1, 100)

myguess = None
pretictCount = 0

try:
    myguess = int(input("Guess a number between 1 and 100:"))
except TypeError:
    print("TypeError!")
    print("Your guess must be a number!!")
    try: myguess = int(input("Guess a number between 1 and 100:"))
    except Exception:
        print("You can't play it anymore!")
except ValueError:
    print("ValueError!")
    print("Your guess must be a number!!")
    try: myguess = int(input("Guess a number between 1 and 100:"))
    except Exception:
        print("You can't play it anymore!")

while myguess!= number and pretictCount <7 and myguess != number :
    if myguess > number:
        print("Too high!Choose lower")
        pretictCount += 1
        myguess = int(input("Guess again:"))

    elif myguess < number:
        print("Too low!Choose higher")
        pretictCount += 1
        myguess = int(input("Guess again:"))

if myguess == number:
    print("Congratulations!You guessed right!")

if pretictCount >=7:
    print("You lose!!")
