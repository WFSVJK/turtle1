# -------------------------------------------------------
#. Engineering Class - Woodberry Forest
#. VIjay Krishnan.   Python Assignment #2 - Turtle
#
# Sample program to draw different objects
# -------------------------------------------------------
import turtle
#----------------differnt functions to draw differnt shapes -----
def draw_square ():
    turtle.shape("turtle")
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    print ("Check the Drawing ....hit Enter to continue")
    input ()
def draw_triangle ():
    print ("printing Triangle")
    turtle.shape("turtle")
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    print ("Check the Drawing ....hit Enter to continue")
    input ()

def draw_circle ():
    print ("printing circle")
    turtle.shape("turtle")
    turtle.pencolor('red')
    turtle.circle(70)
    input ()
    
def draw_star ():
    print ("printing star")
    for i in range(5):
        turtle.forward(150)
        turtle.right(144)
    print("Check the Drawing ....hit Enter to continue")
    input()



#---------------------------------------------------------------
print("\n----- Welcome to Vijay's TurtlePlay application ----")
print("----- Choose a Shape to draw ------------------------")
print("""
Square          - Press 1 
Triangle        - Press 2
Circle          - Press 3 
Star            - Press 4
Exit            - Press 0
""")
input_number = input()

if not input_number == "0":
    #Getting the first number and converting from string to int
    if input_number == "1": 
        print(f"\nprinting Square ....")
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

