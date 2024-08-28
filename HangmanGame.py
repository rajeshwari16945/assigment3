import random

def get_word():
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'developer']
    return random.choice(words)

def display_current_progress(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = get_word()
    guessed_letters = set()
    attempts = 6  # Number of allowed wrong guesses
    wrong_guesses = 0
    
    print("Welcome to Hangman!")
    print(display_current_progress(word, guessed_letters))
    
    while wrong_guesses < attempts:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("\nGood guess!")
        else:
            wrong_guesses += 1
            print(f"\nWrong guess! You have {attempts - wrong_guesses} attempts left.")

        current_progress = display_current_progress(word, guessed_letters)
        print(current_progress)
        
        if '_' not in current_progress:
            print("\nCongratulations! You've won!")
            break
    else:
        print(f"\nSorry, you've lost! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
