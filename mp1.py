"""
The mp1.py file is the terminal version of the Egg Roll game 
- meaning that when it is run, it has no interface other than 
the one shown in the WSL terminal. It can be run to load a game 
level using python3 mp1.py level1.in (if you want to load level1.in).

The modules os, subprocess, and sys are imported for the 
clear_screen function which is responsible for clearing 
the screen after every movement of the egg, time for the 
delay of every snapshot of the movement of the eggs, and 
the one with the argparse is to help in accepting two 
arguments for python3 in the command-line interface as 
you open the game. The Moves and Board classes are imported
from the mp1_classes to import the classes representing
the different emojis and moves in the game. The Union, List,
and Tuple are imported from the typing module for the
type-checking.

"""

import os
import subprocess
import sys
import time
from typing import Union, List, Tuple
from argparse import ArgumentParser
from mp1_classes import Moves, Board

def main() -> None:
    """
    This function handles the interaction with the player by loading the game level, 
    managing the moves, displaying the grid, and updating the leaderboard.
    The one with the ArgumentParser() up to .parse.args() is the one responsible 
    for adding a new argument to python3 mp1.py <filename> so that when mp1.py is run, 
    the filename with it will appear through series of function in mp1.py.
    The game will then load the level using the load_level function. 
    The previous moves that are typed will be appended on prev_moves. 
    With the while loop inside this function, the function will run as long as the 
    number of moves is greater than 0 and if there are any eggs or empty nests on 
    every row in the grid. It will then clear the screen, display the grid through 
    display_grid function, and print the previous moves, remaining moves, and points 
    of the player. The program will accept moves which will then be passed on the 
    separate_moves function and for every move in valid_moves, the function will call 
    the apply_move function. At the end of the round, the previous moves, remaining 
    moves, and score accumulated by the player will be flashed on the screen.
    
    Args:
        None

    Returns:
        None
    """
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()

    grid, num_moves, points = load_level(args.stage_file)
    prev_moves: List[str] = []

    while num_moves > 0 and (any('🥚' in row for row in grid) and any('🪹' in row for row in grid)):
        clear_screen()
        display_grid(grid)
        print(
            "===============\n"
            "To see the Top 3 scores for this grid, you may click the 'H' key on your keyboard."
            "Note that the high scores will not be shown if the input is 'RHL', 'LH', or "
            "any variants where 'H' is together with other symbols in the input.\n"
            "==============="
        )
        print(f"Previous moves: {''.join(prev_moves)}")
        print(f"Remaining moves: {num_moves}")
        print(f"Points: {points}")

        directions = input("Enter move/s: ")
        if directions in ("H", "h"):
            first_score, second_score, third_score = get_leaderboard(args.stage_file)
            print(f"""===============\nLeaderboard for this level:\n
    1st: {first_score}
    2nd: {second_score}
    3rd: {third_score}
            """)
            input("Press any key to return to the game.")

        valid_moves = separate_moves(directions)
        for move in valid_moves:
            if num_moves == 0:
                break
            grid, points = apply_move(grid, move, points)
            move_conversion = {"f": "↑", "b": "↓", "l": "←", "r": "→"}
            prev_moves.append(move_conversion[move])
            num_moves -= 1

    clear_screen()
    display_grid(grid)
    print(f"Previous moves: {''.join(prev_moves)}")
    print(f"Remaining moves: {num_moves}")
    if any('🪹' in row for row in grid):
        print(f"Points: {points}")
    else:
        points = points + (num_moves) * 2
        print(f"Points: {points}")
    change_leaderboard(args.stage_file, points)


def load_level(filename: str) -> Tuple[List[List[str]], int, int]:
    """
    This function reads the information located in the .in file as represented
    by the argument (filename) which is a path. The first line in the file will
    be saved as num_rows, the second line as num_moves, and the remaining lines
    will be saved as grid. The function will return a grid, containing list of
    rows of emojis, number of moves available, and 0 as the initial point or score.

    Args: 
        filename (str): The name of the file containing the level data.

    Returns:
        Tuple[List[List[str]], int, int]: A tuple containing the grid, 
        number of moves, and initial points.

    """
    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0


def display_grid(grid: List[List[str]]) -> None:
    """
    This function displays the game grid on the terminal.
    It accepts one argument which is a grid or a list of 
    rows of emojis. The function prints every list of rows 
    of emojis and joins them into one row using for loop.

    Args: 
        grid List[List[str]]: The current game grid.

    Returns:
        None

    """
    for row in grid:
        print(''.join(row))


