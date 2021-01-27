# -------------------------------------------------------
#. Engineering Class - Woodberry Forest
#. VIjay Krishnan.   Python Assignment #2 - Turtle
#
# Sample program to draw different objects
# -------------------------------------------------------
import turtle
#----------------differnt functions to draw differnt shapes -----
def draw_square ():
    print ("printing square")
    turtle.shape("turtle")
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    print ("enter to continue")
    input ()
def draw_triangle ():
    print ("printing Triangle")
    
def draw_circle ():
    print ("printing circle")
def draw_star ():
    print ("printing star")


#---------------------------------------------------------------
print("----- Draw different Shapes ----")
print("""
Square         - Press 1 Triangle    - Press 2
Circle         - Press 3 xx        - Press 4
Exit           - Press 0
""")
input_number = input()

if not input_number == "0":
    #Getting the first number and converting from string to int
    print("\nEnter number 1: ", end=" ")
    num1 = int(input())
    if input_number == "1": 
        print(f"\nprint sequre")
        draw_square ()
    elif input_number == "2": 
        print(f"\nprint triangle")
        draw_triangle ()
    elif input_number == "3": 
        print(f"\nprint circle 3")
        draw_circle ()
    elif input_number == "4": 
        print(f"\nprint triangle4")
        draw_star ()
    else:
        print("\nYou did not enter option 1, 2, 3 or 4")
else:
    print("\n---------------------------------------------\n")

