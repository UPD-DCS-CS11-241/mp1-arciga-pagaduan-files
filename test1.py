from argparse import ArgumentParser
import os
import subprocess
import sys
import time



def main():
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()
    with open(args.stage_file, encoding="utf-8") as file:
        num_rows = file.readline()
        num_moves = file.readline()
        #level_layout = file.readline()
        for line in file:
            print(line,end="")

    prev_moves = ""
    points = 0

    #print(f"\nNumber of rows: {num_rows}",end="")
    #print(f"Number of moves: {num_moves}",end="")
    while num_moves != 0:
        print(f"\nPrevious moves:")
        print(f"Remaining moves: {num_moves}", end="")
        print(f"Points: {points}")
        directions = input("Enter move/s: " )
        directions = separate_moves(input("Enter move/s:" ))
        print(directions)
        num_moves = int(num_moves) - 1
        
    #for move in range(num_moves):




###################################################################################################################################


def clear_screen(): #to clear the terminal after every input
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([clear_cmd])

def first_grid_setup(row, col): #basic set-up, to control size of grid
    grid = []
    d = []
    for i in range(row):
        if i == 0 or i == max(range(row)):
            grid.append(['#'] * col)
        else:
            grid.append(['.'] * col)
        grid[i][0] = '#'
        grid[i][-1] = '#'

    for m in grid:
        d.append(m)
    return d

# print(first_grid_setup(4, 9))

def grid_added_elements(row, col): #to add any more element to the grid (PRINT THIS!)
    grid = first_grid_setup(row, col)
    d = []
    #first grid
    # grid[3][7], grid[2][7] = '#', '#' #extra walls
    # grid[2][2], grid[2][4], grid[2][6], grid[2][8], grid[2][10], grid[2][12] = 'P', 'P', 'P', 'P', 'P', 'P' #pans
    grid[1][1], grid[1][2] = 'O', 'O'
    grid[2][6], grid[2][7] = 'P', 'P'
    # grid[1][3], grid[1][11], grid[3][1], grid[3][6], grid[3][8], grid[3][13] = 'O', 'O', 'O', 'O', 'O', 'O' #nests
    for m in grid:
        d.append(m)
    return d

# print(grid_added_elements(4, 9))



# ito nagamit na

def separate_moves(args): #to throw away any unnecessary input, to accept multiple inputs at once 
    moves = 'LBFRlbfr'
    s = []
    for arg in args:
        if arg in moves:
            s.append(arg)
    return s








def actual_moves(args): #appends the direction to which the eggs would be rolling
    d = []
    moves = separate_moves(args)
    directions = '↑←↓→'
    for move in moves:
        if move == 'L' or move == 'l':
            d.append(directions[1])
        elif move == 'B' or move == 'b':
            d.append(directions[2])
        elif move == 'F' or move == 'f':
            d.append(directions[0])
        elif move == 'R' or move == 'r':
            d.append(directions[3])
    return "".join(d)

def egg_coords(row, col): #to get the original coords of the eggs
    # return [(2, 3), (2, 5), (2, 9), (2, 11), (3, 3), (3, 11)] #change at any time
    return [(1, 6), (1, 7)]

def egg_movements(args, row, col, grid): #updates the coords of the eggs
    grid = grid_added_elements(row, col)
    coords = egg_coords(row, col)
    updated = []

    for r, c in coords:
        if args == 'B' or args == 'b':
            while grid[r - 1][c] != '#' and grid[r - 1][c] != '0':
                r -= 1
            updated.append((r, c))
            # else:
            #     updated.append((r, c))
            # updated.append((r, c))
        if args == 'F' or args == 'f':
            while grid[r + 1][c] != '#' and grid[r - 1][c] != '0':
                r += 1
            updated.append((r, c))
            # else:
            #     updated.append((r, c))
        if args == 'L' or args == 'l':
            while grid[r][c - 1] != '#' and grid[r - 1][c] != '0':    
                c -= 1
            updated.append((r, c))
            # else:
            #     updated.append((r, c))
        if args == 'R' or args == 'r':
            while grid[r][c + 1] != '#' and grid[r - 1][c] != '0':
                c += 1
            updated.append((r, c))
            # else:
            #     updated.append((r, c))

    return updated

