# The user will input a letter from the alphabet and the 
# computer will let the user know if it is a vowel or a consonant. 

# letter takes place of what the user inputted
letter = input("Type in one alphabetical letter: \n")
# letter is being converted to lowercase, incase user puts in an uppercase letter
letter = letter.lower()
# If the letter is a, e, i, o, or u, the computer will print out it is a vowel.
if letter == 'a' or letter == 'e' or letter =='i' or letter =='o' or letter == 'u':
    print("You typed in a vowel.")
# If the letter is y, the computer will print out the following:
elif letter == 'y':
    print("You typed in 'y'. This letter is sometimes a vowel and sometimes a consonant.")
# If the letter inputted is not a, e, i, o, u, or y, it will print out it is a consonant. 
else:
    print("You typed in a consonant.")