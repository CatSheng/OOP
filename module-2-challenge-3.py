# This code will take a month inputted by the user and 
# let the user know how many days are in that month. 

# month holds the spot for what the user inputs
month = input("Input a month: \n")
# This converts all the letters in the word the user inputted to lowercase
month = month.lower()
# If the month that they inputted matches with one of these options, 
# the computer will tell the user how many days are in that month.
if month == 'january':
    print("There are 31 days in January.")
elif month == 'february':
    print("There are 28 or 29 days in February.")
elif month == 'march':
    print("There are 31 days in March.")
elif month == 'april':
    print("There are 30 days in April.")
elif month == 'may':
    print("There are 31 days in May.")
elif month == 'june':
    print("There are 30 days in June.")
elif month == 'july':
    print("There are 31 days in July.")
elif month == 'august':
    print("There are 31 days in August.")
elif month == 'september':
    print("There are 30 days in September.")
elif month == 'october':
    print("There are 31 days in October.")
elif month == 'november':
    print("There are 30 days in November.")
elif month == 'december':
    print("There are 31 days in December.")
# If the user does not input a month or spells it wrong, the following will be shown: 
else:
    print("That is not a month.")


