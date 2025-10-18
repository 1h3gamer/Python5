import random
playing = True
number = str(random.randint(0,100))

print("I will generate a random number from 0 to 100 and you have to guess the number one digit at a time")
print("The game ends when you get one answer correct")

while playing:
    guess = input("Give your best guess \n")
    if number == guess:
        print("You win the game")
        print("The number was ", number)
        break
    else:
        print("Your guess isn't quite right.Try again!")