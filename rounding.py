#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Dec. 07, 2022
# This program gets a users decimal number and rounds it to how many digits the user inputs.
# Rounding function
def rounding(num_array, rounding_digits):
    num_array[0] = num_array[0] * (10**rounding_digits)
    num_array[0] += 0.5
    num_array[0] = int(num_array[0])
    num_array[0] = num_array[0] / (10**rounding_digits)


def main():
    # Adds users number to a list.
    num_user = []
    # Gets users decimal number and digits the user wants to round by.
    user_float = input("Please enter a number that you would like to be rounded: ")
    user_rounding = input("Please enter by how many digits you would like to round: ")
    try:
        # tries to convert users number to a float and digits to round by to an int.
        user_float = float(user_float)
        user_rounding = int(user_rounding)
        num_user.append(user_float)

    except ValueError:
        # Exception if user inputs a string.
        print("This program does not support strings (PLEASE ENTER A DECIMAL)")
        main()

    # function called for rounding.
    rounding(num_user, user_rounding)
    # displays new user number.
    print(f"{user_float} rounded by {user_rounding} digits is {num_user[0]}")


if __name__ == "__main__":
    main()
