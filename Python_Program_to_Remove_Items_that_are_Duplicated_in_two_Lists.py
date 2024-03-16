# Define two lists
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

# Convert lists to sets and perform symmetric difference operation (^), 
# which returns elements that are present in either set, but not in both.
# Then, convert the result back to a list and print it.
print(list(set(list_1) ^ set(list_2)))
