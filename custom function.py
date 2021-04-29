# Calls the function at the bottom of the code. Sentence is hardcoded but
# can be changed in the code. the function splits the sentence into 
# a list of words removing the capitalization, commas, and spaces.
def editor(sentence):
    """This function takes words in a sentence and divides them into a list"""
    if isinstance(sentence, str):
        # Makes all the letters in sentence lowercase
        sentence = sentence.lower()
        # newSentence and trash are an empty list
        newSentence = []
        trash = []
        # word is an empty string
        word = ''
        # iterating through each character in the sentence
        if ' ' not in sentence:
            print("This is not a sentence. >:(")
        else:
            for character in sentence:
                # if the character is a space append the word to list
                if character == ' ':
                    newSentence.append(word)
                    word = ''
                # Takes all the commas and puts it in the trash list
                elif character == ',':
                    trash.append(character)
                # Character is not a space add the character to word
                else:
                    word += character
            # Taking each word created and putting it into the newSentence list
            if word:
                newSentence.append(word)
            return newSentence
    # If the user did not input a string
    else:
        print("That is not a string! >:(")
# Sentence is hard coded, needs to be changed to check for errors
finalAnswer = editor("I like dogs, however, I like cats better!")
if finalAnswer is not None:
    print(finalAnswer)
