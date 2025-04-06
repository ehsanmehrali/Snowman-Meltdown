import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


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
    mistakes += 1
    print("Word: ", display_word)
    print("\n")
    return mistakes



def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistake = len(STAGES)
    print(secret_word)
    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.
    while mistakes < max_mistake:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)
        # print("You guessed:", guess)

        if guess not in secret_word:
            mistakes += 1
            print(f"OOPS! '{guess}' is not in the word.\n")

        answer = [letter in guessed_letters for letter in secret_word]
        if all(answer):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("🎉 Congratulations! You saved the snowman!")
            return


if __name__ == "__main__":
    play_game()