def get_permutation(string, i=0):
    if i == len(string):
        print("".join(string))
        return  # Added return to stop further recursion

    for j in range(i, len(string)):
        # swap
        string[i], string[j] = string[j], string[i]
        
        get_permutation(string, i + 1)
        
        # backtrack to the original state
        string[i], string[j] = string[j], string[i]

get_permutation(list("yes"))
