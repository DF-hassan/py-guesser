import random

range_top = input("Please enter a number : ")

if range_top.isdigit():
    range_top = int(range_top)
    if range_top <= 0:
        print("Please Enter a Number Greater Than 0 next Time")
        quit()
else:
    print("Please Ener a Number!")
    quit()

random_number = random.randint(0, range_top)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Enter a Number Next Time!")
        continue
    
    if user_guess == random_number:
        print("You Got it :) ********************")
        break
    elif user_guess > random_number:
        print("You Were aBove The Number!")
    else:
        print("You Were Below The Number!")

print(f"You Got it in {guesses} Quesses")