# india = ["mumbai", "bangalore", "chennai", "delhi"]
# pakistan = ["lahore", "karachi", "islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
#
# # Exercise i
# found = 0
# city = input()
# if city in india:
#     print(f"{city} is in india")
# elif city in pakistan:
#     print(f"{city} is in pakistan")
# elif city in bangladesh:
#     print(f"{city} is in bangladesh")
# else:
#     print(f"{city} doesn't belong to any of these countries")
# # Exercise ii
#
# cityName1 = input("Enter two city name 1 : ")
# cityName2 = input("Enter two city name 2 : ")
# if cityName1 and cityName2 in bangladesh or cityName1 and cityName2 in india or cityName1 and cityName2 in pakistan:
#     print("Both cities belong to same country")
# else:
#     print("Both cities doesn't belong to same country")
#
# # Exercise 2
# sugar = int(input())
#
# if sugar < 80:
#     print("Low sugar level")
# elif sugar > 100:
#     print("High sugar level")
# else:
#     print("Normal sugar level")

# Loop exercise
result = ["heads", "tails", "tails", "heads", "tails", "heads", "tails", "tails", "tails"]
headCnt = 0

for res in result:
    if res == "heads":
        headCnt += 1
print(f"The head count is  {headCnt}")

for i in range(1, 10, 2):
    print("i = ", i, ", i * i = ", i**2)
expense_list = [2340, 2500, 2100, 3100, 2980]
expense = int(input("Enter a amount : "))
found = 0
for i in range(len(expense_list)):
    if expense == expense_list[i]:
        found = 1
        print(f"The expense is found in month {i + 1}")
if found == 0:
    print(f"{expense} not found in the list")
for i in range(1, 6):
    ans = input("Are you tired?")
    if ans == "yes":
        print("You did not finished your race")
print("Congratulations on finishing the race")

for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end='')
    print()
