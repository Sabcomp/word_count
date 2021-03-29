text = input("What's on your mind today? ") # Takes input from the user

word_list = text.split()  # Creates a list of the words

print("oh nice, you just told me what's on your mind in " + str(len(word_list)) + " words!")  # len() function shows the number of elements in word-list
