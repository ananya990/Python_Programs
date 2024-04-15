import re

class MyRegex:
    def __init__(self):
        # Regular expression to validate an IP address
        self.pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

def main():
    my_regex = MyRegex()
    while True:
        try:
            # Input IP address from the user
            input_str = input()
            # Check if the input matches the regex pattern
            print(bool(re.match(my_regex.pattern, input_str)))
        except EOFError:
            break

if __name__ == "__main__":
    main()

""" Explaination
^: Asserts the start of the string.

( ... ){3}: Defines a group that is repeated exactly three times. This group captures each segment of the IP address (A.B.C.).

(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?): This part of the expression matches the first three segments of the IP address (A, B, and C). It allows for three possible cases:
-> 25[0-5]: Matches numbers from 250 to 255.
-> 2[0-4][0-9]: Matches numbers from 200 to 249.
-> [01]?[0-9][0-9]?: Matches numbers from 0 to 199. [01]? allows for an optional leading zero, and [0-9][0-9]? matches one or two digits.

\\.: Escaped period (dot), matches the period between each segment.

(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?): This part of the expression matches the fourth segment of the IP address(D).

$: Asserts the end of the string. """
