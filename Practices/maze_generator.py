# TE 2nd Maze Generator
# TE 3rd Maze Generator
# Imports
import turtle
import random

#Global Variables
CELL_SIZE = 40# size of each square cell in pixels
ROWS = 10# number of rows in maze
COLS = 10# number of columns in maze
#Setup
screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.title("Random Maze Generator (Guaranteed Solvable)")

start = turtle.Turtle()#Start point
start.penup()
start.setpos(-185,180)
start.pendown()
start.write("Start")

end = turtle.Turtle()#End point
end.penup()
end.setpos(180,-180)
end.pendown()
end.write("End")

pen = turtle.Turtle()#The pen, this actually draws the maze.
pen.speed(0)#Pen speed
pen.pensize(3)#Pen Size
pen.hideturtle() #This will hide the pen when it doesn't need to be seen
# Maze Cell System
# Each cell has walls: [top, right, bottom, left]
maze =[[[True, True, True, True] for c in range(COLS)] for r in range(ROWS)]#Boolean values for maze
visited = [[False for c in range(COLS)] for r in range(ROWS)]#Booleans values for visted parts of the maze

# Functions

def draw_cell(x, y, walls):
    """Draw one cell given its bottom-left corner (x, y) and wall states."""
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)

    # top wall
    if walls[0]:
        pen.pendown()
        pen.forward(CELL_SIZE)
    pen.penup()
    pen.goto(x + CELL_SIZE, y)
    pen.setheading(-90)

    # right wall
    if walls[1]:
        pen.pendown()
        pen.forward(CELL_SIZE)
    pen.penup()
    pen.goto(x + CELL_SIZE, y - CELL_SIZE)
    pen.setheading(180)

    # bottom wall
    if walls[2]:
        pen.pendown()
        pen.forward(CELL_SIZE)
    pen.penup()
    pen.goto(x, y - CELL_SIZE)
    pen.setheading(90)

    # left wall
    if walls[3]:
        pen.pendown()
        pen.forward(CELL_SIZE)
    pen.penup()

def draw_maze():
    """Draw all cells of the maze."""
    start_x = -COLS * CELL_SIZE // 2
    start_y = ROWS * CELL_SIZE // 2
    for r in range(ROWS):
        for c in range(COLS):
            x = start_x + c * CELL_SIZE
            y = start_y - r * CELL_SIZE
            draw_cell(x, y, maze[r][c])

def get_neighbors(r, c):
    """Return valid neighbor cells with direction info."""
    neighbors = []
    if r > 0: neighbors.append(("up", r - 1, c))
    if r < ROWS - 1: neighbors.append(("down", r + 1, c))
    if c > 0: neighbors.append(("left", r, c - 1))
    if c < COLS - 1: neighbors.append(("right", r, c + 1))
    return neighbors

def remove_wall(r, c, direction):
    """Remove the wall between current cell and a neighbor."""
    if direction == "up":
        maze[r][c][0] = False
        maze[r-1][c][2] = False
    elif direction == "down":
        maze[r][c][2] = False
        maze[r+1][c][0] = False
    elif direction == "left":
        maze[r][c][3] = False
        maze[r][c-1][1] = False
    elif direction == "right":
        maze[r][c][1] = False
        maze[r][c+1][3] = False

def generate_maze(r, c):
    """Recursive backtracking algorithm to carve maze paths."""
    visited[r][c] = True
    neighbors = get_neighbors(r, c)
    random.shuffle(neighbors)
    for direction, nr, nc in neighbors:
        if not visited[nr][nc]:
            remove_wall(r, c, direction)
            generate_maze(nr, nc)

# Generate
generate_maze(0, 0)  # start carving from top-left cell

# Draw
draw_maze()

turtle.done()