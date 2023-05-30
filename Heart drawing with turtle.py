# Importing the turtle library for graphics
import turtle
# Importing the time library for adding a delay
import time

# Defining a function to draw a heart shape using the turtle library


def draw_heart():

    # Creating a turtle object
    pen = turtle.Turtle()

    # Defining a nested function to draw a curved line
    def curve():
        for i in range(200):
            pen.right(1)
            pen.forward(1)

    # Defining a nested function to draw the overall heart shape
    def heart():

        # Setting the fill color to red
        pen.fillcolor('red')

        pen.begin_fill()

        pen.left(140)
        pen.forward(113)

        curve()
        pen.left(120)

        curve()

        pen.forward(112)

        pen.end_fill()

    # Defining a nested function to write the text 'I LOVE YOU' on the heart
    def write_text():

        pen.up()

        # Setting the position of the turtle to write the text
        pen.setpos(-68, 95)
        pen.down()

        pen.color('black')

        # Writing the text on the heart shape with specific font size and style
        pen.write('I LOVE YOU', font=("Verdana", 16, "bold"))

    # Calling the heart function to draw the heart shape
    heart()

    # Calling the write_text function to write the text on the heart
    write_text()

    # Hiding the turtle object after drawing the heart
    pen.ht()

    # Adding a delay of 5 seconds before closing the turtle window using the bye() function
    time.sleep(5)
    turtle.bye()


# Calling the draw_heart function to run the program
draw_heart()
