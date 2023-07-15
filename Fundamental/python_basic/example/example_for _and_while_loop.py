# TODO : example for  for loop and while loop
# Case 1
my_list = [2, 4, 6, 8, 3, 4, 5]
for item in my_list:
    print(item)

# Case 3:
i = 0
while i == len(my_list):
    print(i)

# Case 2:
while True:
    response = input("Enter you name:")
    if response == "vamsi":
        print("Okay")
    else:
        print("exit")
        break
