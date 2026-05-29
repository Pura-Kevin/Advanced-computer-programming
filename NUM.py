import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 6
        guess = None

        print(f"\nYou have {max_attempts} attempts to guess the number.")

        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (1-100): "))

                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue

                attempts += 1

                if guess == secret_number:
                    print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                    break
                elif guess < secret_number:
                    print("Too low! Try a higher number.")
                else:
                    print("Too high! Try a lower number.")

            except ValueError:
                print("Invalid input! Please enter a valid number.")

        if guess != secret_number:
            print(f"\nGame Over! The number was {secret_number}.")
            print("You've used all your attempts.")

        while True:
            play_again = input(f"\nWould you like to play again? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y']:
                print("\n" + "=" * 50)
                break
            elif play_again in ['no', 'n']:
                print("Thanks for playing! Goodbye!")
                return
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    number_guessing_game()