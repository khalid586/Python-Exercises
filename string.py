# this file contains example of strings in python
text = "ice cream"
print("this is 0 to 3: " + text[0:3])  # prints from 0th index to 2nd index not 3rd index
print("this is 4 to 9: " + text[4:9])  # prints from 4th index to 2nd index not 8th index (before 9th)
print("this is 4 to end: " + text[4:])   # prints from 4th index to the last index
print("this is beginning to 3: " + text[:3])   # prints from the beginning to 2nd (before 3rd)
