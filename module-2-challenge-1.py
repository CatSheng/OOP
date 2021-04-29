# This code takes in an integer from the user. Repeats 
# back the number, and informs the user if it is even or odd.

# wholeNumber saves the spot of the input the user gave the computer
wholeNumber = int(input("Please enter a whole number: \n"))
# Repeats back to the user what the number they inputted.
print("Your number is ")
print(wholeNumber)
# If the number is divisible by 2 and gives a remainder of 0, it will print out even.
if (wholeNumber % 2) == 0:
    print("Your number is an even number.")
# If the number does not give a remainder of 0, it will print out odd.
else:
    print("Your number is an odd number.")
