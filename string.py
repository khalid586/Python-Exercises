# this file contains example of strings in python
text = "ice cream"
print("this is 0 to 3: " + text[0:3])  # prints from 0th index to 2nd index not 3rd index
print("this is 4 to 9: " + text[4:9])  # prints from 4th index to 2nd index not 8th index (before 9th)
print("this is 4 to end: " + text[4:])   # prints from 4th index to the last index
print("this is beginning to 3: " + text[:3])   # prints from the beginning to 2nd (before 3rd)
# we can't make changes like text[3] = 'a' as we can do in cpp . It will give us error
text = '''this will store multiline 
string. To store multiline string we have to use triple quotes.'''
print(text)
first = "khalid"
second = "abdullah"
full_name = first + ' ' + second  # this is string concatenation
print(full_name)
