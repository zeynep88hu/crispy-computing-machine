import turtle
import time
import random

# Setup the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []
score = 0
high_score = 0
delay = 0.1

# Pen for score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


# Move the snake
def move():
    directions = {"up": (0, 20), "down": (0, -20), "left": (-20, 0), "right": (20, 0)}
    x, y = directions.get(head.direction, (0, 0))
    head.setx(head.xcor() + x)
    head.sety(head.ycor() + y)


# Control functions
def change_direction(new_direction):
    opposite_directions = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if head.direction != opposite_directions.get(new_direction):
        head.direction = new_direction


wn.listen()
wn.onkey(lambda: change_direction("up"), "Up")
wn.onkey(lambda: change_direction("down"), "Down")
wn.onkey(lambda: change_direction("left"), "Left")
wn.onkey(lambda: change_direction("right"), "Right")

# Main game loop
while True:
    wn.update()

    # Collision with borders
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Collision with food
    if head.distance(food) < 20:
        food.goto(random.randint(-270, 270), random.randint(-270, 270))

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        high_score = max(high_score, score)

        pen.clear()
        pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move segments
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()
    time.sleep(delay)