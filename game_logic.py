
import random

from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word)
    print("✏️ Guessed letters:", " ".join(sorted(guessed_letters)))
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistake = len(STAGES)

    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.

    while mistakes < max_mistake:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").lower()


        if not guess.isalpha() or len(guess) != 1:
            print("🤬 Enter a single valid letter.\n")
            continue

        # checks for wrong repeated letters.
        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print(f"OOPS! '{guess}' is not in the word.\n")

        answer = all([letter in guessed_letters for letter in secret_word])
        if answer:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("🥳 Congratulations! You saved the snowman!")
            return

    # If we get here, even the hat will melt.
    display_game_state(mistakes - 1, secret_word, guessed_letters)
    print("💧 The snowman has completely melted!")
    print("🫥 The word was:", secret_word)


if __name__ == "__main__":
    play_game()