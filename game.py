import random
print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")
number_to_guess = random.randrange(100)
chances = 7
guess_counter = 0
while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input('Please Enter your Guess : '))
    if my_guess == number_to_guess:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {guess_counter} tries.")
        break
    else:
        print("Incorrect guess.")
        if my_guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
if guess_counter == chances:
    print(f"Sorry, you've run out of chances. The number was {number_to_guess}")