import pygame
import sys

WINDOW_TITLE = "Game Of Life"

# Define some colors
BLACK    = (  0,   0,   0)
PURPLE   = ( 22,  20,  48)
WHITE    = (255, 255, 255)
GREEN    = (  0, 255,   0)
RED      = (255,   0,   0)
BLUE     = ( 67,  66,  88)

# This sets the width and height of each grid location
width  = 20
height = 20
 
# This sets the margin between each cell
margin = 5

NR_ROWS = 20
NR_COLS = 20
SCREEN_WIDTH = 255
SCREEN_HEIGHT = 255

def add_padding(nr_rows, nr_cols, grid):
    new_grid=create_grid(nr_rows+2, nr_cols+2)
    for row in range(nr_rows):
        for column in range(nr_cols):
            new_grid[row][column]=grid[row][column]
    return new_grid

def get_number_neighbours_cell(nr_rows, nr_cols, grid, row, column):
    nr_neighbours = 0
    if (grid[row][column-1] != 0):
        nr_neighbours = nr_neighbours + 1
            
    if (grid[row][column+1] != 0):
        nr_neighbours = nr_neighbours + 1
    
    if (grid[row-1][column-1] != 0):
        nr_neighbours = nr_neighbours + 1
            
    if (grid[row-1][column+1] != 0):
        nr_neighbours = nr_neighbours + 1
            
    if (grid[row+1][column-1] != 0):
        nr_neighbours = nr_neighbours + 1
            
    if (grid[row+1][column+1] != 0):
        nr_neighbours = nr_neighbours + 1
                
    if(grid[row-1][column] != 0):
        nr_neighbours = nr_neighbours + 1

    if (grid[row+1][column] != 0):
        nr_neighbours = nr_neighbours + 1

    return nr_neighbours


    
def next_generation_value(nr_rows, nr_cols, grid, row, column):
    nr_neighbours = get_number_neighbours_cell(nr_rows, nr_cols, grid, row, column)
#     print "Final row "+ str(row)+ " col "+ str(column) + " neighbours " + str(nr_neighbours)
    if (nr_neighbours < 2):
        return 0
    if (grid[row][column] == 1  and (nr_neighbours == 2 or nr_neighbours == 3)):
        return 1
    if (grid[row][column] == 0  and (nr_neighbours == 3)):
        return 1
    if (nr_neighbours > 3):
        return 0
    return 0

def next_generation(nr_rows, nr_cols, grid):
    next_grid = create_grid(nr_rows, nr_cols)
    for row in range(nr_rows):
        for column in range(nr_cols):
            value = next_generation_value(nr_rows, nr_cols, grid, row, column)
            next_grid[row][column] = value
    return next_grid

def reset(nr_rows, nr_cols, grid):
    for row in range(nr_rows):
        for column in range(nr_cols):
            grid[row][column] = 0
    
    return grid
            
def select_cell():
    # User clicks the mouse. Get the position
    pos = pygame.mouse.get_pos()
    
    # Change the x/y screen coordinates to grid coordinates
    column = pos[0] // (width + margin)
    row = pos[1] // (height + margin)
    # Set that location to zero
    grid[row][column] = 1
    print("Click ", pos, "Grid coordinates: ", row, column)
    
    return grid

def random_configuration():
    pass

def process_events(nr_rows, nr_cols, grid, done):
    next_grid = None
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid = select_cell()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("Reset")
                grid = reset(nr_rows, nr_cols, grid)
            elif event.key == pygame.K_n:
                print "Next generation"
                grid = add_padding(nr_rows, nr_cols, grid)
                next_grid = next_generation(nr_rows, nr_cols, grid)
            elif event.key == pygame.K_c:
                print "Random configuration"
                random_configuration()
            elif event.key == pygame.K_ESCAPE:
                print "Exit"
                sys.exit(0)

    return (grid, next_grid, done)
  
def draw_grid(nr_rows, nr_cols, grid, screen, width, height, margin):
    # Draw the grid
    for row in range(nr_rows):
        for column in range(nr_cols):
            color = BLACK
            if grid[row][column] == 1:
                color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(margin+width)*column+margin,
                              (margin+height)*row+margin,
                              width,
                              height])

def create_grid(nr_rows, nr_cols):
    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []
    for row in range(nr_rows):
        # Add an empty array that will hold each cell in this row
        grid.append([])
        for col in range(nr_cols):
            grid[row].append(0) # Append a cell
    return grid
      

if __name__ == '__main__':
    grid = create_grid(NR_ROWS, NR_COLS)
 
    # Initialize pygame
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    # Set title of screen
    pygame.display.set_caption(WINDOW_TITLE)
 
    #Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while done == False:
        (grid, next_grid, done) = process_events(NR_ROWS, NR_COLS, grid, done)
 
        # Set the screen background
        screen.fill(PURPLE)
 
        if next_grid is not None:
            grid = next_grid
        
        draw_grid(NR_ROWS, NR_COLS, grid, screen, width, height, margin)
 
         # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
    pygame.quit()