"""
The game.py file contains the different functions that enable 
our team to create the game interface. To give an overview on 
how the whole file works, we used the pygame library to create 
features such as button and loading images onto the screen. 
The game.py shows the different assets or the icons used to load 
the nests, eggs, etc. on the game screen through calling screen.blit() 
across the document. It also contains the logic behind how the points 
are calculated and to determine if the game is over or not.

The code block from "from typing" to "from mp1_classes" imports 
pygame as it is the library used for loading screen frames, 
sys for system commands such as quitting the game, and KEYDOWN, 
K_UP, and others as they will be used in the start_with_gui_level() 
function to detect if the keys clicked on the keyboard are the letter 
keys or the arrow keys for the game to progress. It also contains the 
global variables for the screen width, screen height, and frame per 
second which are the basis to the screen resolution of the game. 
We used 960 x 768 pixels as it is not large (or wide enough) but 
it is also not small. We also used 60 frames per second as it is 
one of the most common FPS in games.

The typing module is used for the mypy --strict and pyright checking.
The mp1_classes module is used for handling events such as when the
DELETE key is pressed to restart the level.

The block of code that consists of game_light up to lose_dark variables 
assigns the pictures on the images folder loaded via pygame.image.load() 
into variables. This is important as it will be used in the 
start_gui_with_level() function on loading the game interface screen and 
the frames that show you if you win or lose the game.

"""
from typing import List, Tuple, Dict
import sys
import pygame
from pygame.locals import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_f, K_b, K_l, K_r, QUIT, K_DELETE # pylint: disable=no-name-in-module
from mp1_classes import EventHandler, Board

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 768
FPS = 60

game_light = pygame.image.load('images/game_light.png')
game_dark = pygame.image.load('images/game_dark.png')
win_light = pygame.image.load('images/win_light.png')
win_dark = pygame.image.load('images/win_dark.png')
lose_light = pygame.image.load('images/lose_light.png')
lose_dark = pygame.image.load('images/lose_dark.png')

def load_assets() -> Dict[str, pygame.Surface]:
    """
    The load_assets function is responsible for loading the icons 
    in the game such as the eggs, grass, walls, frying pans, and nests. 
    It has a dictionary assets that has strings of the description of 
    the icons as the keys and the object being loaded via 
    pygame.image.load() as the values. These objects or images 
    will be scaled down to 81 by 81 pixels via the pygame.transform.scale, 
    and the function will return a dictionary of these scaled images.
    
    Args: 
        None as it is a callable function for loading game assets.

    Returns:
        assets (Dict[str,pygame.Surface]): A dictionary containing scaled image assets.

    """
    assets = {
        "egg": pygame.image.load("assets/egg.png"),
        "nest": pygame.image.load("assets/nest.png"),
        "full_nest": pygame.image.load("assets/full_nest.png"),
        "frying_pan": pygame.image.load("assets/frying_pan.png"),
        "grass": pygame.image.load("assets/grass.png"),
        "wall": pygame.image.load("assets/wall.png")
    }
    for key, image in assets.items():
        assets[key] = pygame.transform.scale(image, (81, 81))
    return assets


