# # this file contains example of strings in python
# text = "ice cream"
# print("this is 0 to 3: " + text[0:3])  # prints from 0th index to 2nd index not 3rd index
# print("this is 4 to 9: " + text[4:9])  # prints from 4th index to 2nd index not 8th index (before 9th)
# print("this is 4 to end: " + text[4:])   # prints from 4th index to the last index
# print("this is beginning to 3: " + text[:3])   # prints from the beginning to 2nd (before 3rd)
# # we can't make changes like text[3] = 'a' as we can do in cpp . It will give us error
# text = '''this will store multiline
# string. To store multiline string we have to use triple quotes.'''
# print(text)
# first = "khalid"
# second = "abdullah"
# full_name = first + ' ' + second  # this is string concatenation
# print(full_name)
# Exercise of string
# Create 3 variables to store street, city and country, now create address variable to store entire address.
# Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in
# such a way that the street, city and country prints in a separate line
# Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index
# Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies
# and y fruits "
#  "daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
# I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement
# is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.

street = "khajaShamsuddin"
city = "Cumilla"
country = "Bangladesh"
address = street + '\n' + city + '\n' + country
print(address)
address = f"{street}\n{city}\n{country}"
print(address)
str = "Earth revolves around the sun"
print(str[6:14])
print(str[-3:])
fruits = 12
veggies = 15
print(f"I eat {veggies} veggies and {fruits} fruits daily")
s = 'maine 200 banana khaye'
s = s.replace('200', '10').replace('banana', 'samosa')
print(s)
