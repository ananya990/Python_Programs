# Original list containing nested lists
my_list = [[1], [2, 3], [4, 5, 6, 7]]

# Using list comprehension to flatten the nested list
flat_list = [num for sublist in my_list for num in sublist]

# Printing the flattened list
print(flat_list)
