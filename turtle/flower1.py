import turtle


def draw_square(square_d):
    for i in range(1,5):
        square_d.forward(150)
        square_d.right(90)

def draw_tri(triange_dr):
    for j in range(1,4):
        triange_dr.forward(90)
        triange_dr.right(120)


def draw():
    window = turtle.Screen()
    window.bgcolor("skyblue")

    # draw square
    rupesh = turtle.Turtle()
    rupesh.color("yellow")
    rupesh.shape("turtle")
    rupesh.speed(50)
    for i in range(1,77):
        draw_square(rupesh)
        rupesh.right(5)

    # draw circle
    uday = turtle.Turtle()
    uday.color("blue")
    uday.shape("circle")
    uday.speed(50)
    for k in range(1, 37):
        uday.circle(70)
        uday.right(10)



    # draw triangle
    raju =  turtle.Turtle()
    raju.color("red")
    raju.shape("triangle")
    raju.speed(50)

    for j in range(1, 37):
        draw_tri(raju)
        raju.right(10)


    line = turtle.Turtle()
    line.shape("circle")
    line.right(90)
    line.forward(300)

    window.exitonclick()



draw()