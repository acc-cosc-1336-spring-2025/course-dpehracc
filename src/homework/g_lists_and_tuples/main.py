#
from lists import get_lowest_list_value, get_highest_list_value

def main():
    while True:
        print("\n1 - Show the list low/high values")
        print("2 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            numbers = []
            while True:
                try:
                    num = float(input("Enter a value: "))
                    numbers.append(num)

                    if len(numbers) >= 3:
                        again = input("Do you want to enter another value? (y/n): ")
                        if again.lower() != 'y':
                            break
                except ValueError:
                    print("Please enter a valid number.")

            print("Lowest value:", get_lowest_list_value(numbers))
            print("Highest value:", get_highest_list_value(numbers))

        elif choice == "2":
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()