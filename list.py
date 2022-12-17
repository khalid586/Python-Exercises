items = ["bread", "pasta", "milk", "choco"]
mylist = ["soap", "shampoo", "soda"]
print(items[0])
print(items)
items[0] = "rice"
print(items)
print(items[:2])  # from beginning to 1(before 2)
print(items[2:])  # print from index 2 till the last index
items.append("vegetable")  # adds vegetable at the end of the list
print(items)
items.insert(2, "butter")  # inserts butter at index 2
items += mylist  # we can add another list inside a list (combine two lists) .
print(items)
print(len(items))  # length of the list
print("butter" in items)  # checks whether an item is present or not in list
print("cola" in items)

# we can delete item from a list by below mentioned techniques
del items[0]
print(items)

items = [ele for ele in items if ele != "milk"]
print(items)
items.remove("vegetable")
items.pop(3)  # remove item at index 3
print(items)
# Exercise - 1
# Let us say your expense for every month are listed below,
#
# January - 2200
#
# February - 2350
#
# March - 2600
#
# April - 2130
#
# May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list



# Exercise - 2
# You have a list of your favourite marvel super heros.
#
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
#
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available
# in list)
