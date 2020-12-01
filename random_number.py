#!/usr/bin/env python3
# Created by: Roman Cernetchi
# Created on: November 2020
# This program checks if a person chose the right number between 1 and 100

import random


def main():
    # This function checks if the person chose right or wrong

    # Input

    chosen_number = int(input("Enter a number between 0 and 9: "))
    generated_number = random.randint(0, 9)  # A number between 0 and 9
    print("")

    # process
    if chosen_number == generated_number:
        # Output
        print("Correct!")

    else:
        print("The correct number is {}".format(generated_number))


if __name__ == "__main__":
    main()
