# ============================================================
# TASK 1: Hangman Game
# CodeAlpha Python Programming Internship
# ============================================================

import random

# Predefined word list
WORDS = ["python", "hangman", "coding", "laptop", "github"]

# Hangman ASCII art stages (0 = full, 6 = empty)
HANGMAN_STAGES = [
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
       |
       |
       |
=========""",
    """
   -----
   |   |
       |
       |
       |
       |
=========""",
]

def display_state(guessed_letters, word, wrong_count):
    """Display current hangman stage, word progress, and guessed letters."""
    print(HANGMAN_STAGES[6 - wrong_count])
    print("\nWord: ", end="")
    for letter in word:
        print(letter if letter in guessed_letters else "_", end=" ")
    print()
    print(f"\nWrong guesses left: {6 - wrong_count}")
    print(f"Letters guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

def play_hangman():
    """Main game loop for Hangman."""
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("\n=============================")
    print("   Welcome to HANGMAN! 🎮")
    print("=============================")
    print(f"Guess the {len(word)}-letter word!\n")

    while wrong_guesses < max_wrong:
        display_state(guessed_letters, word, wrong_guesses)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 You WIN! The word was: '{word.upper()}'")
            break

        # Get player input
        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠  Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("⚠  You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ '{guess}' is in the word!")
        else:
            wrong_guesses += 1
            print(f"❌ '{guess}' is NOT in the word.")

    else:
        # Player lost
        display_state(guessed_letters, word, wrong_guesses)
        print(f"\n💀 Game Over! The word was: '{word.upper()}'")

    # Ask to play again
    again = input("\nPlay again? (yes/no): ").lower().strip()
    if again in ("yes", "y"):
        play_hangman()
    else:
        print("\nThanks for playing! Goodbye 👋")

if __name__ == "__main__":
    play_hangman()
