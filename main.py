
"""NUMBER GUESSING GAME"""

import random


# Function to get a valid integer from the user
def get_number(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            return value
        except ValueError:
            print("Please enter a valid number.")


# Function to make sure user only enters 'y' or 'n'
def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y" or answer == "n":
            return answer
        else:
            print("Enter only 'y' or 'n'.")


# Function that runs one round of the game
def play_game():

    # Ask for range
    low = get_number("Enter the LOW number: ")
    high = get_number("Enter the HIGH number: ")

    # Make sure high is greater than low
    while high <= low:
        print("High number must be greater than low number.")
        high = get_number("Enter a new HIGH number: ")

    # Ask for number of attempts
    attempts = get_number("How many attempts would you like? ")

    # Generate random number in range
    secret_number = random.randint(low, high)

    print(f"\nI picked a number between {low} and {high}.")

    count = 0

    # Loop for guesses
    while count < attempts:
        guess = get_number("Enter your guess: ")
        count += 1

        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"You guessed it in {count} tries!")
            return  # End the round if correct

        print(f"Attempts used: {count}/{attempts}")

    # If they run out of attempts
    print("You ran out of attempts.")
    print(f"The number was {secret_number}.")


# Main program
def main():

    # Ask for name and greet user
    name = input("What is your name? ").strip()
    print(f"Hello, {name}! Welcome to the game.")

    while True:
        play_game()

        # Ask to play again
        again = get_yes_no("Do you want to play again? (y/n): ")

        if again == "n":
            print("Thanks for playing!")
            break


# Run the program
main()
