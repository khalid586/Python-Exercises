india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Exercise i
found = 0
city = input()
if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in pakistan")
elif city in bangladesh:
    print(f"{city} is in bangladesh")
else:
    print(f"{city} doesn't belong to any of these countries")
# Exercise ii

cityName1 = input("Enter two city name 1 : ")
cityName2 = input("Enter two city name 2 : ")
if cityName1 and cityName2 in bangladesh or cityName1 and cityName2 in india or cityName1 and cityName2 in pakistan:
    print("Both cities belong to same country")
else:
    print("Both cities doesn't belong to same country")
