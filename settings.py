import turtle

# ============================================================
# SETTINGS & SHARED VARIABLES
# ============================================================

WIDTH = 900
HEIGHT = 450
GROUND_Y = -150

AUTO_PLAY = False

# Game state variables
game_over = False
score = 0
speed = 8
spawn_timer = 0

# Screen setup
screen = turtle.Screen()
screen.title("Python Dino Runner")
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("#f7f7f7")
screen.tracer(0)
screen.listen()

# Ground line
ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.goto(-WIDTH // 2, GROUND_Y)
ground.pendown()
ground.forward(WIDTH)

# Score writer
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(300, 170)

def update_score():
    score_writer.clear()
    score_writer.write(
        f"SCORE: {int(score):05d}",
        align="center",
        font=("Arial", 16, "bold")
    )

# Game Over message
message = turtle.Turtle()
message.hideturtle()
message.penup()

def show_game_over():
    message.clear()
    message.goto(0, 30)
    message.write(
        "GAME OVER",
        align="center",
        font=("Arial", 32, "bold")
    )
    message.goto(0, -20)
    message.write(
        "Press R to restart",
        align="center",
        font=("Arial", 16, "normal")
    )