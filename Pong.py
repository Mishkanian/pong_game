"""
Pong
"""
import turtle

wn = turtle.Screen()
wn.title("Pong by Michael Mishkanian")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A (Player's paddle)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # make paddle a rectangle
paddle_a.penup()
paddle_a.goto(-350, 0) # starting location of paddle on left side of screen

# Paddle B (Computer Paddle)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) # starting location of paddle on right side of screen

# Ball
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(0, 0) # ball starts in middle of screen

# Main game loop
while True:
    wn.update()
