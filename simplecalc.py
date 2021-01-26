# -------------------------------------------------------
#. Engineering Class - Woodberry Forest
#. VIjay Krishnan.   Python Assignment #1 - Decision
#
# Sample program to demonstrate printing, basic match calculations
# -------------------------------------------------------
print("----- Simple calculator app ----")
print("\nWhat do you want to calculate?")
print("""
Addition       - Press 1 Subtraction    - Press 2
Multiplication - Press 3 Division       - Press 4
Exit           - Press 0
""")

input_number = input()

if not input_number == "0":
    #Getting the first number and converting from string to int
    print("\nEnter number 1: ", end=" ")
    num1 = int(input())

    #Getting the second number and converting from string to int
    print("\nEnter number 2: ", end=" ")
    num2 = int(input())

    if input_number == "1": 
        print(f"\nsum of {num1} and {num2} is {num1 + num2}")
    elif input_number == "2": 
        print(f"\ndiffe between {num1} and {num2} is {num1 - num2}")
    elif input_number == "3": 
        print(f"\nProduct of {num1} and {num2} is {num1 * num2}")
    elif input_number == "4": 
        print(f"\n{num1} div by {num2} is {num1 / num2}")
    else:
        print("\nYou did not enter option 1, 2, 3 or 4")
print("\n---------------------------------------------\n")