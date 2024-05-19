"""The dateutil.parser module is particularly useful for parsing dates from 
strings in various formats without needing to specify the format explicitly."""

# Import the parser module from the dateutil package
from dateutil import parser

# Use the parse function to convert a date-time string into a datetime object
date_time = parser.parse("Mar 11 2011 11:31AM")

# Print the resulting datetime object to see the parsed date and time
print(date_time)

# Print the type of the date_time variable to confirm it's a datetime object
print(type(date_time))
