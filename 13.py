import random
guess_number = random.randint(1,100)

while True:
    choice1 = int(input("Guess a number: "))
    
    if choice1 == guess_number:
        print("WOW!!! you guessed it correctly")
        break
    elif choice1 > guess_number:
        print("Too high")
    else:
        print("Too low")
