import random
import time

print("🤖 Welcome to Smart Number Hunter!")
print("I will try to understand your guessing style.\n")

name = input("Enter your name: ")

secret = random.randint(1, 100)
attempts = 0
history = []

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("❌ Please enter a number.")
        continue

    attempts += 1
    history.append(guess)

    if guess < secret:
        print("📈 Too Low!")

    elif guess > secret:
        print("📉 Too High!")

    else:
        print("\n🎯 You found it!")
        print(f"Player: {name}")
        print(f"Secret number: {secret}")
        print(f"Attempts: {attempts}")

        # Analyze player's guessing style
        if len(history) >= 2:
            changes = []

            for i in range(1, len(history)):
                changes.append(history[i] - history[i - 1])

            average_change = sum(changes) / len(changes)

            print("\n🧠 Your Guessing Analysis:")

            if average_change > 10:
                print("You tend to make BIG jumps.")
            elif average_change < -10:
                print("You tend to move down quickly.")
            else:
                print("You usually make small adjustments.")

        print("\nYour guesses:")
        print(history)

        break

print("\n🤖 Game completed!")