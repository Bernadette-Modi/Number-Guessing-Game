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
