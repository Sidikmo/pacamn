import turtle
import time
import random


# Step 1: Setting Up the Game Environment
screen = turtle.Screen()
screen.title("Pac-Man Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off the screen updates

# Step 2: Creating Pac-Man
pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("yellow")
pacman.penup()
pacman.goto(0, 0) # start position
pacman.direction = "stop"

# Step 3: Control Pac-Man's Direction
def go_up():
    pacman.direction = "up"
def go_down():
    pacman.direction = "down"
def go_left():
    pacman.direction = "left"

def go_right():
    pacman.direction = "right"

# Move Pac-Man
def move():
    if pacman.direction == "up":
        y = pacman.ycor()
        pacman.sety(y + 20)
    elif pacman.direction == "down":
        y = pacman.ycor()
        pacman.sety(y - 20)
    elif pacman.direction == "left":
        x = pacman.xcor()
        pacman.setx(x - 20)
    elif pacman.direction == "right":
        x = pacman.xcor()
        pacman.setx(x + 20)


# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")



ghosts = []
colors = ["purple", "cyan", "orange", "green"]
start_pos = [(100, 0), (-100, 0), (0, 100), (0, -100)]

for color, position in zip(colors, start_pos):
    ghost = turtle.Turtle()
    ghost.shape("square")
    ghost.color(color)
    ghost.penup()
    ghost.goto(position)
    ghosts.append(ghost)

# random ghost directions

# = put value in variable
# == compare or to check
def move_ghosts():
    for ghost in ghosts:
        direction = random.choice(["up", "down", "left", "right"])
        if direction == "up":
            y = ghost.ycor()
            ghost.sety(y + 20)
        elif direction == "down":
            y = ghost.ycor()
            ghost.sety(y - 20)
        elif direction == "left":
            x = ghost.xcor()
            ghost.setx(x - 20)
        elif direction == "right":
            x = ghost.xcor()
            ghost.setx(x + 20)


# create the maze:
maze_layout = [
    "WWWWWWWWWWWWWW",
    "W            W",
    "W WWW WW WWW W",
    "W            W",
    "W WWW WW WWW W",
    "W            W",
    "WWWWWWWWWWWWWW",
]

block_size = 40  # Change this to a larger number to scale up the maze

def draw_maze(maze):
  valid_food_positions = []
  maze_width = len(maze[0])
  maze_height = len(maze)
  
  block_size_width = screen.window_width() / maze_width
  block_size_height = screen.window_height() / maze_height
  
  block_size = min(block_size_width, block_size_height)
  
  wall = turtle.Turtle()
  wall.shape("square")
  wall.color("red")
  wall.penup()
  wall.speed(0)  # controls how fast maze is drawn
  
  start_x = -((maze_width / 2) * block_size)
  start_y = ((maze_height / 2) * block_size)
  
  for y in range(maze_height):
      for x in range(maze_width):
          character = maze[y][x]
          screen_x = start_x + (x * block_size)
          screen_y = start_y - (y * block_size)
  
          if character == "W":
              wall.goto(screen_x, screen_y)
              wall.shapesize(stretch_wid=block_size / 20, stretch_len=block_size / 20)
              wall.stamp()
          else:
              valid_food_positions.append((screen_x, screen_y))
  return valid_food_positions
  
draw_maze(maze_layout)

#Create the Food
valid_positions = draw_maze(maze_layout)

foods = []
for _ in range(40):
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("orange")
    food.penup()
    food.shapesize(stretch_wid=0.4, stretch_len=0.4)
    # Choose a random position from the valid positions
    x, y = random.choice(valid_positions)
    food.goto(x, y)
    foods.append(food)




# Main Game Loop
while True:
    screen.update()
    move()  # moving pacman
    move_ghosts()  # moving ghosts

    for food in foods:
        if pacman.distance(food) < 10:
            # Respawn the food at a new valid location
          food.hideturtle()

    time.sleep(0.1)  # Control the speed of Pac-Man's movement
# Main Game Loop