# print(egg_movements('L', 4, 9))

def first_level():
    row = 4
    col = 9
    grid = grid_added_elements(row, col)
    coords = egg_coords(row, col)
    count = 5

    for r, c in coords:
        grid[r][c] = '0'

    while count != 0:
        for m in grid:
            print(''.join(m))
        inp = input('try this mf: ')
        time.sleep(0.09)
        coords = egg_movements(inp, row, col, grid)
        print(coords)
        for r, c in coords:
            grid[r][c] = '0'
        count -= 1
        clear_screen()


#################################################

if __name__ == "__main__":
    main()




















###### this is for the clearing the terminal

#import os
#import subprocess
#import sys

#def clear_screen():
#    """Clears the terminal screen, if any"""
#    if sys.stdout.isatty():
#        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
#        subprocess.run([clear_cmd])

#def main():
#    if len(sys.argv) < 2:
#        print('The game requires a filename to start.', file=sys.stderr)
#        return
#    with open(sys.argv[1], encoding='utf-8') as f:
#        # add input code here
#        for line in f:
#            print(line,end='')
            


# -----------------------------------------------------------------


import os
import subprocess
import sys
import time
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()

    # Load level configuration
    grid, num_moves, points = load_level(args.stage_file)
    print(f"num of moves: {num_moves}")
    prev_moves = []

    # Game loop
    while num_moves > 0 and any('🥚' in row for row in grid):
        clear_screen()
        display_grid(grid)
        print(f"Previous moves: {' '.join(prev_moves)}")
        print(f"Remaining moves: {num_moves}")
        print(f"Points: {points}")

        directions = input("Enter move/s: ")
        valid_moves = separate_moves(directions)

        for move in valid_moves:
            if num_moves == 0:
                break
            grid, points = apply_move(grid, move, points)
            prev_moves.append(move)
            num_moves -= 1

    clear_screen()
    display_grid(grid)
    print("Game Over!")
    print(f"Final Points: {points}")
    print(f"Moves Played: {' '.join(prev_moves)}")

def load_level(filename):
    """Loads the level configuration from a file."""
    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0

def display_grid(grid):
    """Displays the current state of the grid."""
    for row in grid:
        print(''.join(row))

def clear_screen():
    """Clears the terminal screen."""
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([clear_cmd])

def separate_moves(args):
    """Filters valid moves from user input."""
    return [move.lower() for move in args if move.lower() in 'lrfb']

def apply_move(grid, move, points):
    """Applies a move to the grid and updates the game state."""
    if move == 'l':
        grid, points = tilt_grid(grid, points, dx=0, dy=-1)
    elif move == 'r':
        grid, points = tilt_grid(grid, points, dx=0, dy=1)
    elif move == 'f':
        grid, points = tilt_grid(grid, points, dx=-1, dy=0)
    elif move == 'b':
        grid, points = tilt_grid(grid, points, dx=1, dy=0)
    return grid, points

def tilt_grid(grid, points, dx, dy):
    """Tilts the grid in the given direction, updating egg positions and scores."""
    num_rows = len(grid)
    num_cols = len(grid[0])

    new_grid = [row[:] for row in grid]
    processed = set()  # Keep track of already processed eggs

    for r in range(num_rows):
        for c in range(num_cols):
            if (r, c) in processed:
                continue
            if grid[r][c] == '🥚':  # Egg found
                nr, nc = r + dx, c + dy
                while 0 <= nr < num_rows and 0 <= nc < num_cols:
                    if new_grid[nr][nc] == '🟩':
                        new_grid[nr][nc], new_grid[r][c] = '🥚', '🟩'
                        r, c = nr, nc  # Update position
                        nr, nc = r + dx, c + dy
                    elif new_grid[nr][nc] == '🍳':  # Egg gets cooked
                        new_grid[r][c] = '🟩'
                        points -= 5                        break
                    elif new_grid[nr][nc] == '🪹':  # Egg enters nest
                        new_grid[nr][nc] = '🪺'
                        new_grid[r][c] = '🟩'
                        points += 10
                        break
                    else:
                        break
                processed.add((r, c))  # Mark egg as processed
    return new_grid, points


