
import random

from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays snowman and guessed letters.
    """

    header_title = "❄️  Snowman Meltdown Game  ❄️"
    # Header
    print("=" * 75)
    print(f"{header_title:.^75}")
    print("=" * 75)

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
    print("✏️ Guessed letters: ", " ".join(sorted(guessed_letters)))


def continue_game():
    """
    Ask users if they want to play again.
    :return: True
    """
    while True:
        answer = input("\nDo you want to play again? (y-n) ").lower()
        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            print("\n 🤗Thank you for playing")
            exit()
        else:
            print("Invalid input! (y-n)")



def play_game():
    """
    Initial game setup, and checking whether the answer is correct or incorrect.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistake = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    # For now, display the initial game state.
    while mistakes < max_mistake:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").lower()

        # Validate Input
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
            print("\n 🥳 Congratulations! You saved the snowman!")

            if continue_game():
                play_game()

    # If we get here, even the hat will melt.
    display_game_state(mistakes , secret_word, guessed_letters)
    print("\n💧 The snowman has completely melted!")
    print("🫥 The word was:", secret_word)

    if continue_game():
        play_game()


if __name__ == "__main__":
    play_game()