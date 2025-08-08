import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Cool Spirograph Design")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Set up color hue
hue = 0
n = 36  # Number of different colors
colors = [colorsys.hsv_to_rgb(i/n, 1, 1) for i in range(n)]

# Convert RGB to turtle-friendly format
colors = [(r*255, g*255, b*255) for r, g, b in colors]

# Use colormode 255 for RGB
turtle.colormode(255)

# Draw spirograph pattern
for i in range(360):
    pen.pencolor(colors[i % n])
    pen.circle(100)
    pen.left(10)
    pen.forward(2)

# Exit on click
screen.exitonclick()
