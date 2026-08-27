import random

def guess_the_number():
    print("--- Welcome to the Number Guessing Game! ---")
    print("I am thinking of a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Take input from the user
            user_guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Check the user's guess against the secret number
            if user_guess < secret_number:
                print("Too low! Try a higher number.")
            elif user_guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()