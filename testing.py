def editor(sentence):
    """This function takes all the words in a sentence and divides them up into a list of words"""
    # newSentence is an empty list
    newSentence = []
    # word is an empty string
    word = ''
    # iterating through each character in the sentence
    for character in sentence:
        # if the character is a space, append the word to the empty list: newSentence
        if character == ' ':
            newSentence.append(word)
            word = ''
        # If the character is not a space, add the character to the empty string: word
        else:
            word += character
    return newSentence

finalAnswer = editor("Mary had a little duck.")
print(finalAnswer)

# Output: ['Mary', 'had', 'a', 'little']