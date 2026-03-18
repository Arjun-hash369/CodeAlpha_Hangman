import random

# Predefined list of 5 words
words = ["apple", "chair", "tiger", "plant", "bread"]

# Select random word
word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman Game!")

# Display blanks
print("_ " * len(word))

# Game loop
while incorrect_guesses < max_attempts:
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")

    # Display word progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check win condition
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 You Win! The word was:", word)
        break

# Lose condition
if incorrect_guesses == max_attempts:
    print("\n💀 You Lose! The word was:", word)