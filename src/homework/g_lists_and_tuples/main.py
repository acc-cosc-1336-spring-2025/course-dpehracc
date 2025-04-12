#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix

def main():
    dna_data = [
        ['T','T','T','C','C','A','T','T','T','A'],
        ['G','A','T','T','C','A','T','T','T','C'],
        ['T','T','T','C','C','A','T','T','T','T'],
        ['G','T','T','C','C','A','T','T','T','A']
    ]

    while True:
        print("\n1 - Get p distance matrix")
        print("2 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            matrix = get_p_distance_matrix(dna_data)
            for row in matrix:
                print(" ".join(f"{num:.5f}" for num in row))
        elif choice == "2":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()