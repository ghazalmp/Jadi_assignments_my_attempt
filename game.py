# Guess_A_Number game


# Import the 'random' module to generate random numbers
import random

# Generate a random integer between 1 and 99 and store it in 'answer'
answer = random.randint(1, 99)

# Ask the user to input their name
name = input("Please insert your name: ")

# Greet the user by printing their name
print("Hello,", name)

# Ask the user for their initial guess and convert it to an integer
guess = int(input("Please insert your guess: "))

# Start a loop that continues until the user's guess matches the 'answer'
while guess != answer:
    # If the guess is greater than the answer, inform the user it's too high
    if guess > answer:
        print("Your guess is higher")
    # If the guess is less than the answer, inform the user it's too low
    else:
        print("Your guess is lower")
    
    # Ask the user to guess again
    guess = int(input("Please insert your guess: "))

# When the user guesses correctly, print a congratulatory message
print("Wowwwww!", name, "you did it, you have rocked.")
