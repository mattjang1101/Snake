# Simple Snake game in python 3
# Part 1 - Getting started

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)        # Turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)   #Fastest
head.shape("square")
head.penup()    # No drawing when moving
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)   #Fastest
food.shape("circle")
food.color("red")
food.penup()    # No drawing when moving
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 
           24, "normal"))

# Functions. If current direction is opposite to the desired direction,
# (left -> right) (up -> down), etc... Don't change directions. Otherwise,
# change directions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
    
def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    # X and Y coordinates for head
    y = head.ycor() 
    x = head.xcor() 

    # Moves head up 
    if head.direction == "up":
        head.sety(y + 20) 

    # Moves head down
    if head.direction == "down":
        head.sety(y - 20)  

    # Moves head left
    if head.direction == "left":
        head.setx(x - 20) 

    # Moves head right
    if head.direction == "right":
        head.setx(x + 20)  

# Keyboard bindings. Call on go functions if the keys are pressed
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()     # update the screen

    # ************* Check for a COLLISION with the border **************** #
    if (head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or
        head.ycor() < -290):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)    # off the screen

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        # Write to screen
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), 
                  align="center", font=("Courier", 24, "normal"))

    #** APPEND: If snake collides with food (each turtle object is 20px by 20px) ****#
    if head.distance(food) < 20:
        # Move the food to a random spot. Screen is 600 by 600 
        # and in order for the food to not go offscreen (reaches -300 or 300),
        # set position to -290 and 290
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)        # animation speed
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten delay
        delay -= 0.001

        # Increase the score. Write to screen
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), 
                  align="center", font=("Courier", 24, "normal"))

    # ******* Move the end segments first in reverse order ******* #
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    # Move segment 0 (first segment) to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # moves the head
    move()         

    #******* COLLISION: heck for head collision with the body segments *******#
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)    # off the screen

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Write to screen
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), 
                    align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)   # slows execution for 0.1 seconds
# end while
wn.mainloop()