import random

def guess_the_number():
    try:
        # Ask the user to set the upper limit N for the guessing range
        max_number = int(input("Set a maximum number of this game: "))
        if max_number < 1:
            print("Maximum number must be at least 1.")
            return

        # Randomly choose a secret number between 1 and max_number
        secret_number = random.randint(1, max_number)

        # Initialize the guessing range
        low = 1
        high = max_number

        # Start the guessing loop
        while True:
            try:
                # Prompt the user to guess within the current range
                guess_input = input(f"Guess a number between {low} and {high} until you get it right: ")
                
                # Try converting input to integer
                guess = int(guess_input)

                # Check if the guess is within the valid current range
                if guess < low or guess > high:
                    print(f"Please input a NUMBER between {low} and {high} !!!")
                    continue

                # Check if the guess is correct
                if guess == secret_number:
                    print("BOOM !!!")
                    print("Congrats ! You have ended the game ! 🍦 Here's your cream as present ^.^")
                    break
                else:
                    # Update the guessing range based on the guess
                    if guess < secret_number:
                        low = guess + 1
                    else:
                        high = guess - 1
                    print("The balloon is still being expanded… ")

            except ValueError:
                # If input is not a valid integer, show this message
                print(f"Please input a NUMBER between {low} and {high} !!!")

    except ValueError:
        print("Please enter a valid integer for the maximum number!")

# Run the game
guess_the_number()