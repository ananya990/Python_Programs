index = [1, 2, 3, 4]
languages = ["Python", "Java", "Ruby", "C"]

# Using zip to combine index and languages into pairs
# and then converting them into a dictionary
dictionary = dict(zip(index, languages))
print(dictionary)