if __name__ == "__main__":
    main()

    import os
import subprocess
import sys
import time
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()

    # Load level configuration
    grid, num_moves, points = load_level(args.stage_file)
    print(f"num of moves: {num_moves}")
    prev_moves = []

    # Game loop
    while num_moves > 0 and any('🥚' in row for row in grid):
        clear_screen()
        display_grid(grid)
        print(f"Previous moves: {' '.join(prev_moves)}")
        print(f"Remaining moves: {num_moves}")
        print(f"Points: {points}")

        directions = input("Enter move/s: ")
        valid_moves = separate_moves(directions)

        for move in valid_moves:
            if num_moves == 0:
                break
            grid, points = apply_move(grid, move, points)
            prev_moves.append(move)
            num_moves -= 1

    clear_screen()
    display_grid(grid)
    print("Game Over!")
    print(f"Final Points: {points}")
    print(f"Moves Played: {' '.join(prev_moves)}")

def load_level(filename):
    """Loads the level configuration from a file."""
    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0

def display_grid(grid):
    """Displays the current state of the grid."""
    for row in grid:
        print(''.join(row))

def clear_screen():
    """Clears the terminal screen."""
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([clear_cmd])

def separate_moves(args):
    """Filters valid moves from user input."""
    return [move.lower() for move in args if move.lower() in 'lrfb']

def apply_move(grid, move, points):
    """Applies a move to the grid and updates the game state."""
    if move == 'l':
        grid, points = tilt_grid(grid, points, dx=0, dy=-1)
    elif move == 'r':
        grid, points = tilt_grid(grid, points, dx=0, dy=1)
    elif move == 'f':
        grid, points = tilt_grid(grid, points, dx=-1, dy=0)
    elif move == 'b':
        grid, points = tilt_grid(grid, points, dx=1, dy=0)
    return grid, points

def tilt_grid(grid, points, dx, dy):
    """Tilts the grid in the given direction, updating egg positions and scores."""
    num_rows = len(grid)
    num_cols = len(grid[0])

    new_grid = [row[:] for row in grid]
    processed = set()  # Keep track of already processed eggs

    for r in range(num_rows):
        for c in range(num_cols):
            if (r, c) in processed:
                continue
            if grid[r][c] == '🥚':  # Egg found
                nr, nc = r + dx, c + dy
                while 0 <= nr < num_rows and 0 <= nc < num_cols:
                    if new_grid[nr][nc] == '🟩':
                        new_grid[nr][nc], new_grid[r][c] = '🥚', '🟩'
                        r, c = nr, nc  # Update position
                        nr, nc = r + dx, c + dy
                    elif new_grid[nr][nc] == '🍳':  # Egg gets cooked
                        new_grid[r][c] = '🟩'
                        points -= 5                        
                        break
                    elif new_grid[nr][nc] == '🪹':  # Egg enters nest
                        new_grid[nr][nc] = '🪺'
                        new_grid[r][c] = '🟩'
                        points += 10
                        break
                    else:
                        break
                processed.add((r, c))  # Mark egg as processed
    return new_grid, points


if __name__ == "__main__":
    main()



###### THIS IS THE CORRECT

import os
import subprocess
import sys
import time
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()

    # Load level configuration
    grid, num_moves, points = load_level(args.stage_file)
    print(f"num of moves: {num_moves}")
    prev_moves = []

    # Game loop
    while num_moves > 0 and any('🥚' in row for row in grid):
        clear_screen()
        display_grid(grid)
        print(f"Previous moves: {' '.join(prev_moves)}")
        print(f"Remaining moves: {num_moves}")
        print(f"Points: {points}")

        directions = input("Enter move/s: ")
        valid_moves = separate_moves(directions)

        for move in valid_moves:
            if num_moves == 0:
                break
            grid, points = apply_move(grid, move, points)
            prev_moves.append(move)
            num_moves -= 1

    clear_screen()
    display_grid(grid)
    print("Game Over!")
    print(f"Final Points: {points}")
    print(f"Moves Played: {' '.join(prev_moves)}")

