india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Exercise i
# found = 0
# cityName = input()
# for name in india:
#     if name == cityName:
#         found = 1
#         print("This city belongs to india")
# for name in pakistan:
#     if name == cityName:
#         found = 1
#         print("This city belongs to pakistan")
# for name in bangladesh:
#     if name == cityName:
#         found = 1
#         print("This city belongs to bangladesh")
#
# if found == 0:
#     print("City doesn't belong any of these three countries")

# Exercise ii
found = 0
done = 0
cityName = input("Enter two city names separated by space : ").split(" ")

for name in india:
    for givenName in cityName:
        if givenName == name:
            found += 1
if found == 2:
    print("Both city belongs to the same country")
    done = 1
found = 0
for name in pakistan:
    for givenName in cityName:
        if givenName == name:
            found += 1
if found == 2:
    print("Both city belongs to the same country")
    done = 1
found = 0
for name in bangladesh:
    for givenName in cityName:
        if givenName == name:
            found += 1
if found == 2:
    print("Both city belongs to the same country")
    done = 1

if done == 0:
    print("Both cities are not from same country")