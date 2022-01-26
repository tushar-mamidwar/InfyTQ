"""

Write a program to create the following pattern:
(tyrtle program to draw three consecutive circles with different colours)
"""
import turtle

wn = turtle.Screen()  # creates a graphics window
wn.setup(500, 500)  # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")  # alex looks like a turtle

"""
alex.color("black")    # alex has a color
alex.right(60)         # alex turns 60 degrees right
alex.left(60)          # alex turns 60 degrees left
alex.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,3):
    alex.circle(20*counter)
"""

# Write the logic to create the given pattern
# Refer the statements given above to draw the patter
colours = ("green", "red", "blue")
for colour in colours:
    alex.color(colour)
    for counter in range(1, 4):
        alex.circle(20 * counter)
    alex.left(120)