def display_grid(screen: pygame.Surface,
    grid: List[List[str]],
    assets: Dict[str, pygame.Surface]) -> None:
    """
    The display_grid function is responsible for displaying the grid of 
    the ones in the .in files and the grids on the .in files will then 
    be represented by every value in the dictionary assets through series 
    of if statements. It accepts three arguments: screen which pertains 
    to the game screen with width and height which will be defined on the 
    start_with_gui_level function, the grid which will be also defined in 
    the said function as it will be saved by calling the load_level function, 
    and the assets which will be defined as the start_with_gui_level calls 
    display_grid. The nested for loops iterate each row first through the 
    for row_idx... and column through for col_idx.... The x and y are the 
    basis for the starting position where the assets or icons will be placed. 
    The multiplier here is 27 since through trial and error, we observed that 
    the width and height of every cell or icon must be 1/3 of the dimension 
    of the scaled assets or icons in the display_grid function (81 x 81). 
    The nested loops are responsible for iterating every row and every column 
    of the grid, filling the cells or the square areas with the icons in the 
    assets (substituting eggs emoji with the image of an egg for example).


    Args:
        screen (pygame.Surface): The game screen surface.
        grid (List[List[str]]): The game grid.
        assets (Dict[str, pygame.Surface]): Dictionary of game assets.

    Returns:
        None
    """
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            x, y = col_idx * 27, row_idx * 27
            if cell == '🥚':
                screen.blit(assets['egg'], (x, y))
            elif cell == '🪹':
                screen.blit(assets['nest'], (x, y))
            elif cell == '🪺':
                screen.blit(assets['full_nest'], (x, y))
            elif cell == '🍳':
                screen.blit(assets['frying_pan'], (x, y))
            elif cell == '🟩':
                screen.blit(assets['grass'], (x, y))
            else:
                screen.blit(assets['wall'], (x, y))


def load_level(filename: str) -> Tuple[List[List[str]], int, int]:
    """
    The load_level function is responsible for loading the files in 
    .in format. It accepts filename path as the argument. The function 
    then opens the file in UTF-8 format using with open... as file. 
    The first line of the file is saved as num_rows, the second line 
    as num_moves, and the next remaining lines are saved as a list of 
    lines in the variable grid. The function returns the grid as a 
    list of lines of emojis, num_moves representing the number of moves 
    available, and 0 since it will be saved as the initial point or score 
    in the start_gui_with_level function.

    Args:
        filename (str): The name of the level file.

    Returns:
        Tuple[List[List[str]], int, int]:
            - The game grid.
            - The number of moves allowed.
            - The initial score (0).
    """
    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0


def get_leaderboard_scores(filename: str) -> Tuple[int, int, int]:
    """
    This function reads the leaderboard file (hs_gui_level#.in) 
    related to the file opened in the terminal. It saves the Top 3 
    scores from the file into variables first, second, and third, and returns them.
    
    Args:
        filename (str): The name of the leaderboard file.

    Returns:
        Tuple[int, int, int]:
            - First place score.
            - Second place score.
            - Third place score.
    """
    leaderboard_file = 'hs_gui_' + filename
    try:
        with open(leaderboard_file, encoding="utf-8") as file:
            first = int(file.readline().strip())
            second = int(file.readline().strip())
            third = int(file.readline().strip())
        return first, second, third
    except (ValueError, FileNotFoundError) as e:
        print(f"Cannot read the leaderboard file: {e}")
        return 0, 0, 0


