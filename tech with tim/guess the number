'''
guess the number
'''
import random

top = input("enter the top range: ")

if top.isdigit():
    top = int(top)
else:
    print("enter a number pls..!")
    quit()


number = random.randint(0,top)
count = 0

while True:
    count += 1
    guess = input("enter the guess: ")
    
    
    if guess.isdigit():
        guess = int(guess)
    else:
        print("enter a number pls..!")
        count -= 1
        continue

    if guess == number:
        print("you got it..!")
        break
    elif guess > number:
        print("you are above it..!")
    else:
        print("you are below it..!")

print(f"you got it in {count} attempts")
