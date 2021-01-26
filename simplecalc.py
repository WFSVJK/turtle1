print("Hi! Welcome to the calculator")

print("\n\nWhat do you want to do?")
print("""
Addition - Press 1
Subtraction - Press 2
Multiplication - Press 3
Division - Press 4
Exit - Press 0
""")

#Getting the operation to be performed
operation = input().strip() #strip removes spaces before or after the input.

#Checking if user wants to exit
if not operation == "0":
    #Getting the first number and converting from string to int
    print("\nEnter number 1: ", end=" ")
    number_1 = int(input())

    #Getting the second number and converting from string to int
    print("\nEnter number 2: ", end=" ")
    number_2 = int(input())

    #Depending on user choice, we do the calculation and print the results
    if operation == "1":
        print(f"\nThe sum of {number_1} and {number_2} is {number_1 + number_2}")
    elif operation == "2":
        print(f"\nThe difference between {number_1} and {number_2} is {number_1 - number_2}")
    elif operation == "3":
        print((f"\nThe product of {number_1} and {number_2} is {number_1 * number_2}"))
    elif operation == "4":
        if not (number_2 == 0):
            print((f"\n{number_1} divided by {number_2} is {number_1 / number_2}"))
        else:
            print("You cannot divide a number by 0")
    else:
        print("\nYou did not enter option 1, 2, 3 or 4")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")