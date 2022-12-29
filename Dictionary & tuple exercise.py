# # dict is similar to map and tuple is similar to pair in c++
# dictionary = {"tom": 1, "tommy": 2}
# print(dictionary)
# print(type(dictionary.items()))

# Exercise - 1:
# We have the following information on countries and their population (population is in cr),
#
# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# Using above create a dictionary of countries and its population
# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# add: if user input add then it should further ask for a country name to add. If country already exist
# in our dataset then it should print that it exist and do nothing.
# If it doesn't then it asks for population and add that new country/population in our dictionary and
# print it
# remove: when user inputs remove it should ask for a country to remove.
# If country exist in our dictionary then remove it and print new dictionary
# using format shown above in (a). Else print that country doesn't exist!
# query: on this again ask user for which country he or she wants to query.
# When user inputs that country it will print population of that country.

country = {"china": 143, "india": 136, "usa": 32, "pakistan": 21}
q = int(input("Enter the type of query you want to perform : 1 for printing the details , 2 for adding a country ,"
              " 3 for removing a country , 4 for a specific country: "))

if q == 1:
    for k, v in country.items():
        print(f"{k}==>{v}")
if q == 2:
    cntry = input("Enter the country to be added: ")
    if cntry in country:
        print("It already exists")
    else:
        val = int(input("Enter the population of the country: "))
        country[cntry] = val
        for k, v in country.items():
            print(f"{k}==>{v}")
if q == 3:
    cntry = input("Enter country to be deleted: ")
    if cntry in country:
        del country[cntry]
        for k, v in country.items():
            print(f"{k}==>{v}")
    else:
        print(f"{cntry} not found in the dictionary")
if q == 4:
    cntry = input("Enter country you want to check the population")
    if cntry in country:
        print(country[cntry])
    else:
        print("Invalid. It is not present")
