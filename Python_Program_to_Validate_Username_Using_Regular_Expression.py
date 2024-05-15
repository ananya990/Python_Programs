""" Valid Username Points
- Start with an alphabetic character.
- Are between 8 and 30 characters long (inclusive).
- Contain only alphanumeric characters and underscores. """

import re

class UsernameValidator:
    regularExpression = r"^[a-zA-Z][a-zA-Z0-9_]{7,29}$"

if __name__ == "__main__":
    userName = input("Enter username : ").strip()

    if re.match(UsernameValidator.regularExpression, userName):
        print("Valid Username")
    else:
        print("Invalid Username")

""" Explanation
Regular expression : ^[a-zA-Z][a-zA-Z0-9_]{7,29}$
--> ^ : This asserts the start of the string, indicating that the pattern must begin at the start of the string.
--> [a-zA-Z]: This matches any alphabetic character, both lowercase and uppercase. It ensures that the username starts with an alphabetic character.
--> [a-zA-Z0-9_]{7,29}:
        - [a-zA-Z0-9_]: This matches any alphanumeric character or underscore.
        - {7,29}: This quantifier specifies that the previous character class (alphanumeric character or underscore) must occur between 7 and 29 times, inclusive. 
                  This ensures that the length of the username, after the initial alphabetic character, is between 8 and 30 characters inclusive.
                  
-->$: This asserts the end of the string, indicating that the pattern must end at the end of the string. """
