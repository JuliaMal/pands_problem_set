# # Solution for Problem #6
# The program asks user to enter a sentence and outputs every second word.

# asks user to input a sentence 
sentence = input("Please input a sentence: ")

# counts words in string using split() function and takes every second word
for word in sentence.split()[::2]:
    # prints the results (every second word)
    print(word)