# Importing the permutations function from the itertools module
from itertools import permutations

# Define a list of characters
chars = 'pro'

# Generating permutations of the characters in the list
# Each permutation is converted into a string and added to the list 'words'
words = [''.join(p) for p in permutations(chars)]

# Printing the list of permutations
print(words)
