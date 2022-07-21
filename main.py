import random
import turtle
import time

delay = 0.01

WIDTH = 600
HEIGHT = 600

key_queue = []

wn = turtle.Screen()
wn.title("Snaneke")
wn.bgcolor("black")
wn.setup(width=WIDTH, height=HEIGHT)
wn.tracer(0)

screenclear = turtle.Turtle()
screenclear.speed(0)
screenclear.shape("square")
screenclear.shapesize(50, 50)
screenclear.pensize(10000000)
screenclear.color("black")
screenclear.hideturtle()

# Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.shapesize(2, 2)
head.pensize(41)
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "up"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.shapesize(2.5, 2.5)
food.color("red")
food.penup()
food.goto(0, 100)

segments = []


# Functions
def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


def move():
    if len(segments) > 0:
        if head.distance(segments[0]) < 100:
            head.clear()
            head.pencolor("grey")
            head.pendown()
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 50)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y + -50)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x + -50)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 50)
    head.penup()

def collision():
    # Wall collision
    if head.xcor() > WIDTH / 2:
        head.goto(-(WIDTH / 2), head.ycor())
    if head.xcor() < -(WIDTH / 2):
        head.goto(WIDTH / 2, head.ycor())
    if head.ycor() > HEIGHT / 2:
        head.goto(head.xcor(), -(HEIGHT / 2))
    if head.ycor() < -(HEIGHT / 2):
        head.goto(head.xcor(), HEIGHT / 2)

    # Food collision
    if head.distance(food) < 50:
        screenclear.hideturtle()
        # Move Food
        x = random.randint(-(WIDTH / 2 - 50) / 50, (WIDTH / 2 - 50) / 50)
        y = random.randint(-(HEIGHT / 2 - 50) / 50, (HEIGHT / 2 - 50) / 50)
        food.goto(x * 50, y * 50)

        new_segment = turtle.Turtle()
        new_segment.width = 40
        new_segment.penup()
        new_segment.speed(1)
        new_segment.shapesize(2, 2)
        new_segment.pensize(41)
        new_segment.shape("square")
        new_segment.color("grey")
        segments.append(new_segment)

def movement():
    # Tail movement
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        if segments[i].distance(segments[i - 1]) < 100:
            segments[i].clear()
            segments[i].pendown()
        segments[i].goto(x, y)
        segments[i].penup()

        if segments.index(segments[i]) == len(segments) - 1:
            segments[i - 1].clear()

    # Move first tail piece to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        if segments[0].distance(head) < 100:
            segments[0].clear()
            segments[0].pendown()
        segments[0].goto(x, y)
        segments[0].penup()

        segments[-1].clear()

def body_collision():
    global segments
    # Body collision
    for segment in segments:
        if head.distance(segment) < 50:
            wn.update()
            time.sleep(0.5)
            for segment1 in segments:
                segment1.clear()
                segment1.ht()
                del segment1

            screenclear.showturtle()
            screenclear.pendown()
            screenclear.goto(0, 0)
            screenclear.penup()

            segments = []
            head.goto(0, 0)
            head.direction = "stop"

            time.sleep(0.5)

# Inputs
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Loop
runs = 0
while True:
    runs += 1

    if runs % 20 == 0:
        wn.update()
        collision()
        movement()
        move()
        body_collision()

    wn.update()
    time.sleep(delay)