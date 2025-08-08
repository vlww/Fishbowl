import turtle
import time
import colorsys
import os

# ASCII Art
ascii_art = r"""
  _____            _       _   _             
 |  __ \          | |     | | (_)            
 | |  | | ___  ___| |_ ___| |_ _  ___  _ __  
 | |  | |/ _ \/ __| __/ _ \ __| |/ _ \| '_ \ 
 | |__| |  __/\__ \ ||  __/ |_| | (_) | | | |
 |_____/ \___||___/\__\___|\__|_|\___/|_| |_|

        Turtle Art Showcase - Enjoy!
"""

print(ascii_art)
time.sleep(2)

# Setup turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Design Demo")
turtle.colormode(255)

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# ===== Helper Functions =====

def clear_screen():
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()

def draw_spirograph(duration=5):
    clear_screen()
    hue_steps = 36
    colors = [colorsys.hsv_to_rgb(i / hue_steps, 1, 1) for i in range(hue_steps)]
    colors = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

    start_time = time.time()
    angle = 0
    while time.time() - start_time < duration:
        pen.pencolor(colors[angle % hue_steps])
        pen.circle(100)
        pen.left(10)
        pen.forward(1)
        angle += 1

def draw_starburst(duration=5):
    clear_screen()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()

    hue_steps = 100
    colors = [colorsys.hsv_to_rgb(i / hue_steps, 1, 1) for i in range(hue_steps)]
    colors = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

    start_time = time.time()
    angle = 0
    while time.time() - start_time < duration:
        pen.pencolor(colors[angle % hue_steps])
        pen.forward(200)
        pen.backward(200)
        pen.left(7)
        angle += 1

def sgiri():
    clear_screen()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.pencolor(105,195,156)
    pen.right(45)
    for i in range(8):
        for i in range(30):
            pen.circle(5+i*5)
            pen.left(90)
            pen.forward(10)
            pen.right(90)
        pen.right(45)
        pen.goto(0, 0)

def triangle():
    clear_screen()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.pencolor(189,97,46)
    for i in range(100):
     pen.forward(10+i*5)
     pen.left(120)

def rose():
    clear_screen()
    pen.reset()
    pen.speed(0)
    pen.width(2)
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.pencolor(255, 0, 163)
    for i in range(200):
     pen.circle(100, 60-i)
     pen.left(i)

# ===== Run Design Loop =====

designs = [rose]

for design in designs:
    design()

# Done
pen.clear()
pen.penup()
pen.goto(0, 0)
pen.color("white")
pen.write("Thanks for watching!", align="center", font=("Courier", 24, "bold"))
turtle.done()