def load_level(filename):
    """Loads the level configuration from a file."""
    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0

def display_grid(grid):
    """Displays the current state of the grid."""
    for row in grid:
        print(''.join(row))

def clear_screen():
    """Clears the terminal screen."""
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([clear_cmd])

def separate_moves(args):
    """Filters valid moves from user input."""
    return [move.lower() for move in args if move.lower() in 'lrfb']

def apply_move(grid, move, points):
    """Applies a move to the grid and updates the game state."""
    if move == 'l':
        grid, points = tilt_grid(grid, points, dx=0, dy=-1)
    elif move == 'r':
        grid, points = tilt_grid(grid, points, dx=0, dy=1)
    elif move == 'f':
        grid, points = tilt_grid(grid, points, dx=-1, dy=0)
    elif move == 'b':
        grid, points = tilt_grid(grid, points, dx=1, dy=0)
    return grid, points

def tilt_grid(grid, points, dx, dy):
    """Tilts the grid in the given direction, updating egg positions and scores with animations."""
    num_rows = len(grid)
    num_cols = len(grid[0])

    while True:  # Repeat until no eggs can move
        moved = False
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '🥚':  # Egg found
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < num_rows and 0 <= nc < num_cols:
                        if grid[nr][nc] == '🟩':  # Move to empty space
                            grid[nr][nc], grid[r][c] = '🥚', '🟩'
                            moved = True
                            clear_screen()
                            display_grid(grid)  # Show the updated grid
                            time.sleep(0.5)  # Add animation delay
                            clear_screen()
                        elif grid[nr][nc] == '🍳':  # Egg gets cooked
                            grid[r][c] = '🟩'  # Remove the egg
                            points -= 5
                            moved = True
                        elif grid[nr][nc] == '🪹':  # Egg enters nest
                            grid[nr][nc] = '🪺'  # Egg in the nest
                            grid[r][c] = '🟩'
                            points += 10
                            moved = True
        if not moved:
            break  # Stop when no more movements are possible
    return grid, points



if __name__ == "__main__":
    main()





####################### this is the latest


import os
import subprocess
import sys
import time
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()

    # Load level configuration
    grid, num_moves, points = load_level(args.stage_file)
    print(f"num of moves: {num_moves}")
    prev_moves = []

    # Game loop
    while num_moves > 0 and any('🥚' in row for row in grid):
        clear_screen()
        display_grid(grid)
        print(f"Previous moves: {' '.join(prev_moves)}")
        print(f"Remaining moves: {num_moves}")
        print(f"Points: {points}")

        directions = input("Enter move/s: ")
        valid_moves = separate_moves(directions)

        for move in valid_moves:
            if num_moves == 0:
                break
            grid, points = apply_move(grid, move, points)
            prev_moves.append(move)
            num_moves -= 1

    clear_screen()
    display_grid(grid)
    print("Game Over!")
    print(f"Final Points: {points}")
    print(f"Moves Played: {' '.join(prev_moves)}")

def load_level(filename):
    """Loads the level configuration from a file."""
    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0

def display_grid(grid):
    """Displays the current state of the grid."""
    for row in grid:
        print(''.join(row))

def clear_screen():
    """Clears the terminal screen."""
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([clear_cmd])

def separate_moves(args):
    """Filters valid moves from user input."""
    return [move.lower() for move in args if move.lower() in 'lrfb']

def apply_move(grid, move, points):
    """Applies a move to the grid and updates the game state."""
    if move == 'l':
        grid, points = tilt_grid(grid, points, dx=0, dy=-1)
    elif move == 'r':
        grid, points = tilt_grid(grid, points, dx=0, dy=1)
    elif move == 'f':
        grid, points = tilt_grid(grid, points, dx=-1, dy=0)
    elif move == 'b':
        grid, points = tilt_grid(grid, points, dx=1, dy=0)
    return grid, points


