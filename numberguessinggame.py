import random 
def get_difficulty():
    while True:
        print("\nSelect a difficulty level: ")
        print("1. Easy (10 chances)")
        print("2. Medium (7 chances)")
        print("3. Hard (5 chances)")
        choice = input("Enter 1, 2, 3: ").split()
        if choice == "1":
            return 10
        if choice == "2":
            return 7
        if choice == "3":
            return 5
        else: 
            print("Invalid input. Please select 1, 2, or 3.")

def main():
    print("Welcome to the Number Guessing Game!")
    print("Rules: The computer will randomly select a number between 1 too 100.")
    print("You will have a limited number of chances based on the difficulty level you choose.")

    target_number = random.randint(1, 100)
    chances = get_difficulty()
    print("\nGreat! I've selected a number between 1 and 100. Let's start!")
    print(f"You have {chances} chances to guess the number.")

    for attempt in range(1, chances + 1):
        try:
            guess = int(input(f"\Attempt {attempt}: Enter your guess: ").strip())
            if guess < 1 or guess > 100: 
                print("Please enter a number between 1 and 100.")
                continue
            if guess == target_number:
               print(f"\nCongratulations! You guessed the number {target_number} correct in {attempt} attempts.")
               break
            elif guess < target_number:
               print("Too high! Try a lower number.")
            else:
               print("Too high! Try a lower number.")
        except ValueError: 
            print("Invalid input. Please enter a valid number.")
            continue
    else:
        print(f"\nGame over! You've used all your chances. The correct number was {target_number}.")
if __name__ == "__main__":
    main()
    