import turtle
import random
import time
# Setting up window
wn = turtle.Screen()
wn.bgcolor("dark blue")
wn.setup(width = 600,height = 600)
wn.title("Snake Game")
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("light green")
head.penup()
head.goto(0,0)
head.direction = 'stop'

# Move function
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

# Direction changing functions
def go_up():
    if head.direction!='down':
        head.direction = 'up'
def go_down():
    if head.direction!='up':
        head.direction = 'down'
def go_left():
    if head.direction!='right':
        head.direction = 'left'
def go_right():
    if head.direction!='left':
        head.direction = 'right'

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up,'Up')
wn.onkeypress(go_down,'Down')
wn.onkeypress(go_left,'Left')
wn.onkeypress(go_right,'Right')
delay = 0.1 # To slow down the snake speed

# Food
food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.speed(0)
food.penup()
food.shapesize(0.5,0.5)
x = random.randint(-290,290)
y = random.randint(-290,290)
food.goto(x,y)

# adding a segment
segments = []

score = 0
# Score Management
pen  = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(-220,240)

# Main Loop
while True:
    wn.update()
    move()
    # Food Eating logic
    if head.distance(food) < 15:
       x = random.randint(-290,290)
       y = random.randint(-290,290)
       food.goto(x,y)
       new_segment = turtle.Turtle()
       new_segment.shape('square')
       new_segment.color('light green')
       new_segment.speed(0)
       new_segment.penup()
       segments.append(new_segment)
       score = score+10
    # Length increase logic
    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments)> 0 :
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    # Window collision logic
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
         time.sleep(1)
         head.goto(0,0)
         head.direction = 'stop'
         for i in segments:
             i.goto(1000,1000)
         segments = []
         score = 0
    # Body Collision Check
    for i in range(len(segments)-1):
        if head.distance(segments[i+1])<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
    pen.clear()
    pen.write("Score: {}".format(score),align='center',font=('Courier',18,'normal'))
    time.sleep(delay)
