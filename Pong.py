"""
Pong game by Michael Mishkanian
"""
import turtle

wn = turtle.Screen()
wn.title("Pong by Michael Mishkanian")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # make paddle a rectangle
paddle_a.penup()
paddle_a.goto(-350, 0) # starting location of paddle on left side of screen

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) # starting location of paddle on right side of screen

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) # ball starts in middle of screen
ball.dx = .3 #movement speed of ball
ball.dy = .3

def paddle_a_up():
    """
    This function takes in the current y-coordinate of paddle A
    and then increases the position by 20 (AKA "go up")
    """
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    """
    This function takes in the current y-coordinate of paddle A
    and then decreases the position down 20 (AKA "go down")
    """
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    """
    This function takes in the current y-coordinate of paddle B
    and then increases the position by 20 (AKA "go up")
    """
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    """
    This function takes in the current y-coordinate of paddle B
    and then decreases the position by 20 (AKA "go down")
    """
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Key bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checks
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverse direction if ball is too high
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # reverse direction if ball is too low

    # retart game when the ball passes a paddle
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    # Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 
                          and ball.ycor() > paddle_b.ycor() - 40):
                          ball.setx(340)
                          ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 
                          and ball.ycor() > paddle_a.ycor() - 40):
                          ball.setx(-340)
                          ball.dx *= -1

