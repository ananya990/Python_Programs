# Initialize a variable to count the occurrences of the character
count = 0

# The string in which we want to search for the character
my_string = "python program"

# The character we want to count occurrences of
my_char = "p"

# Iterate over each character in the string
for i in my_string:
    # Check if the current character matches the character we're looking for
    if i == my_char:
        # If it matches, increment the count
        count += 1

# Print the total count of occurrences of the character
print(count)
