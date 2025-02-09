# Hangman Game in Python made by me

import random

# List of words for the game
words = ["dinosaur", "sky", "age", "spongebob", "pug", "car", "bomb", "rand", "cash", "team",]

def select_word(words):
    """Selects a random word from the list."""
    return random.choice(words)

def main():
    secret_word = select_word(words)
    guessed_letters = ""
    remaining_attempts = 10  # Initial attempts (head + body + arms + legs)

    print("Welcome to Hangman!")
    print(f"Guess the word with {remaining_attempts} attempts remaining.")

    while remaining_attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter try a different one.")
            continue

        guessed_letters += guess

        if guess not in secret_word:
            remaining_attempts -= 1
            print(f"Wrong! {remaining_attempts} attempts left.")
        else:
            print("Correct!")

        # Display the word with underscores for unguessed letters
        display_word = "".join([c if c in guessed_letters else "_" for c in secret_word])
        print(f"Word: {display_word}")

        if display_word == secret_word:
            print("Congratulations! You guessed the word.")
            break

    if remaining_attempts == 0:
        print(f"Sorry, you're out of attempts. The word was '{secret_word}'.")

if __name__ == "__main__":
    main()