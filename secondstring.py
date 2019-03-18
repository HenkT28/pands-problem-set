# Henk Tjalsma, 2019
# Solution to problem 6 - secondstring.py script
# Write a program that takes a user input string and outputs every second word.
# https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word
# https://www.pythoncentral.io/cutting-and-slicing-strings-in-python/
# https://stackoverflow.com/questions/509211/understanding-slice-notation

# Enter the user input string
sentenceInput=(input("Please enter sentence: "))

# string = 'The quick brown fox jumps over the lazy dog.'
# every_second_word = sentenceInput.split(' ')[::2]

# You split the original string using spaces, then you take every other word from it with the [::2] splice.
every_second_word = sentenceInput.split(' ')
print(every_second_word[::2])