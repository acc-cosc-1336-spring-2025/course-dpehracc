from repetition import get_factorial
from repetition import sum_odd_numbers

# Create menu
def main():
    while True:  
        print("\nHomework 3 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")

        choice = input("Select an option: ")

        if choice == "1":
            while True:
                try:
                    num = int(input("Enter a number (1-9): "))
                    if 1 <= num < 10:
                        break  
                    print("Invalid. Please enter a number between 1 and 9.")
                except ValueError:
                    print("Invalid. Please enter an integer.")

            result = get_factorial(num)
            print(f"The factorial is {result}")

        elif choice == "2":
            while True:
                try:
                    num = int(input("Enter a number (1-99): "))
                    if 1 <= num < 100:
                        break
                    print("Invalid. Please enter a number 1-99.")
                except ValueError:
                    print("Invalid. Please enter a digit 1-99.")

            result = sum_odd_numbers(num)
            print(f"Sum of odd numbers up to {num} is {result}")

        elif choice == "3":
            exit_choice = input("Exit program? (y/n): ").strip().lower()
            if exit_choice == "y":
                exit()

        else:
            print("Invalid. Please enter 1, 2, or 3.")

# Ask if the user wants to exit after each selection
        exit_choice = input("Do you want to exit? (y/n): ").strip().lower()
        if exit_choice == "y":
            print("Exiting program. Goodbye!")
            exit()

if __name__ == "__main__":
    main()
    