import random
import requests

# Word lists categorized by difficulty with categories
words = {
    'fruits': ['apple', 'banana', 'grape', 'orange', 'melon'],
    'animals': ['tiger', 'elephant', 'giraffe', 'dolphin', 'penguin'],
    'instruments': ['guitar', 'piano', 'trumpet', 'violin', 'drums']
}

# Initialize performance metrics
games_played = 0
games_won = 0
total_guesses = 0
correct_guesses = 0

# Define hint types
hint_types = ['Reveal a letter', 'Category hint', 'Word definition']

def select_word():
    """Selects a word and category randomly from the word list."""
    category = random.choice(list(words.keys()))
    word = random.choice(words[category]).lower()
    return word, category

def display_hangman(tries):
    stages = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def get_word_definition(word):
    """Fetch the word definition from an online dictionary API (if available)."""
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code == 200:
            data = response.json()
            if len(data) > 0 and "meanings" in data[0]:
                definition = data[0]["meanings"][0]["definitions"][0]["definition"]
                return definition
    except Exception as e:
        print(f"Error fetching definition: {e}")
    return "Definition not available."

def offer_hint(word, word_completion, category):
    """Offers a hint based on the player's choice."""
    print("Choose a hint:")
    for i, hint in enumerate(hint_types, 1):
        print(f"{i}. {hint}")

    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        # Reveal a random letter
        remaining_letters = [letter for letter in word if letter not in word_completion]
        if remaining_letters:
            hint_letter = random.choice(remaining_letters)
            print(f"Hint: The letter '{hint_letter}' is in the word.")
        else:
            print("No more letters to reveal!")
    elif choice == '2':
        # Provide the category hint
        print(f"Hint: The word is a type of {category}.")
    elif choice == '3':
        # Provide the word definition
        definition = get_word_definition(word)
        print(f"Hint: Definition of the word - {definition}")
    else:
        print("Invalid choice!")

def play_game():
    global games_played, games_won, total_guesses, correct_guesses

    word, category = select_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word (or type 'hint' for a hint): ").lower()
        total_guesses += 1

        if guess == "hint":
            offer_hint(word, word_completion, category)
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                correct_guesses += 1
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    games_played += 1

    if guessed:
        print("Congrats, you guessed the word! You win!")
        games_won += 1
    else:
        print(f"Sorry, you ran out of tries. The word was '{word}'. Maybe next time!")

    print(f"Games played: {games_played}, Games won: {games_won}")

# Run the game
play_game()
