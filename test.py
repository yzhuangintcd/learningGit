import random

def roll_dice():
    # Simulate rolling a six-sided die
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")

    while True:
        input("Press Enter to roll the die...")

        # Roll the die and display the result
        result = roll_dice()
        print(f"You rolled: {result}")

        # Ask the user if they want to roll again
        play_again = input("Do you want to roll again? (yes/no): ").lower()

        if play_again != 'yes' or play_again != 'yeah' or play_again != 'yeahhhhh':
            print("Thanks for playing! Bye.")
            break

if __name__ == "__main__":
    main()
