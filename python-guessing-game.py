import random

print("Hi there! What's your name?")
name = input()

print("Hi " + name + " I'm thinking about a number between 1 and 20.")

randNum = random.randint(1, 20)

for guessTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    
    if guess > randNum:
        print("Hmmmm your number is to high.")
    elif guess < randNum:
       print("Hmmmm your number is to low.")
    else:
       break
if guess == randNum:
    print("Great, " + name + ". You guessed my number in the " + str(guessTaken) + " guesses.")
else:
    print("Nop, you ran out of tries. My number was " + str(randNum) + ".")