def clear_screen() -> None:
    """
    This function clears the terminal screen whenever it is called.
    This is usually called in the main function wherein every snapshot 
    of the movement is displayed.

    Args:
        None

    Returns:
        None

    """
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        try:
            subprocess.run([clear_cmd], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to clear the screen: {e}")


def separate_moves(args: Union[str, None]) -> List[str]:
    """
    This function accepts valid moves in 'lrfb' and discards irrelevant inputs.
    The input is provided by the player when the "Enter move/s:" is shown on the terminal. 
    The function checks through isinstance() if the args is a string. 
    If it is a string, it will return a list of characters or letters if the letters are in 'lfrb', 
    and an empty list if otherwise.

    Args:
        args (Union[str, None]): A string containing potential moves or None (represented by spaces)
    
    Returns: 
        List[str]: A list of valid moves ('lrfb') in lowercase.

    """
    if isinstance(args, str):
        return [move.lower() for move in args if move.lower() in 'lrfb']
    return []

def get_leaderboard(filename: str) -> Tuple[int, int, int]:
    """
    This function reads the leaderboard file (hs_mp1_level#.in) 
    related to the file opened in the terminal. It saves the Top 3 
    scores from the file into variables first, second, and third, and returns them.
    
    Args:
        filename (str): The level file name

    Returns:
        Tuple[int, int, int]: The top three scores, defaulting to 0 if not found.
    """
    leaderboard_file = 'hs_mp1_' + filename
    try:
        with open(leaderboard_file, encoding="utf-8") as file:
            first = int(file.readline().strip())
            second = int(file.readline().strip())
            third = int(file.readline().strip())
        return first, second, third
    except (ValueError, FileNotFoundError):
        return 0, 0, 0


def apply_move(grid: List[List[str]], move: str, points: int) -> Tuple[List[List[str]], int]:
    """
    This function applies a move to the grid and updates the points. The apply_move 
    function has three arguments: grid which is the list of rows of emojis loaded by 
    the load_level function, move which is the character in 'lfrb', and points which 
    is the points accumulated by the player. Through if statements, the function checks 
    the appropriate action to do depending on the move. If move == 'l', it will call 
    tilt_grid with dy = -1. The dy and dx will change depending on the value of move. 
    The function will return an updated grid which is a list of rows of emojis and 
    the updated points.

    Args:
        grid (List[List[str]]): The current game grid.
        move (str): The move to apply ('l', 'r', 'f', 'b').
        points (int): The current score.

    Returns:
        Tuple[List[List[str]], int]: The updated grid and points.
    """
    match move:
        case Moves.leftward:
            grid, points = tilt_grid(grid, points, 0, -1)
        case Moves.rightward:
            grid, points = tilt_grid(grid, points, 0, 1)
        case Moves.forward:
            grid, points = tilt_grid(grid, points, -1, 0)
        case Moves.backward:
            grid, points = tilt_grid(grid, points, 1, 0)
    return grid, points


def tilt_grid(grid: List[List[str]], points: int, dx: int, dy: int) -> Tuple[List[List[str]], int]:
    """
    This function handles the tilting of the grid in a specific direction. It uses a 
    while loop that runs as long as movements are possible, determined by the `moved` 
    variavle. Depending on `dx` and `dy`, the function processes rows 
    (horizontal movement or dx = 0) or columns (vertical movement or dx != 0) 
    by combining them into strings and passing them to the process_lines function.

    The grid is updated based on the processed lines, either by replacing rows for 
    horizontal movement or updating columns for vertical movement. 
    If any movement occurs, the grid will be displayed through 
    the display_grid function. If there are no further movements are possible, 
    the function returns the updated grid and score.

    Args:
        grid (List[List[str]]): The current game grid.
        points (int): The current score.
        dx (int): Row direction (-1 for up, 1 for down, 0 for no change).
        dy (int): Column direction (-1 for left, 1 for right, 0 for no change).

    Returns:
        Tuple[List[List[str]], int]: The updated grid and points.
    """

    moved = True
    num_rows, num_cols = len(grid), len(grid[0])

    while moved:
        moved = False

        lines = (
            [''.join(row) for row in grid] if dx == 0 else
            [''.join(grid[r][c] for r in range(num_rows)) for c in range(num_cols)]
        )
        direction = 'left' if (dx == -1 or dy == -1) else 'right'
        updated_lines, points, moved = process_lines(lines, points, direction)

        for idx, line in enumerate(updated_lines):
            if dx == 0:
                grid[idx] = list(line)
            else:
                for r in range(num_rows):
                    grid[r][idx] = line[r]

        if moved:
            clear_screen()
            display_grid(grid)
            time.sleep(0.3)

    return grid, points


def process_lines(lines: List[str], points: int, direction: str) -> Tuple[List[str], int, bool]:
    """
    This function processes multiple lines (rows or columns) for egg 
    movement by calling the shift_eggs function and getting the
    updated lines (if the eggs have shifted). It will return the updated
    lines, the updated points, and if the eggs moved or not.

    Args:
        lines (List[str]): A list of strings representing rows or columns of the grid.
        points (int): The current score.
        direction (str): The direction of movement ('left' or 'right').

    Returns:
        Tuple[List[str], int, bool]: 
            - List[str]: The updated lines after processing movement.
            - int: The updated score.
            - bool: Whether any movement occurred.
    """
    moved = False
    updated_lines = []
    for line in lines:
        shifted_line, line_moved, updated_points = shift_eggs(line, points, direction)
        updated_lines.append(shifted_line)
        moved = moved or line_moved
        points = updated_points
    return updated_lines, points, moved



def shift_eggs(line: str, points: int, direction: str) -> Tuple[str, bool, int]:
    """
    This function is responsible for shifting the eggs to the left, 
    right, up, or down depending on the argument direction. It has 
    three arguments: line which is either a row or a column, points 
    which is the initial points, and direction. It has variables for 
    every emoji of grass, eggs, etc, and a variable moved = False 
    which will be changed if the eggs in the line shifted, determining 
    the moved_any on the tilt_grid function. The code block contains 
    if statements depending on the direction, and it usually checks 
    if the pan is on the direction of the egg (which changes 
    the egg tile into grass tile), or if the nest that is empty is 
    on the direction of the egg (which changes the nest into a full 
    nest), or if the grass is next to the egg (which changes the egg 
    tile into grass tile and vice versa). The function returns a 
    joined line_list, wherein the initial line_list is the value 
    of line and the updated line_listis the one changed through 
    index checking and changing of values on the list. It also 
    returns moved if the eggs shifted and points if the player 
    accumulated points for moving.

    Args:
        line (str): A string representing a single row or column of the grid.
        points (int): The current score.
        direction (str): The direction of movement ('left' or 'right').

    Returns:
        Tuple[str, bool, int]: 
            - str: The updated line after movement.
            - bool: Whether any movement occurred in the line.
            - int: The updated score.
    """
    line_list = list(line)
    moved = False

    match direction:
        case 'left':
            for i in range(1, len(line_list)):
                if line_list[i] == '🥚':
                    match line_list[i - 1]:
                        case Board.pan:
                            line_list[i] = Board.grass
                            moved = True
                            points -= 5
                        case Board.empty_nest:
                            line_list[i - 1] = Board.full_nest
                            line_list[i] = Board.grass
                            moved = True
                            points += 10
                        case Board.grass:
                            line_list[i - 1] = line_list[i]
                            line_list[i] = Board.grass
                            moved = True
        case 'right':
            for i in range(len(line_list) - 2, -1, -1):
                if line_list[i] == '🥚':
                    match line_list[i + 1]:
                        case Board.pan:
                            line_list[i] = Board.grass
                            moved = True
                            points -= 5
                        case Board.empty_nest:
                            line_list[i + 1] = Board.full_nest
                            line_list[i] = Board.grass
                            moved = True
                            points += 10
                        case Board.grass:
                            line_list[i + 1] = line_list[i]
                            line_list[i] = Board.grass
                            moved = True

    return ''.join(line_list), moved, points


def change_leaderboard(filename: str, new_score: int) -> None:
    """
    This function updates the leaderboard with a new score. It will be 
    called by the 'main' function once the game round is finished. It will
    call the 'get_leaderboard' function to retrieve the Top 3 scores for 
    the level. These scores will then be stored in a list where they will be
    sorted, and the (new) Top 3 scores will be extracted and written in the
    leaderboard file.

    Args:
        filename (str): The stage file name
        new_score (int): The new score to be added on the leaderboard

    Returns:
        None
    """
    first_score, second_score, third_score = get_leaderboard(filename)
    scores = [first_score, second_score, third_score, new_score]
    try:
        scores = sorted(scores, reverse=True)[:3]
        with open('hs_mp1_' + filename, 'w', encoding="utf-8") as file:
            for score in scores:
                file.write(f"{score}\n")
    except ValueError as e:
        print(f"The score values are None: {e}")


if __name__ == "__main__":
    main()
