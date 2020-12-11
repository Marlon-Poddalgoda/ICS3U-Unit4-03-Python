#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program calculates the square of all positive integers
#       between 0 and a user input


def main():
    # this function will calculate the square of all positive
    #      integers between 0 and a user input

    print("This program calculates the square of all positive integers"
          " between 0 and a user input.")

    # loop counter variable
    loop_counter = 0

    # square of positive integers variable
    square_num = 0

    # input
    user_input = input("Enter a positive integer: ")
    print("")

    # process
    try:
        user_input_int = int(user_input)

        if user_input_int >= 0:
            # loop statement
            for loop_counter in range(user_input_int + 1):
                square_num = loop_counter**2
                print("{0}² = {1}".format(loop_counter, square_num))
        else:
            # output
            print("{} is not a positive integer!"
                  .format(user_input_int))
    except Exception:
        # output
        print("That's not a number! Try again.")
    finally:
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