def tilt_grid(grid, points, dx, dy):
    """Moves all eggs (🥚) in the specified direction with frame-by-frame animation."""
    num_rows = len(grid)
    num_cols = len(grid[0])
    moved = True

    while moved:  # Continue moving eggs until no movement occurs
        moved = False
        new_grid = [row[:] for row in grid]  # Copy the grid for updates

        if dx == 0 and dy == -1:  # Move Left
            for r in range(num_rows):
                for c in range(1, num_cols):  # Start from the second column
                    if grid[r][c] == '🥚':
                        if grid[r][c - 1] == '🪹':  # Egg enters nest
                            new_grid[r][c - 1] = '🪺'
                            new_grid[r][c] = '🟩'
                            points += 10
                            moved = True
                        elif grid[r][c - 1] == '🍳':  # Egg gets cooked
                            #new_grid[r][c - 1] = '🟩'
                            new_grid[r][c] = '🟩'
                            points -= 5
                            moved = True
                        elif grid[r][c - 1] == '🟩':  # Egg moves left
                            new_grid[r][c - 1] = '🥚'
                            new_grid[r][c] = '🟩'
                            moved = True

        elif dx == 0 and dy == 1:  # Move Right
            for r in range(num_rows):
                for c in range(num_cols - 2, -1, -1):  # Start from the second-to-last column
                    if grid[r][c] == '🥚':
                        if grid[r][c + 1] == '🪹':  # Egg enters nest
                            new_grid[r][c + 1] = '🪺'
                            new_grid[r][c] = '🟩'
                            points += 10
                            moved = True
                        elif grid[r][c + 1] == '🍳':  # Egg gets cooked
                            new_grid[r][c + 1] = '🟩'
                            #new_grid[r][c] = '🟩'
                            points -= 5
                            moved = True
                        elif grid[r][c + 1] == '🟩':  # Egg moves right
                            new_grid[r][c + 1] = '🥚'
                            new_grid[r][c] = '🟩'
                            moved = True

        elif dx == -1 and dy == 0:  # Move Up
            for c in range(num_cols):
                for r in range(1, num_rows):  # Start from the second row
                    if grid[r][c] == '🥚':
                        if grid[r - 1][c] == '🪹':  # Egg enters nest
                            new_grid[r - 1][c] = '🪺'
                            new_grid[r][c] = '🟩'
                            points += 10
                            moved = True
                        elif grid[r - 1][c] == '🍳':  # Egg gets cooked
                            new_grid[r - 1][c] = '🟩'
                            #new_grid[r][c] = '🟩'
                            points -= 5
                            moved = True
                        elif grid[r - 1][c] == '🟩':  # Egg moves up
                            new_grid[r - 1][c] = '🥚'
                            new_grid[r][c] = '🟩'
                            moved = True

        elif dx == 1 and dy == 0:  # Move Down
            for c in range(num_cols):
                for r in range(num_rows - 2, -1, -1):  # Start from the second-to-last row
                    if grid[r][c] == '🥚':
                        if grid[r + 1][c] == '🪹':  # Egg enters nest
                            new_grid[r + 1][c] = '🪺'
                            new_grid[r][c] = '🟩'
                            points += 10
                            moved = True
                        elif grid[r + 1][c] == '🍳':  # Egg gets cooked
                            #new_grid[r + 1][c] = '🟩'
                            new_grid[r][c] = '🟩'
                            points -= 5
                            moved = True
                        elif grid[r + 1][c] == '🟩':  # Egg moves down
                            new_grid[r + 1][c] = '🥚'
                            new_grid[r][c] = '🟩'
                            moved = True

        # Display the updated grid for animation
        clear_screen()
        display_grid(new_grid)
        time.sleep(0.2)  # Add delay for animation

        grid = [row[:] for row in new_grid]  # Update grid for the next iteration

    return grid, points




def move_line_left(line, points):
    """Processes a single row or column to move eggs left."""
    new_line = ['🟩'] * len(line)  # Create a blank line
    idx = 0  # Index for new line
    for cell in line:
        if cell == '🥚':  # Egg moves to the leftmost position
            new_line[idx] = '🥚'
            idx += 1
        elif cell == '🍳':  # Egg encounters a frying pan
            points -= 5
        elif cell == '🪹':  # Egg reaches a nest
            new_line[idx] = '🪺'
            idx += 1
            points += 10
    return new_line

if __name__ == "__main__":
    main()
