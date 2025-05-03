#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.homework.j_classes.class_a import Die

def main():
    die = Die()
    while True:
        input("Please press Enter to roll the die.")
        die.roll()
        print(die)
        again = input("Roll again? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()