def apply_move(grid: List[List[str]], move: str, points: int) -> Tuple[List[List[str]], int, bool]:
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
        move (str): The move direction ('l', 'r', 'f', 'b').
        points (int): The current score.

    Returns:
        Tuple[List[List[str]], int, bool]:
            - The updated grid.
            - The updated score.
            - Whether the move was valid.
    """
    prev_grid = [row[:] for row in grid]
    if move == 'l':
        grid, points = tilt_grid(grid, points, dx=0, dy=-1)
    elif move == 'r':
        grid, points = tilt_grid(grid, points, dx=0, dy=1)
    elif move == 'f':
        grid, points = tilt_grid(grid, points, dx=-1, dy=0)
    elif move == 'b':
        grid, points = tilt_grid(grid, points, dx=1, dy=0)

    if grid != prev_grid:
        return grid, points, True

    return grid, points, False


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


def is_game_over(grid: List[List[str]], num_moves: int) -> bool:
    """
    The is_game_over function checks if the game is over by checking 
    whether the empty_nests == 0, eggs == 0, or num_moves == 0 through 
    the function .count(). In the empty_nests, the count of empty nests 
    will be checked for every row, and their sum will be added. 
    Same goes for the eggs where the count of the eggs will be checked 
    in every row. The function returns True if either the empty nests, 
    eggs, or number of moves count is 0 and False if otherwise.

    Args:
        grid (List[List[str]]): The current game grid.
        num_moves (int): The remaining number of moves.

    Returns:
        bool: True if the game is over, False otherwise.
    """
    empty_nests = sum(row.count('🪹') for row in grid)
    eggs = sum(row.count('🥚') for row in grid)
    return empty_nests == 0 or eggs == 0 or num_moves == 0


def check_if_win_or_lose(grid: List[List[str]]) -> bool:
    """
    The check_if_win_or_lose function checks if at the end of the 
    movement (or gaming session), the player loses or wins by checking 
    the sum of the count of empty nests per row which is saved in the 
    empty nests variable. If empty_nests == 0, the function returns 
    True, signifying that the player wins the game, and False if 
    otherwise, signifying that the player loses the game.

    Args:
        grid (List[List[str]]): The current game grid.

    Returns:
        bool: True if the player won, False otherwise.
    """
    empty_nests = sum(row.count('🪹') for row in grid)
    if empty_nests == 0:
        return True
    return False


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
    first_score, second_score, third_score = get_leaderboard_scores(filename)
    scores = [first_score, second_score, third_score, new_score]
    scores = sorted(scores, reverse=True)[:3]
    with open('hs_gui_' + filename, 'w', encoding="utf-8") as file:
        for score in scores:
            file.write(f"{score}\n")


def process_game_events(grid: List[List[str]],
    num_moves: int,
    points: int,
    prev_moves: List[str],
    filename: str) -> Tuple[List[List[str]], int, int, List[str]]:
    """
    This function creates a dictionary that maps every key on the
    keyboard to a specific letter in 'fblr'. It process game events 
    like key presses and update the game state through the apply_move 
    function, returning the updated grid, number of moves, points, and
    list of previous moves.

    Args:
        grid (List[List[str]]): The current game grid.
        num_moves (int): The remaining number of moves.
        points (int): The current score.
        prev_moves (List[str]): The list of previous moves.
        filename (str): The name of the level file.

    Returns:
        Tuple[List[List[str]], int, int, List[str]]: Updated game 
        state (grid, moves, score, and previous moves).
    """
    key_to_move = {
        K_UP: 'f',
        K_f: 'f',
        K_DOWN: 'b',
        K_b: 'b',
        K_LEFT: 'l',
        K_l: 'l',
        K_RIGHT: 'r',
        K_r: 'r',
    }

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  # pylint: disable=no-member
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_DELETE:
                grid, num_moves, points = load_level(filename)
                prev_moves = []
                continue

            move = key_to_move.get(event.key)
            if move:
                grid, points, valid_move = apply_move(grid, move, points)
                if valid_move:
                    prev_moves.append(move.upper())
                    num_moves -= 1

    return grid, num_moves, points, prev_moves



def start_gui_with_level(filename: str, mode: str = "light", tutorial: bool = False) -> None:
    """
    The start_gui_with_level function is responsible for doing everything 
    that involves the .in files: from loading the files, applying the moves, 
    checking if the game is over, and others by calling several functions 
    throughout the game.py file. It starts by initializing the pygame through 
    pygame.init(), the screen with width and height, the caption for the 
    game window, and the clock for the time within the game (for the frame 
    per second). The function accepts two arguments: the filename which is 
    a path of the file and the mode (the default is "light", and calling 
    the function with one argument means that the function will load the 
    game screen in light mode). The load_assets will then be called so that 
    there will be scaled icons saved in assets variable. The file is then 
    loaded by calling the load_level function, extracting the grid, 
    number of moves, and initial points. It has a while loop which 
    checks for every event or action that the player does on the keyboard 
    or the game window. Every key is checked in the process_game_events
    function. The if statements with the KEYDOWN and other 
    conditions with K is for checking every event or action on the keyboard. 
    If the X on the game window is pressed, the game window disappears. 
    Pressing the UP arrow key or F calls the function apply_move with 'f' 
    as its direction, pressing the DOWNarrow key or B calls the function 
    apply_move with 'b' as its direction, pressing the LEFT arrow key or 
    L calls the function apply_move with 'l' as its direction, and pressing 
    the RIGHT arrow key or R calls the function apply_move with 'r' as its 
    direction. The movement done is then appended on the prev_moves. 
    The screen is shown through the screen.blit(...) call, which shows the 
    light mode of the game interface if the mode = "light" and dark mode if 
    mode = "dark". The function display_grid is called to display the 
    contents of the file, substituting every emojis into their corresponding 
    icons in the assets. The previous moves, number of moves available, 
    and points are displayed through the code below. Note that the 
    previous moves will only be shown the prev_moves is not an empty list.
    
    There are two helper functions inside this function: the draw_game_texts
    and the handle_game_end. The draw_game_texts handles the drawing of the
    game texts such as the previous moves, points, and number of moves
    remaining. The handle_game_end function is responsible for checking if
    the game has already ended, and what to do when such thing happens.

    Args:
        filename (str): The name of the level file.
        mode (str, optional): Display mode ('light' or 'dark'). Defaults to "light".
        tutorial (bool, optional): Whether the game is in tutorial mode. Defaults to False.
    
    Returns:
        None
    """
    pygame.init()  # pylint: disable=no-member
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Egg Roll")
    clock = pygame.time.Clock()

    assets = load_assets()
    grid, num_moves, points = load_level(filename)
    prev_moves: List[str] = []
    font = pygame.font.Font(None, 36)

    def draw_game_texts() -> None:
        """
        This handles drawing game text components on the screen while
        the game is ongoing. It displays the previous moves (if any),
        number of moves remaining, and the points accumulated by the player.
        
        Args:
            None

        Returns:
            None
        """
        screen.blit(game_light if mode == "light" else game_dark, (0, 0))
        display_grid(screen, grid, assets)
        if prev_moves:
            prev_moves_text = font.render(f"{''.join(prev_moves)}", True, (121, 78, 7))
            screen.blit(prev_moves_text, (315, 583))
        moves_text = font.render(f"{num_moves}", True, (121, 78, 7))
        screen.blit(moves_text, (315, 623))
        points_text = font.render(f"{points}", True, (121, 78, 7))
        screen.blit(points_text, (315, 668))

    def handle_game_end() -> None:
        """
        This handles end-game display and leaderboard updates by calling
        the check_if_win_or_lose function. It is responsible for displaying
        the final points, number of moves remaining, and the moves used
        throughout the game. The leaderboard is then changed if the level
        shown is not a tutorial level. The background is displayed through the
        screen.blit function, while the texts use font.render with the arguments 
        string, True for anti-aliasing (for good-quality text display), and 
        the RGB code. It then calls the process_events in the mp1_classes.py
        if the user wants to restart the level or not.

        Args:
            None

        Returns:
            None
        """
        event_handler = EventHandler()
        if check_if_win_or_lose(grid):
            points_to_add = num_moves * 2
            final_points = points + points_to_add
            screen.blit(win_light if mode == "light" else win_dark, (0, 0))
        else:
            final_points = points
            screen.blit(lose_light if mode == "light" else lose_dark, (0, 0))

        if not tutorial:
            change_leaderboard(filename, final_points)
        display_grid(screen, grid, assets)
        prev_moves_text = font.render(f"{''.join(prev_moves)}", True, (121, 78, 7))
        screen.blit(prev_moves_text, (315, 583))
        moves_text = font.render(f"{num_moves}", True, (121, 78, 7))
        screen.blit(moves_text, (315, 623))
        points_text = font.render(f"{final_points}", True, (121, 78, 7))
        screen.blit(points_text, (315, 668))
        pygame.display.flip()

        while True:
            restart = event_handler.process_events("end_game")
            if restart is True:
                start_gui_with_level(filename, mode)

    while num_moves > 0:
        grid, num_moves, points, prev_moves = process_game_events(
            grid, num_moves, points, prev_moves, filename
        )

        draw_game_texts()

        if is_game_over(grid, num_moves):
            handle_game_end()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()  # pylint: disable=no-member
    sys.exit()
