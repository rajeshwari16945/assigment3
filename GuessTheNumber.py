import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low. Try again.")
        elif guess > number_to_guess:
            print("Your guess is too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    guessing_game()
