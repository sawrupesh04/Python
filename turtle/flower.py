import turtle


def circle_dr():
    # for turtle window...........................................................
    window = turtle.Screen()
    window.bgcolor("skyblue")  # window background color..........................

    # draw circle.................................................................
    rupesh = turtle.Turtle()  # create instance
    rupesh.shape("circle")    # shape is your painter
    rupesh.speed(300)         # set speed to draw
    rupesh.right(50)          # set angle to right at 50 to start draw in at 50 degree
    # now draw the flower.........................................................
    for i in range(1,67):     # set the range of flower circle in one set of circle
        for j in range(1,5):  # set the range of how much circle want to draw to complete flower
            folwer(rupesh, i, "green") # function that perform action
            rupesh.right(90)  # rotate every flower circle at 90 degree to right
    rupesh.right(45)          # set ange of leaf handle
    rupesh.forward(200)       # set leaf handle distance
    rupesh.shape("circle")    # set leaf handle curser shape


    window.exitonclick()      # set click function when click on turtle window to exit
def folwer(circle, radius, color): # define function to perform action
    circle.color(color)       # call the function that set the color of flower
    circle.circle(radius)     # call the function that set the radius of flower

circle_dr()                   # call the main function that execute program


