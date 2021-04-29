# This code takes in an integer from the user. Repeats back the
# number, and informs the user if it is even or odd.
# Comments in ALL CAPS are related to part 2 of Module 2 assignment,
# 'Improve One of Your Coding Challenges'.


# TRY/EXCEPT STATEMENT
try:
    # wholeNumber saves the spot of the input the user gave the computer
    wholeNumber = int(input("Please enter a whole number: \n"))
    # Repeats back to the user what the number they inputted.
    print(f"Your number is {wholeNumber}")

    # The number is divisible by 2 and a remainder of 0, print out even.
    if (wholeNumber % 2) == 0:
        print("Your number is an even number.\n")
    # If the number does not give a remainder of 0, print out odd.
    else:
        print("Your number is an odd number.\n")

    # COLLECTION OBJECTS/LISTS
    evenList = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    oddList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    evenOrOdd = input("Would you like to see a list of even or odd numbers? (even/odd)\n")
    evenOrOdd = evenOrOdd.lower()
    # TYPE TESTING
    # The 'isinstance' will check if the input is a string or not.
    if isinstance(evenOrOdd, str):
        # If the user picks even, print out the list of example even numbers.
        if evenOrOdd == 'even':
            print("This is an example of what even numbers are:")
            print(evenList)
        # If the user picks odd, print out the list of example odd numbers.
        elif evenOrOdd == 'odd':
            print("This is an example of what odd numbers are:")
            print(oddList)
        # If the user does not write out 'even' or 'odd'.
        else:
            print("Sorry, I can not compute the response.")
    # If the user somehow bypasses the input not being a string.
    else:
        print("That is not a string.")

    # MEMBERSHIP TESTING
    yesOrNo = input("\nWould you like to see if your number is in the example lists?\n").lower()
    if yesOrNo == 'yes':
        # The computer will check if the number is in the example lists.
        if wholeNumber in oddList or wholeNumber in evenList:
            print("Yeah! Your number was part of the example lists.")
        # If the number is not in the list, print out the following.
        else:
            print("Sorry, it was not part of the example lists. :(")
    # If the user does not want to check if their number is in the list.
    elif yesOrNo == 'no':
        print("Oh, okay. :(")
    # If the user writes something other than 'yes' or 'no'.
    else:
        print("Sorry, I can not compute the response.")

except ValueError:
    print("That is not an integer!")
