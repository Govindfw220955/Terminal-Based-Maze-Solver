import random
import turtle

# ANSI escape codes for text formatting
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"

# Global variables for maze settings
CELL_SIZE = 10
START_X = -200
START_Y = 200

def create_maze(n, density):
    # Create a maze with walls and open spaces
    maze = [[RED + ' █ ' + RESET if random.random() < density else BLUE + ' ◌ ' + RESET for _ in range(n)] for _ in range(n)]
    maze[0][0] = BOLD + GREEN + ' S ' + RESET   # Start
    maze[n-1][n-1] = BOLD + GREEN + ' E ' + RESET  # End
    return maze

def draw_cell(x, y, color):
    # Draw a cell at the specified position with the given color
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(CELL_SIZE)
        turtle.right(90)
    turtle.end_fill()

def draw_maze(maze):
    # Draw the maze grid with walls and open spaces
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            x = START_X + j * CELL_SIZE
            y = START_Y - i * CELL_SIZE
            if cell == RED + ' █ ' + RESET:
                draw_cell(x, y, 'black')
            elif cell == BLUE + ' ◌ ' + RESET:
                draw_cell(x, y, 'white')
            elif cell == BOLD + GREEN + ' S ' + RESET:
                draw_cell(x, y, 'green')
            elif cell == BOLD + GREEN + ' E ' + RESET:
                draw_cell(x, y, 'red')

def dfs_pathfinding(maze, x, y, path):
    # Depth-First Search algorithm to find a path from the start to the end
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and (maze[x][y] == BLUE + ' ◌ ' + RESET or maze[x][y] == BOLD + GREEN + ' S ' + RESET or maze[x][y] == BOLD + GREEN + ' E ' + RESET):
        path.append((x, y))
        maze[x][y] = BOLD + BLUE + ' ◌ ' + RESET  # Mark as visited

        if x == len(maze) - 1 and y == len(maze[0]) - 1:  # Reached the end
            return True

        # Explore all possible moves: right, down, left, up
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for move in moves:
            new_x, new_y = x + move[0], y + move[1]
            if dfs_pathfinding(maze, new_x, new_y, path):
                return True

        path.pop()  # Backtrack if no valid moves

    return False

def draw_path(path):
    # Draw the path using Turtle graphics
    turtle.speed(10)
    turtle.penup()
    turtle.goto(START_X + CELL_SIZE / 2, START_Y - CELL_SIZE / 2)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('blue')
    turtle.shape("arrow")

    for cell in path:
        x, y = cell
        turtle.goto(START_X + y * CELL_SIZE + CELL_SIZE / 2, START_Y - x * CELL_SIZE - CELL_SIZE / 2)

def main():
    # Setup Turtle
    turtle.setup(800, 800)
    turtle.title("Maze with Path")
    turtle.bgcolor("white")

    # Hide Turtle
    turtle.hideturtle()

    # Get user input for maze size
    maze_size = int(input("Enter the size of the maze (n x n): "))
    wall_density = 0.2
    
    # Generate the initial maze
    maze = create_maze(maze_size, wall_density)
    
    print("\nGenerated Maze:")
    draw_maze(maze)

    while True:
        # Display user menu
        print("\nMenu:")
        print("1. Find and Draw the Path")
        print("2. Generate Another Maze")
        print("3. Exit the Game")       
        option = int(input("Enter Your Choice (1/2/3): "))
        
        if option == 1:
            # Find and draw the solution path
            path = []
            if dfs_pathfinding(maze, 0, 0, path):
                draw_path(path)
                print("\nPath Found and Drawn!")
            else:
                print("\nNo path found.")

        elif option == 2:
            # Generate a new maze and redraw it
            turtle.clear()
            maze = create_maze(maze_size, wall_density)
            print("\nGenerated Maze:")
            draw_maze(maze)
            
        else:
            # Exit the game
            turtle.bye()
            break

    turtle.done()

if __name__ == '__main__':
    main()
