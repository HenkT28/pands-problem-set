# Henk Tjalsma, 2019
# Solution to problem 6 - secondstring.py script
# Write a program that takes a user input string and outputs every second word.

# https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word
# https://www.pythoncentral.io/cutting-and-slicing-strings-in-python/
# https://stackoverflow.com/questions/509211/understanding-slice-notation
# https://docs.python.org/2.3/whatsnew/section-slices.html
# https://stackoverflow.com/questions/3453085/what-is-double-colon-in-python-when-subscripting-sequences

# Enter the user input string
sentenceInput=(input("Please enter sentence: "))

# Example string = 'The quick brown fox jumps over the lazy dog.'
# Extract the elements -> every_second_word = sentenceInput.split(' ')[::2]
# seq[::n] is a sequence of each n-th item in the entire sequence.

# You split the original string using spaces, then you take every other word from it with this [::2] 
every_second_word = sentenceInput.split(' ')
print(every_second_word[::2])