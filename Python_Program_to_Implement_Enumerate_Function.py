fruits = ["apple" , "mango" , "orange" , "kiwi"]

# Loop over an enumerate object
for item in enumerate(fruits):
  print(item)
print()
"""This part of the code iterates over the fruits list using enumerate(fruits). 
The enumerate() function returns tuples where the first element is the index, 
and the second element is the corresponding item in the sequence."""

# Loop over an enumerate object with separate index and item variables
for count, item in enumerate(fruits):
  print(count, item)
print()
"""This part of the code is similar to the previous one, but it unpacks the tuple into count 
and item variables during each iteration and displays it."""

# Change the default counter and loop over an enumerate object
for count, item in enumerate(fruits, 100):
  print(count, item)
"""In this part, the enumerate() function is used with an additional argument (100), 
specifying the starting index for the enumeration. By providing 100 as the second argument to enumerate(), 
the index starts from 100, not the default 0."""
