my_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
my_str = my_str.casefold()

# count the vowels
count = {x:sum([1 for char in my_str if char == x]) for x in 'aeiou'}

print(count)
