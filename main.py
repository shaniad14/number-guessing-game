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

 

