# Define a function named 'name'
def name():
    # Assign the value "John" to the variable 'n1'
    n1 = "Ananya"
    # Assign the value "Armin" to the variable 'n2'
    n2 = "Annie"

    # Return a dictionary with keys 1 and 2, and corresponding values n1 and n2
    return {1: n1, 2: n2}

# Call the 'name' function and store the result in the 'names' variable
names = name()

# Print the content of the 'names' variable
print(names)
