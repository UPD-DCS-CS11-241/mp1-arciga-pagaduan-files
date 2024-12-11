# Welcome to Egg Roll!
> Note that the code documentation part is still not yet done. Apologies for the delay.

Good day! Are you egg-cited to play the greatest game of all time? If you are seeing this, this is your sign to roll with us in ***Egg Roll***.

**Egg Roll** is a 2D puzzle game that aims to put the eggs on all nests. Several eggs are scattered throughout the screen, and by performing a series of tilts and directions, you will be able to roll the eggs on their respective nests. But beware: you should avoid getting all your eggs into the frying pan as it will lower your points. 

What are you waiting for? Let's get rolling!

# Overview
Here are the contents of the user manual / documentation:

 1. [Getting Started](#getting-started)
 2. [Opening the Game](#opening-the-game)
 3. [Navigating the Game Interface](#navigating-the-game-interface)
    - [Play](#play)
    - [Settings](#settings)
      - [Tutorials](#tutorials)
      - [Control Keys](#control-keys)
      - [Night Mode](#night-mode)
      - [Credits](#credits)
      - [Main Menu](#main-menu)
    - [Exit Game](#exit-game)
 4. [Game Levels](#game-levels)
    - [Level 1: U-Turn](#level-1-u-turn)
    - [Level 2: Shake It Off](#level-2-shake-it-off)
    - [Level 3: Mitosis](#level-3-mitosis)
    - [Level 4: Clockwise](#level-4-clockwise)
    - [Level 5: Into The Void](#level-5-into-the-void)
    - [Tutorials: Level 1](#tutorials-level-1)
    - [Tutorials: Level 2](#tutorials-level-2)
    - [Tutorials: Level 3](#tutorials-level-3)
    - [Tutorials: Level 4](#tutorials-level-4)
    - [Tutorials: Level 5](#tutorials-level-5)
 5. [For Instructors and Developers](#for-instructors-and-developers)
    - [Code Documentation](#code-documentation)
      - [mp1.py](#the-mp1py-file)
      - [test.py](#the-testpy-file)
      - [gui.py](#the-guipy-file)
      - [game.py](#the-gamepy-file)
    - [Bonus Features](#bonus-features)
    - [For Future Developers](#for-future-developers)
    - [Release and Patch Notes](#release-and-patch-notes)
    - [Acknowledgements and Task Delegations](#acknowledgements-and-task-delegations)


# Getting Started

Before playing the game, here are the prerequisites or steps that you should follow to setup your device and ensure a smooth experience in playing the game: 

 1. Make sure that you are using Windows 10 or higher that supports WSL. If so, click on the Windows Icon 🪟 and search for **`Command Prompt`** in the Start Menu. Right-click it and select **`Run as administrator`**. Click **`Yes`** to gain rights to install WSL in your computer.

 2.   Install WSL on your computer / PC through **`Command Prompt`** or **`Windows Powershell`**. Type **`wsl --install`** in your terminal. This will install WSL which has the terminal to create the commands needed to run the game. After installing, you may be asked for your username and password. 

 3. In your WSL terminal, type **`sudo apt update`** followed by **`sudo apt install python3.12`** to install Python in your WSL system. To verify if you already installed Python, type **`python3 --version`** in your terminal. It should show you something like **`Python 3.12.7`** in your screen - this means you have Python in version 3.12.7.

 4. Also, if you are interested in testing the program, type **`pip install pygame`** to install PyGame. This is the third-party library that is utilized for the game program.

 5. Lastly, type **`pip install pytest`** to install PyTest. This is also a third-party library used for testing the functionality of the game program.


 
# Opening the Game
1. Since you are here in Github reading these instructions, click on the **`Code`** button - the green button beside the ➕ symbol *(as encircled in the photo below)*.

![How To Download Files](/readme_docs/screenshot_1.png)

 2. Once done, click on the **`Download ZIP`** button. This should download all your files on your PC.

 3. In your PC, extract the contents of the ZIP you have downloaded. You can do it by clicking the right side of your mouse pad, selecting **`Extract All`**, and clicking **`Extract`**. You can also do this by clicking the ⋯ (three dots icon), selecting **`Extract All`**, and clicking **`Extract`** to put your files on your target folder destination. *(The three dots icon is shown in the sample picture below.)*

![How To Extract ZIP](/readme_docs/screenshot_2.png)

 4. Make sure that your folder **`mp1-arciga-pagaduan-files-main`** is in your Linux system. You can do this by dragging the folder or copying the folder and pasting it into the **`Ubuntu > home > (your username)`** folder. You can check if your folder is in the right path by opening your WSL application through searching for **`WSL`** in the Start Menu. Type **`ls`** in your terminal. It should show you the name of your folder. *(The right implementation of knowing if the folder is in the right location is shown in the picture below.)*

![How To Know if Your Folder is in the Right Location](/readme_docs/screenshot_3.png)

 5. Type **`cd mp1-arciga-pagaduan-files-main`** in your terminal. This should allow you to execute commands inside the said folder. 
 6. To start the game, type **`python3 gui.py`** in your terminal. This should open up the game (or on a deeper sense, the `gui.py` file). *To verify if you implement the steps correctly and the game loads, a tab that looks similar to the picture below must appear.*

![How To Know if Your Game Loads Correctly](/images/main_menu_light.png)


# Navigating the Game Interface
![Main Menu Interface](/images/main_menu_light.png)

In this section, we will be navigating the Egg Roll interface.  The picture above shows the `Main Menu` interface of the game. It has three buttons: [`Play`](#play), [`Settings`](#settings), and [`Exit Game`](#exit-game) which will be explained in the next sections.

## Play
![Levels Interface](/images/levels_light.png)

As you click the `Play` button, you can see the interface (just like the one shown above) containing the levels for the game. It also has the `Main Menu` button to go back to the main menu of the game.

There are five levels named: *U-Turn, Shake It Off, Mitosis, Clockwise,* and *Into The Void*. When you click a level here (example: U-Turn), a loading screen will be shown which directs you to the game itself *(as shown in the pictures below).*

![Loading Screen Interface](/images/loading_1_light.png)

![Game Interface](/readme_docs/level1_interface.png)


It also has the `Main Menu` button that leads you back to the [Main Menu](#navigating-the-main-interface). More details on these levels, as well as the mechanics and solutions, are shown in the [Game Levels](#game-levels) section.

## Settings
![Settings Interface](/images/settings_light.png)

As you click the `Settings` button, you can see the interface (as shown in the picture above) containing the different options in store for this game. This includes `Tutorials`, `Control Keys`, `Night Mode`, `Credits`, and `Main Menu`.

### Tutorials
![Tutorials Interface](/images/tutorials_light.png)

As you click the `Tutorials` button, you can see the interface (just like the one shown above) containing the tutorial levels for the game. It also has the `Main Menu` button to go back to the main menu of the game.

There are five levels for the tutorial section. These levels are relatively easy as it can give you a grasp on what the rules are. When you click a level here (example: Level 1), a loading screen will be shown which directs you to the game itself *(as shown in the pictures below).*

![Loading Screen Interface](/images/loading_1_light.png)

![Game Interface](/readme_docs/game_interface.png)

More details on these levels, as well as the mechanics and solutions, are shown in the [Game Levels](#game-levels) section.


### Control Keys
![Control Keys](/images/control_keys_light.png)

Clicking the `Controls` button will show the interface like the one shown above. It contains the different controls for you to move the egg across the game area such as:

 - `L`, `l`, or `←` to move left
 - `R`, `r`, or `→` to move right
 - `F`,`f`, or `↑` to move up
 - `B`, `b`, or `↓` to move down

It also has the `Settings` button, and when clicked, it will bring you back to the [Settings](#settings).

### Night Mode
![Night Mode Settings](/images/settings_dark.png)

![Night Mode Main Menu](/images/main_menu_dark.png)

Clicking the `Night Mode` button will change the whole game interface into night mode like the one shown above.


### Credits
![Credits](/images/credits_light.png)

Clicking the `Credits` button will direct you to the interface as shown above. It contains the name of the creators of the game (us). 

It also has the `Settings` button, and when clicked, it will bring you back to the [Settings](#settings).

### Main Menu
Clicking the `Main Menu` button will be direct you back to the [Main Menu](#navigating-the-game-interface) interface.

## Exit Game
![Exit Game Interface](/images/sure_light.png)

Clicking the `Exit Game` on the [Main Menu](#navigating-the-game-interface) section will lead you to the screen like the one shown above. This screen shows you if you are already leaving the game.  Clicking `Yes` will close the game, while clicking `No` will lead you back to the [Main Menu](#navigating-the-game-interface) interface.

# Game Levels
![Game Interface](/readme_docs/level_3_interface.png)

In the game level interface as shown above (and every game level), you can see the previous moves (which shows you the moves you have made), remaining moves (number of moves available), points (the score you accumulate throughout the game sessions), the control keys you may use to progress the game, and the prompt telling you that you can press `DELETE` in your keyboard to restart the game.

In this game proper, there are total of 10 levels (5 from the Levels in the [Levels](#play) interface and 5 from the [Tutorials](#tutorials). In each level, you are given eggs, and your objective is to put these eggs on all nests. There are frying pans on the game area, and as much as possible, you should avoid getting your eggs into the frying pan. There are also walls where eggs cannot penetrate. Once the eggs reach the nests, the nest will become full and will act as a wall so that the eggs cannot get pass through it.

Getting an egg into the egg nest will give you **10** points. Gettng an egg into a frying pan will give you **-5** points (losing 5 points). Finishing the level with remaining moves will give you **`remaining moves * 2`** points -- meaning, if you finished a game with 30 points from 3 full egg nests and you still have 2 remaining moves (provided that all nests are occupied), you will garner a total of `30 + (2 * 2) = 34` points.  Note that there are levels wherein it is inevitable for eggs to move into the frying pan to solve the particular game level (implying that not all eggs must fit on all nests).

Winning the game means that you have put the eggs on all nests within the given number of moves available. Losing the game means that either you have not put the eggs on all nests at the end of the round, you have put all eggs on the frying pan on or before the end of the round, or you have put some eggs on the frying pan at the end of the round.

To see how the level looks like, photos and solutions are provided to solve the levels below.
> **Spoiler Alert**: For those who do not want spoilers on the solutions, we advise you not to scroll down further.

 1. [Level 1: U-Turn](#level-1-u-turn) 
 2. [Level 2: Shake It Off](#level-2-shake-it-off)
 3. [Level 3: Mitosis](#level-3-mitosis)
 4. [Level 4: Clockwise](#level-4-clockwise)
 5. [Level 5: Into The Void](#level-5-into-the-void)
 6. [Tutorials: Level 1](#tutorials-level-1)
 7. [Tutorials: Level 2](#tutorials-level-2)
 8. [Tutorials: Level 3](#tutorials-level-3)
 9. [Tutorials: Level 4](#tutorials-level-4)
 10. [Tutorials: Level 5](#tutorials-level-5)

## Level 1: U-Turn
![Level 1: U-Turn Interface](/readme_docs/level1_interface.png)

This is a trivial level with a trivial solution. It is named *U-Turn*, with its name based on its actual sequence of steps for the correct solution. This level somehow prepares you to more harder levels in the game.
> **Number of rows**: 4

> **Number of moves available**: 4

> **Solution**: FLB

> **Highest possible points**: 12

## Level 2: Shake It Off
![Level 2: Shake-It-Off Interface](/readme_docs/level_2_interface.png)

This is also a trivial level with a trivial solution - it depends if you figured it out quickly. It is named *Shake It Off*, with its name also based on its actual sequence of steps for the correct solution. One may be tempted to do left or right movement first but doing so will eventually make you have less eggs to put on all nests.
> **Number of rows**: 4

> **Number of moves available**: 4

> **Solution**: FB or BF

> **Highest possible points**: 64

## Level 3: Mitosis
![Level 3: Mitosis Interface](/readme_docs/level_3_interface.png)

This level is named *Mitosis* as the game design resembles the splitting of two cells or squares - inspired by the biological concept of *mitosis*. It is a moderately hard level.
> **Number of rows**: 5

> **Number of moves available**: 5

> **Solution**: LRBR or RLBL

> **Highest possible points**: 37

## Level 4: Clockwise
![Level 4: Clockwise Interface](/readme_docs/level_4_interface.png)

This level is named *Clockwise* as the game solution resembles the actual concept of *clockwise* movement. It is a moderately hard to hard level. 
> **Number of rows**: 9

> **Number of moves available**: 9 

> **Solution**: LFRB

> **Highest possible points**: 200
 
## Level 5: Into The Void
![Level 5: Into The Void Interface](/readme_docs/level_5_interface.png)

This level is named *Into The Void* as the unique game design for this level has frying pans, instead of walls, as the outer layer in the level. Also, the game design for this level resembles being inside a void, since everything is surrounded by frying pans (whose function resembles like a void). It is a moderately hard to hard level. 
> **Number of rows**: 19

> **Number of moves available**: 10 

> **Solution**: FBRLFLR 

> **Highest possible points**: 561

## Tutorials: Level 1
![Tutorials: Level 1 Interface](/readme_docs/tutorials_level1_interface.png)

This level is supposed to be a trivial level wherein you can get a grasp on the mechanics of the game through a simple puzzle.

> **Number of rows**: 3

> **Number of moves available**: 2 

> **Solution**: L 

> **Highest possible points**: 561

## Tutorials: Level 2
![Tutorials: Level 2 Interface](/readme_docs/tutorials_level2_interface.png)

This level is also a trivial level wherein you can get a grasp on how frying pans work in the game.

> **Number of rows**: 4

> **Number of moves available**: 3 

> **Solution**: LR 

> **Highest possible points**: 22

## Tutorials: Level 3
![Tutorials: Level 3 Interface](/readme_docs/tutorials_level3_interface.png)

This level is also a trivial level wherein you can get a grasp on how important it is to take note on the number of moves available for the level. One may tempt to do RLBRF or LRFLB but since there are only 3 moves available, these solutions may not work.

> **Number of rows**: 4

> **Number of moves available**: 3 

> **Solution**: FB or BF

> **Highest possible points**: 22

## Tutorials: Level 4
![Tutorials: Level 4 Interface](/readme_docs/tutorials_level4_interface.png)

This level is an easy to moderately easy level that incorporates the concept of frying pans, importance of number of remaining moves, and every aspect of the game mechanics.

> **Number of rows**: 5

> **Number of moves available**: 5 

> **Solution**: RFLB

> **Highest possible points**: 35

## Tutorials: Level 5
![Tutorials: Level 5 Interface](/readme_docs/tutorials_level5_interface.png)

This level is somehow a trivial level (depending on your perception) as it introduces the concept in some levels of the game wherein you have to think on how your movements affect the other eggs in several 'subdivisions' of the gaming area.

> **Number of rows**: 8

> **Number of moves available**: 4 

> **Solution**: LR or RL

> **Highest possible points**: 44





# For Instructors and Developers
This section is for the instructors who will grade our project, as well as for (future) developers who are interested on improving our project. Also, there are patch notes or announcements in this section for the gamers or users of this game to be informed of the possible updates of the game.

## Code Documentation
This section contains the code documentation and explanation of the `.py` files that are important for this project. The main library used for this project are the `pygame` library for the graphical user interface (GUI) and `pytest` library for the testing of the files. The file `mp1.py` is for the terminal version of the game, `test.py` is for the test cases, `gui.py` is for the main menu interface, and `game.py` is for the game interface.

### The `mp1.py` file
The `mp1.py` file is the terminal version of the Egg Roll game - meaning that when it is run, it has no interface other than the one shown in the WSL terminal. It can be run to load a game level using `python3 mp1.py level1.in` (if you want to load `level1.in`). 
```python
import os
import subprocess
import sys
import time
from argparse import ArgumentParser
```
The modules `os`, `subprocess`, and `sys` are imported for the `clear_screen` function which is responsible for clearing the screen after every movement of the egg, `time` for the delay of every snapshot of the movement of the eggs, and the one with the `argparse` is to help in accepting two arguments for `python3` in the command-line interface as you open the game.

 ```python
def main(): #Handles the interaction with the player
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()


    grid, num_moves, points = load_level(args.stage_file)
    print(f"num of moves: {num_moves}")
    prev_moves = []
  ...
  ...
  if __name__ == "__main__":
    main()
```
The `main` function is for the overall management of the game - from loading the level, displaying the grid, separating the input moves, up to applying the input moves. The one with the `ArgumentParser()` up to `.parse.args()` is the one responsible for adding a new argument to `python3 mp1.py <filename>` so that when `mp1.py` is run, the filename with it will appear through series of function in `mp1.py`. The game will then load the level using the `load_level` function. The previous moves that are typed will be appended on `prev_moves`. With the while loop inside this function, the function will run as long as the number of moves is greater than 0 and if there are any eggs or empty nests on every row in the grid. It will then clear the screen, display the grid through `display_grid` function, and print the previous moves, remaining moves, and points of the player. The program will accept moves which will then be passed on the `separate_moves` function and for every move in `valid_moves`, the function will call the `apply_move` function. At the end of the round, the previous moves, remaining moves, and score accumulated by the player will be flashed on the screen.

 ```python
def load_level(filename): #Reads the information located in the .in file
    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0
```
The `load_level` function reads the information inside the file as represented by the argument `filename` which is a path. The first line in the file will be saved as `num_rows`, the second line as `num_moves`, and the remaining lines will be saved as `grid`. The function will return a grid, containing list of rows of emojis, number of moves available, and `0` as the initial point or score.

 ```python
def display_grid(grid): #Displays the grid
    for row in grid:
        print(''.join(row))
```
The `display_grid` function displays the grid on the terminal. It accepts one argument which is a grid or a list of rows of emojis. The function prints every list of rows of emojis and joins them into one row using for loop.

 ```python
def clear_screen(): #Clears the screen
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([clear_cmd])
```

The `clear_screen` function clears the terminal whenever it is called. This is usually called in the `main` function wherein every snapshot of the movement is displayed. 

 ```python
def separate_moves(args): #Accepts valid moves and discards irrelevant inputs
    if isinstance(args, str):
        return [move.lower() for move in args if move.lower() in 'lrfb']
    else:
        return []
```

The `separate_moves` function accepts `args` as its argument which could be any type. This string is the input provided by the player when the "Enter move/s:" is shown on the terminal. The function checks through `isinstance()` if the `args` is a string. If it is a string, it will return a list of characters or letters if the letters are in 'lfrb', and an empty list if otherwise.

 ```python
def apply_move(grid, move, points): #Links the egg's movements within the grid to the inputs
    if move == 'l':
        grid, points = tilt_grid(grid, points, dx=0, dy=-1)
    elif move == 'r':
        grid, points = tilt_grid(grid, points, dx=0, dy=1)
    elif move == 'f':
        grid, points = tilt_grid(grid, points, dx=-1, dy=0)
    elif move == 'b':
        grid, points = tilt_grid(grid, points, dx=1, dy=0)
    return grid, points
 ```

The `apply_move` function has three arguments: `grid` which is the list of rows of emojis loaded by the `load_level` function, `move` which is the character in 'lfrb', and `points` which is the points accumulated by the player. Through `if` statements, the function checks the appropriate action to do depending on the `move`. If `move == 'l'`, it will call `tilt_grid` with `dy = -1`. The `dy` and `dx` will change depending on the value of `move`.  The function will return an updated grid which is a list of rows of emojis and the updated points.

 ```python
def tilt_grid(grid, points, dx, dy): #Handles the two kinds of movements in the grid: from row to row, and from column to column
    num_rows = len(grid)
    num_cols = len(grid[0])
    moved = True

    while moved:  
        moved = False
        new_grid = [row[:] for row in grid]  

        if dx == 0 and dy != 0: 
            for r in range(num_rows):
                row = ''.join(grid[r])
                if dy == -1: 
                    shifted_row, row_moved, updated_points = step_shift_eggs_with_rules(row, points, 'left')
                elif dy == 1: 
                    shifted_row, row_moved, updated_points = step_shift_eggs_with_rules(row, points, 'right')
                new_grid[r] = list(shifted_row)
                points = updated_points
                moved = moved or row_moved
        ...
        ...
        if moved:
            clear_screen()
            display_grid(new_grid)
            time.sleep(0.3)  
        grid = [row[:] for row in new_grid] 
    return grid, points
 ```

The `tilt_grid` function accepts four arguments: `grid` which is the initial grid from the `apply_move` function, `points` which is the initial score from the `apply_move` function, `dx` is the vertical movement where `-1` tilts the grid up while `1` tilts the grid down, and `dy` is the horizontal movement where`-1` tilts the grid left while `1` tilts the grid right. It contains a while loop where the `new_grid` is created as a storage for the updated grid and `moved = False` is added so that if there are still cells or eggs that can still move, the egg will still move, making the `moved = True` in the later part of the code block. The code block will then check for the values of `dx` and `dy`. If the `dy != 0 and dx = 0`, it will check if the `dy` is equal to `-1` or `1`. Depending on `dy`, it will then call the function `step_shift_eggs_with_rules` to move the eggs to either left or right. The same goes to the condition if `dy = 0 and dx != 0` wherein if `dx` is equal to `-1` or `1`, it will call the function `step_shift_eggs_with_rules` to move the eggs to either up or down. For every iteration of row or column, the `new_grid` is then updated, and the `moved` is updated depending on whether a row or a column moved. If the value of `moved == True`, the screen will be cleared through the `clear_screen()`, the grid will be displayed through `display_grid()`, and a snapshot of the changing of the grid will be shown in the terminal through the `time.sleep()`. The function will then return the updated grid and points.

 ```python
def step_shift_eggs_with_rules(line, points, direction): #Moves the egg from left to right within the grid
    empty_char = '🟩' 
    frying_pan = '🍳'
    nest = '🪹'
    full_nest = '🪺'
    line_list = list(line)
    moved = False

    if direction == 'left':
        for i in range(1, len(line_list)):
            if line_list[i] == '🥚':
                if line_list[i - 1] == frying_pan: 
                    line_list[i] = empty_char
                    moved = True
                    points -= 5
                elif line_list[i - 1] == nest: 
                    line_list[i - 1] = full_nest
                    line_list[i] = empty_char
                    moved = True
                    points += 10
                elif line_list[i - 1] == empty_char: 
                    line_list[i - 1], line_list[i] = line_list[i], empty_char
                    moved = True
...
...
    return ''.join(line_list), moved, points
 ```
 
The `step_shift_eggs_with_rules` function is responsible for shifting the eggs to the left, right, up, or down depending on the argument `direction`. It has three arguments: `line` which is either a row or a column, `points` which is the initial points, and `direction`. It has variables for every emoji of grass, eggs, etc, and a variable `moved = False` which will be changed if the eggs in the `line` shifted, determining the `moved_any` on the `tilt_grid` function. The code block contains `if` statements depending on the `direction`, and it usually checks if the `frying_pan` is on the `direction` of the `egg` (which changes the egg tile into grass tile), or if the `nest` that is empty is on the direction of the egg (which changes the nest into a full nest), or if the `grass` is next to the egg (which changes the egg tile into grass tile and vice versa). The function returns a joined `line_list`, wherein the initial `line_list` is the value of `line` and the updated `line_list`is the one changed through index checking and changing of values on the list. It also returns `moved` if the eggs shifted and `points` if the player accumulated points for moving.

### The `test.py` file
The `test.py` file contains the different test cases used to test the functions of the `mp1.py` file. You may check that it works through typing `pytest test.py`. You may insert a new test case by adding `assert function_name('input_depending_on_args') == correct_output` at the end of each function. The file imported the functions `separate_moves`, `step_shift_eggs_with_rules`, `tilt_grid`, and `apply_moves` from the `mp1.py` file. 

```python
def test_separate_moves():
    assert separate_moves('ZZZZZF') == ['f']
    assert separate_moves('') == []
    assert separate_moves('abcdefghijklmnopqrstuvwxyz') == ['b', 'f', 'l', 'r']
    assert separate_moves(1) == []
    assert separate_moves(' ') == []
    assert separate_moves('i am testing my input') == []
    assert separate_moves('i love cs 11 so much') == ['l']
    assert separate_moves('09176151201') == []
    assert separate_moves('us2 ko na magpasko yeah') == []
    assert separate_moves('lLfFrRbB') == ['l', 'l', 'f', 'f', 'r', 'r', 'b', 'b']
```
In the `test_separate_moves` function, there are several test cases wherein we checked if the `separate_moves` function works correctly for instances when a string of input (whether they are lowercase or uppercase, or with LBRF or none) is given or when a number or whitespace is given. When empty string, numbers, or whitespaces are given as input, the `separate_moves` returns an empty list, meaning that the function does not consider those inputs. Also, we checked if the function correctly extracts the LFRB letters in every possible input.
```python
def test_step_shift_with_eggs_with_rules():
    assert step_shift_eggs_with_rules('🟩🥚🟩', 0, 'left') == ('🥚🟩🟩', True, 0)
    assert step_shift_eggs_with_rules('🟩🥚🟩', 0, 'right') == ('🟩🟩🥚', True, 0)
    assert step_shift_eggs_with_rules('🍳🥚🟩', 0, 'left') == ('🍳🟩🟩', True, -5)
    assert step_shift_eggs_with_rules('🟩🥚🍳', 0, 'right') == ('🟩🟩🍳', True, -5)
    assert step_shift_eggs_with_rules('🪹🥚🟩', 0, 'left') == ('🪺🟩🟩', True, 10)
    assert step_shift_eggs_with_rules('🟩🥚🪹', 0, 'right') == ('🟩🟩🪺', True, 10)
    assert step_shift_eggs_with_rules('🪺🥚🟩', 0, 'left') == ('🪺🥚🟩', False, 0)
    assert step_shift_eggs_with_rules('🟩🥚🪺', 0, 'right') == ('🟩🥚🪺', False, 0)
    assert step_shift_eggs_with_rules('🥚🥚🟩', 0, 'left') == ('🥚🥚🟩', False, 0)
    assert step_shift_eggs_with_rules('🟩🥚🥚', 0, 'right') == ('🟩🥚🥚', False, 0)
    assert step_shift_eggs_with_rules('🟩🥚🥚🟩', 0, 'left') == ('🥚🥚🟩🟩', True, 0)
    assert step_shift_eggs_with_rules('🟩🥚🥚🟩', 0, 'right') == ('🟩🟩🥚🥚', True, 0)
    assert step_shift_eggs_with_rules('🪹🥚🥚🟩', 0, 'left') == ('🪺🥚🟩🟩', True, 10)
    assert step_shift_eggs_with_rules('🟩🥚🥚🪹', 0, 'right') == ('🟩🟩🥚🪺', True, 10)
    assert step_shift_eggs_with_rules('🪺🥚🥚🟩', 0, 'left') == ('🪺🥚🥚🟩', False, 0)
    assert step_shift_eggs_with_rules('🟩🥚🥚🪺', 0, 'right') == ('🟩🥚🥚🪺', False, 0)
    assert step_shift_eggs_with_rules('🍳🥚🥚🟩', 0, 'left') == ('🍳🥚🟩🟩', True, -5)
    assert step_shift_eggs_with_rules('🟩🥚🥚🍳', 0, 'right') == ('🟩🟩🥚🍳', True, -5)
    assert step_shift_eggs_with_rules('', 0, 'left') == ('', False, 0)
    assert step_shift_eggs_with_rules('', 0, 'right') == ('', False, 0)
```
In the `test_step_shift_eggs_with_rules` function, there are several test cases wherein we checked if the function correctly does the basic shifting such as left or right when there are only grass and eggs on the screen, penalty scenarios wherein there are frying pans involved, reward scenarios wherein there are empty nests involved, cases when there are two eggs and there is only one empty nests, cases when there are eggs and full nests (if the eggs will move or not), and empty strings if the rows do not have any icons. Note that the function `step_shift_eggs_with_rules` is a function that shifts the eggs one tile at a time (so if the frying pan is on the left, and there are three eggs moving to the left, only one egg will disappear as in the `mp1.py`, it is in the nested loop, one frame at a time). 
```python
def test_tilt_grid():
    assert tilt_grid([['🟩'], ['🟩'], ['🥚'],], 0, -1, 0) == ([['🥚'], ['🟩'], ['🟩']], 0)
    assert tilt_grid([['🪹'], ['🟩'], ['🥚'],], 0, -1, 0) == ([['🪺'], ['🟩'], ['🟩']], 10)
    assert tilt_grid([['🍳'], ['🟩'], ['🥚'],], 0, -1, 0) == ([['🍳'], ['🟩'], ['🟩']], -5)
    assert tilt_grid([['🥚'], ['🟩'], ['🥚'],], 0, -1, 0) == ([['🥚'], ['🥚'], ['🟩']], 0)
    assert tilt_grid([['🪺'], ['🟩'], ['🥚'],], 0, -1, 0) == ([['🪺'], ['🥚'], ['🟩']], 0)
    assert tilt_grid([['🥚'], ['🟩'], ['🟩'],], 0, 1, 0) == ([['🟩'], ['🟩'], ['🥚']], 0)
    assert tilt_grid([['🥚'], ['🟩'], ['🪹'],], 0, 1, 0) == ([['🟩'], ['🟩'], ['🪺']], 10)
    assert tilt_grid([['🥚'], ['🟩'], ['🍳'],], 0, 1, 0) == ([['🟩'], ['🟩'], ['🍳'], ], -5)
    assert tilt_grid([['🥚'], ['🟩'], ['🥚'],], 0, 1, 0) == ([['🟩'], ['🥚'], ['🥚']], 0)
    assert tilt_grid([['🥚'], ['🟩'], ['🪺'],], 0, 1, 0) == ([['🟩'], ['🥚'], ['🪺']], 0)
    assert tilt_grid([['🟩', '🟩', '🥚']], 0, 0, -1) == ([['🥚', '🟩', '🟩']], 0)
    assert tilt_grid([['🪹', '🟩', '🥚']], 0, 0, -1) == ([['🪺', '🟩', '🟩']], 10)
    assert tilt_grid([['🍳', '🟩', '🥚']], 0, 0, -1) == ([['🍳', '🟩', '🟩']], -5)
    assert tilt_grid([['🥚', '🟩', '🥚']], 0, 0, -1) == ([['🥚', '🥚', '🟩']], 0)
    assert tilt_grid([['🪺', '🟩', '🥚']], 0, 0, -1) == ([['🪺', '🥚', '🟩']], 0)
    assert tilt_grid([['🥚', '🟩', '🟩']], 0, 0, 1) == ([['🟩', '🟩', '🥚']], 0)
    assert tilt_grid([['🥚', '🟩', '🪹']], 0, 0, 1) == ([['🟩', '🟩', '🪺']], 10)
    assert tilt_grid([['🥚', '🟩', '🍳']], 0, 0, 1) == ([['🟩', '🟩', '🍳']], -5)
    assert tilt_grid([['🥚', '🟩', '🥚']], 0, 0, 1) == ([['🟩', '🥚', '🥚']], 0)
    assert tilt_grid([['🥚', '🟩', '🪺']], 0, 0, 1) == ([['🟩', '🥚', '🪺']], 0)
```
In the `test_tilt_grid` function, there are several test cases wherein we checked if the function correctly does the basic left, right, down, and up shifts in every scenario mentioned after this, penalty scenarios that involves frying pans, reward scenarios that involve empty nests, and scenarios that involve full nests. They were added as it was integral to the adherence to the game mechanics, and to make sure that the basic components of the game are correct in execution.
```python
def test_apply_move():
    assert apply_move([['🟩', '🟩', '🥚']], 'l', 0) == ([['🥚', '🟩', '🟩']], 0)
    assert apply_move([['🪹', '🟩', '🥚']], 'l', 0) == ([['🪺', '🟩', '🟩']], 10)
    assert apply_move([['🍳', '🟩', '🥚']], 'l', 0) == ([['🍳', '🟩', '🟩']], -5)
    assert apply_move([['🥚', '🟩', '🥚']], 'l', 0) == ([['🥚', '🥚', '🟩']], 0)
    assert apply_move([['🪺', '🟩', '🥚']], 'l', 0) == ([['🪺', '🥚', '🟩']], 0)
    assert apply_move([['🥚', '🟩', '🟩']], 'r', 0) == ([['🟩', '🟩', '🥚']], 0)
    assert apply_move([['🥚', '🟩', '🪹']], 'r', 0) == ([['🟩', '🟩', '🪺']], 10)
    assert apply_move([['🥚', '🟩', '🍳']], 'r', 0) == ([['🟩', '🟩', '🍳']], -5)
    assert apply_move([['🥚', '🟩', '🥚']], 'r', 0) == ([['🟩', '🥚', '🥚']], 0)
    assert apply_move([['🥚', '🟩', '🪺']], 'r', 0) == ([['🟩', '🥚', '🪺']], 0)
```
In the `test_apply_move` function, there are several test cases wherein we checked if the function correctly returns the expected output after applying a specific move depending on the players' input. There are basic test cases that checks the result of the function for different directions, penalty scenarios that involves eggs moving to frying pans, reward scenarios that involve eggs moving towards empty nests, and scenarios that involve eggs moving towards full nests. They were added to the set of test cases as they will check if the points are calculated correctly depending on where the egg lands, and if the correct icon was displayed at the end of every move.


### The `gui.py` file
The `gui.py` file contains the different functions that enable our team to create the main menu interface. To give an overview on how the whole file works, we used the `pygame` library to create features such as button and loading images onto the screen. The idea on how the file works is that the `gui.py` contains functions that represent the 'buttons' and their functionalities ('Play', 'Settings', 'Exit Game' and other buttons in the game). It is like a 'slideshow' presentation wherein when you click a button (like for example, 'Play'), you will be 'directed' to another frame or in Python sense, a new frame will be shown through the `screen.blit()` function which is seen across the document. Every function contains clickable buttons and event handling methods which will be explained further below.

```python
import pygame, sys
import game
import time
```
In this part of the code, libraries and modules were imported to make the main menu interface work. The `pygame` library was imported as it is one of the libraries in Python used to make games and its features. The `sys` module was imported to let the program interact with the system such as when the player wants to exit the game (removing the game screen on the system). The `game` module was imported as this represents `game.py` - the file used to load the game interface, as well as implementation of game mechanics such as adding the number of points, checking the remaining number of moves, and others. In the `gui.py` file, the `game` module is mostly used to call the function `start_with_gui_level()` in `game.py`, which opens the files such as `level1.in`  which are used to set-up the game itself. The `time` module was used to make the program wait or delay for seconds. This is primarily used in the `loading()` function in `gui.py` wherein the program shows a loading screen in the monitor.

```python
#For setting up the game
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Egg Roll')

#For setting the game icon of the game
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

#For setting the screen resolution of the game
screen = pygame.display.set_mode((960, 768),0,32)
```
This block of code is for the setting up of the game itself. The `pygame.time.Clock()` creates a clock object to be used in functions where time delays are needed. The `from pygame.locals import *` is for importing constants from `pygame` library such as `KEYDOWN` and `QUIT` for managing inputs like arrow keys and letter keys.  The `pygame.display.set_caption('Egg Roll')` sets the name of the game window to 'Egg Roll'. The icon for the game is located on the `images` folder, and the `pygame.display.set_icon()` function displays the `icon.png` on the taskbar whenever the game is opened. The `pygame.display.set_mode()` function makes the resolution of the game to be set to 960 x 768. All the frames used for the game were set to this resolution.

```python
# Images or frames used for the game
main_menu_light = pygame.image.load('images/main_menu_light.png')
levels_light = pygame.image.load('images/levels_light.png')
loading_1_light = pygame.image.load('images/loading_1_light.png')
...
sure_dark = pygame.image.load('images/sure_dark.png')
```

The block of code above is for assigning the object or picture being loaded into variables. As seen in the code, `pygame.image.load()` is primarily used to load the images and frames for the interfaces of the game. These frames are stored in the `images` folder. When you just put the filename as the argument, the game will not load and the terminal will tell you that the images are not in the current directory or folder. The variables are also named according to whether the frames are for light or dark mode.
```python
# Transparent Buttons for the Game
transparent_play_button = pygame.Surface((285,90), pygame.SRCALPHA)
#transparent_play_button.fill((255,0,0,128))
...
transparent_no_button = pygame.Surface((260,80), pygame.SRCALPHA)
#transparent_no_button.fill((255,0,0,128))
```
This block of code is for assigning the rectangle button objects to variables. The `pygame.Surface()` creates a rectangle shape on the interfaces of the game with the width and height as its arguments (for the size of the rectangle).  The `pygame.SRCALPHA` is called for the rectangles to be transparent. Without it, the rectangles will be shown alongside with the game frames. These rectangles will be used as buttons so that when the players click on a specific button like 'Settings', they are directed to the Settings Menu. You can also see the `transparent_no_button.fill()` function being commented out as it was a way for us to check if the buttons were properly placed - we cannot just make it transparent as it will be hard for us to determine if they are placed correctly and if they are working properly.

Before explaining each function in the file, there are certain code blocks that are seen across the functions that are responsible for **creating clickable buttons** and **event handling**.

```python
# An excerpt from the main_menu() function
# For creating CLICKABLE BUTTONS
position_x, position_y = pygame.mouse.get_pos()
...
exit_game_button = pygame.Rect(590, 570, 310, 90)
...   
if exit_game_button.collidepoint((position_x, position_y)):
    if click:
        settings(mode)
...
screen.blit(transparent_exit_game_button, (590, 570))
```
This particular code block is seen across functions in different variations. This code block is responsible for creating clickable buttons, as well as making sure that an action is done when these buttons are clicked. The one with the `pygame.mouse.get_pos()` is responsible for finding the position of the mouse pointer on the game screen, and this position are saved as `position_x` and `position_y`. Every rectangular area is made by `pygame.Rect()` which has four arguments: starting x position, starting y position, width, and height. These rectangle areas are saved in variables such as `exit_game_button`.  There are also `if` statements with the function `.collidepoint()` with `position_x` and `position_y` as its argument. These statements check if the mouse pointer is within the rectangular area of the button and if the area is clicked on the mouse. Once clicked, a new frame will be shown on the screen as other functions will be called such as `settings(mode)`. The one with the `screen.blit(transparent....,(590,570))` makes the transparent buttons be on the screen so that there will be buttons that the players can click. It takes in two arguments, the starting x and starting y position.
```python
# An excerpt from the main_menu() function
# For creating EVENT HANDLING
		click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
```
The block of code above is responsible for event handling. Each function has this block of code, wherein it checks if there are specific keys in the `if` statements that are clicked. For instance, if the `X` on the top of the game window is clicked, the program will stop; if the left key on the mouse is clicked, the click will be equal to `True` -- meaning that a specific button is clicked; and if the `ESC` button is clicked, the game window will disappear and quit.
```python
def main_menu(mode = 'light'):
    click = False
    while True:
        if mode == "light":
            screen.blit(main_menu_light, (0, 0))
        else:
            screen.blit(main_menu_dark, (0, 0))
	...
	pygame.display.update()
	mainClock.tick(60)	
```
The `main_menu` function is responsible for showing the main menu interface. It accepts a single argument: `mode` which as a default value `"light"` meaning that the game will load the light mode of the main menu interface by default, and when it is called again in other functions with `mode = "dark"`, it will show the dark mode. The screen will then be updated by the `.display.update()` function and the `.tick()` function is responsible for the frame per second to be passed when updating the screen.
```python
def levels(mode = "light", tutorials = "no"):
    click = False
    running = True
    while running:
        if mode == "light" and tutorials == "no":
            screen.blit(levels_light,(0,0))
        elif mode == "light" and tutorials == "yes":
            screen.blit(tutorials_light, (0,0))
        elif mode != "light" and tutorials == "no":
            screen.blit(levels_dark,(0,0))
        elif mode != "light" and tutorials == "yes":
            screen.blit(tutorials_dark,(0,0))	
    ...
	pygame.display.update()
	mainClock.tick(60)	
```

The `levels()` function is responsible for displaying the level selector interface for the main levels and tutorial levels, depending on the mode (light or dark) and if the function is called with yes or no as the tutorial. The function has two default values, `mode = "light"` and `tutorials = "no"`, meaning that it loads the main level selector in the light mode as default. This function is called mainly in the `main_menu` function wherein when the player clicks the Play button, the said function will call the `levels` function. 

```python
def loading(file, mode = "light", tutorials = "no"):
    running = True
    while running:
        if file == 1:
            if mode == "light":
                screen.blit(loading_1_light,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial1.in")
                else: 
                    game.start_gui_with_level("level1.in")
            else:
                screen.blit(loading_1_dark,(0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                if tutorials != "no":
                    game.start_gui_with_level("tutorial1.in", mode)
                else: 
                    game.start_gui_with_level("level1.in", mode)

    ...
	pygame.display.update()
	mainClock.tick(60)	
```

The `loading` function is responsible for the loading screen through `screen.blit(image_name, (0,0))` for 5 seconds through `pygame.time.wait(5000)`, as well as the game interface itself through calling `game.start_gui_with_level(filename)` wherein the `game.start_gui_with_level()` function means that the `start_gui_with_level()` function from the `game.py` is called, which basically loads the game interface. The code block consists of several `if` statements which checks the value of the filename - which corresponds to what level of the game is asked and also checks if the level being asked is a tutorial level or not.
```python
def settings(mode = "light"):
    click = False
    running = True
    while running:
        if mode == "light":
            screen.blit(settings_light,(0,0))
        else:
            screen.blit(settings_dark,(0,0))
    ...
	pygame.display.update()
	mainClock.tick(60)	
```
The `settings` function loads the settings interface. When called, it has the default value `mode = "light"`, meaning that the default settings interface is in light mode. It also has sections in the code that creates clickable buttons and event handling.
```python
def control_keys_or_credits(mode = "light", use = "control_keys"): 
    running = True
    click = False
    while running:
        if mode == "light" and use == "control_keys":
            screen.blit(control_keys_light,(0,0))
        elif mode != "light" and use == "control_keys":
            screen.blit(control_keys_dark, (0,0))
        elif mode == "light" and use != "control_keys":
            screen.blit(credits_light,(0,0))
        else:
            screen.blit(credits_dark,(0,0))
	pygame.display.update()
	mainClock.tick(60)	
```
The `control_keys_or_credits` function loads either the control keys interface or the credits interface, depending if the function has only 0-1 arguments or if the mode is set to `"control_keys"` or `"credits"`. We combined the loading of credits and control keys interface since they have the same interface with different contents. The `if` statements handle whether the one being loaded on the screen is the control keys or the credits interface and whether they will be in light or dark mode. Same as the other functions, it also has sections in the code that creates clickable buttons and event handling.
```python
def exit_game(mode = "light"):
    running = True
    click = False
    while running:
        if mode == "light":
            screen.blit(sure_light,(0,0))
        else:
            screen.blit(sure_dark,(0,0))
    ...
	pygame.display.update()
	mainClock.tick(60)	
```
The `exit_game` function loads the confirmation screen if the player clicked the Exit Game button at the main menu interface. It accepts one argument: `mode` which has the default value `"light"`, meaning that if the `exit_game` is called under the `main_menu` function with 0-1 argument, provided that when 1 argument is used (`"light"`), it will show the light mode of the confirmation screen. When the Yes button is clicked, it will exit the game, and clicking the No button will call the `main_menu()` function with the argument `mode` that depends on the mode passed onto the `exit_game` function.  Same as the other functions, it also has sections in the code that creates clickable buttons and event handling.

    main_menu()
This is at the last part of the `gui.py` code which is important since when `python3 gui.py` is called, it will show the main menu interface. If this is removed, the main menu will not show up.


### The `game.py` file
The `game.py` file contains the different functions that enable our team to create the game interface. To give an overview on how the whole file works, we used the `pygame` library to create features such as button and loading images onto the screen. The `game.py` shows the different assets or the icons used to load the nests, eggs, etc. on the game screen through calling `screen.blit()` across the document. It also contains the logic behind how the points are calculated and to determine if the game is over or not.
```python
import pygame
import sys
from pygame.locals import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_f, K_b, K_l, K_r, QUIT, K_DELETE
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 768
FPS = 60
```
The code block above imports `pygame` as it is the library used for loading screen frames, `sys` for system commands such as quitting the game, and `KEYDOWN, K_UP, and others` as they will be used in the `start_with_gui_level()` function to detect if the keys clicked on the keyboard are the letter keys or the arrow keys for the game to progress. It also contains the global variables for the screen width, screen height, and frame per second which are the basis to the screen resolution of the game. We used 960 x 768 pixels as it is not large (or wide enough) but it is also not small. We also used 60 frames per second as it is one of the most common FPS in games.
```python
game_light = pygame.image.load('images/game_light.png')
game_dark = pygame.image.load('images/game_dark.png')
win_light = pygame.image.load('images/win_light.png')
win_dark = pygame.image.load('images/win_dark.png')
lose_light = pygame.image.load('images/lose_light.png')
lose_dark = pygame.image.load('images/lose_dark.png')
```
The block of code above assigns the pictures on the `images` folder loaded via `pygame.image.load()` into variables. This is important as it will be used in the `start_gui_with_level()` function on loading the game interface screen and the frames that show you if you win or lose the game.
```python
def load_assets():
    assets = {
        "egg": pygame.image.load("assets/egg.png"),
        "nest": pygame.image.load("assets/nest.png"),
        ...
    }
    for key, image in assets.items():
        assets[key] = pygame.transform.scale(image, (81, 81))
    return assets
```
The `load_assets` function is responsible for loading the icons in the game such as the eggs, grass, walls, frying pans, and nests. It has a dictionary `assets` that has strings of the description of the icons as the keys and the object being loaded via `pygame.image.load()` as the values. These objects or images will be scaled down to 81 by 81 pixels via the `pygame.transform.scale`, and the function will return a dictionary of these scaled images.
```python
def display_grid(screen, grid, assets):
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            x, y = col_idx * 27, row_idx * 27
            if cell == '🥚':
                screen.blit(assets['egg'], (x, y))
            ...
```
The `display_grid` function is responsible for displaying the grid of the ones in the `.in` files and the grids on the `.in` files will then be represented by every value in the dictionary `assets` through series of `if` statements. It accepts three arguments: `screen` which pertains to the game screen with width and height which will be defined on the `start_with_gui_level` function, the `grid` which will be also defined in the said function as it will be saved by calling the `load_level` function, and the `assets` which will be defined as the `start_with_gui_level` calls `display_grid`.  The nested `for` loops iterate each row first through the `for row_idx...` and column through `for col_idx...`. The x and y are the basis for the starting position where the assets or icons will be placed. The multiplier here is 27 since through trial and error, we observed that the width and height of every cell or icon must be 1/3 of the dimension of the scaled assets or icons in the `display_grid` function (81 x 81). The nested loops are responsible for iterating every row and every column of the `grid`, filling the cells or the square areas with the icons in the `assets` (substituting eggs emoji with the image of an egg for example).

```python
def load_level(filename):
    with open(filename, encoding="utf-8") as file:
        num_rows = int(file.readline().strip())
        num_moves = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(num_rows)]
    return grid, num_moves, 0
```
The `load_level` function is responsible for loading the files in `.in` format. It accepts `filename` path as the argument. The function then opens the file in UTF-8 format using `with open... as file`. The first line of the file is saved as `num_rows`, the second line as `num_moves`, and the next remaining lines are saved as a list of lines in the variable `grid`. The function returns the `grid` as a list of lines of emojis, `num_moves` representing the number of moves available, and `0` since it will be saved as the initial point or score in the `start_gui_with_level` function.
```python
def apply_move(grid, move, points):
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
```
The `apply_move` function accepts three arguments: `grid` which is defined when `apply_move` is called by the `start_gui_with_level` (the grid is the list of lines containing emojis from the `.in` files), `move` which can be `'f'`, `'l'`, `b`, or `r`, and `points` which is the initial score before moving the icons on the desired direction. It saves the initial grid in the `prev_grid` variable as a list of rows of emojis. There will be `if` statements that check your `move` value. Depending on the `move` value, it will call `tilt_grid` to tilt the cells on the grid, getting the updated grid and points. At the end of the function, it will then check if the updated grid is equal to the initial grid. If `True`, it will return the initial grid, initial points, and `False` -- signifying that there will be no movement. Otherwise, it will return the updated grid, updated points, and `True` -- signifying that some cells have shifted.
```python
def tilt_grid(grid, points, dx, dy):
    num_rows = len(grid)
    num_cols = len(grid[0])
    moved = True

    while moved:
        moved = False
        new_grid = [row[:] for row in grid]

        if dx == 0 and dy != 0:  
            for r in range(num_rows):
                row = ''.join(grid[r])
                if dy == -1: 
                    shifted_row, row_moved, updated_points = step_shift_eggs_with_rules(row, points, 'left')
                elif dy == 1:
                    shifted_row, row_moved, updated_points = step_shift_eggs_with_rules(row, points, 'right')
                new_grid[r] = list(shifted_row)
                points = updated_points
                moved = moved or row_moved
             ...
             ...
             ...
             ...
    return grid, points             
```
The `tilt_grid` function is similar to the one in the `mp1.py` and it accepts four arguments: `grid` which is the initial grid from the `apply_move` function, `points` which is the initial score from the `apply_move` function, `dx` is the vertical movement where `-1` tilts the grid up while `1` tilts the grid down, and `dy` is the horizontal movement where`-1` tilts the grid left while `1` tilts the grid right. It contains a while loop where the `new_grid` is created as a storage for the updated grid and `moved = False` is added so that if there are still cells or eggs that can still move, the egg will still move, making the `moved = True` in the later part of the code block. The code block will then check for the values of `dx` and `dy`. If the `dy != 0 and dx = 0`, it will check if the `dy` is equal to `-1` or `1`. Depending on `dy`, it will then call the function `step_shift_eggs_with_rules` to move the eggs to either left or right. The same goes to the condition if `dy = 0 and dx != 0` wherein if `dx` is equal to `-1` or `1`, it will call the function `step_shift_eggs_with_rules` to move the eggs to either up or down. For every iteration of row or column, the `new_grid` is then updated, and the `moved` is updated depending on whether a row or a column moved. The function will then return the updated grid and points.

```python
def step_shift_eggs_with_rules(line, points, direction):
    grass = '🟩'
    frying_pan = '🍳'
    nest = '🪹'
    full_nest = '🪺'
    line_list = list(line)
    moved = False

    if direction == 'left':
        for i in range(1, len(line_list)):
            if line_list[i] == '🥚':
                if line_list[i - 1] == frying_pan: 
                    line_list[i] = grass
                    moved = True
                    points -= 5
                elif line_list[i - 1] == nest: 
                    line_list[i - 1] = full_nest
                    line_list[i] = grass
                    moved = True
                    points += 10
                elif line_list[i - 1] == grass: 
                    line_list[i - 1], line_list[i] = line_list[i], grass
                    moved = True
    ...
    ...
    ...
    return ''.join(line_list), moved, points
```
The `step_shift_eggs_with_rules` function is similar to the one in the `mp1.py` and it is responsible for shifting the eggs to the left, right, up, or down depending on the argument `direction`. It has three arguments: `line` which is either a row or a column, `points` which is the initial points, and `direction`. It has variables for every emoji of grass, eggs, etc, and a variable `moved = False` which will be changed if the eggs in the `line` shifted, determining the `moved_any` on the `tilt_grid` function. The code block contains `if` statements depending on the `direction`, and it usually checks if the `frying_pan` is on the `direction` of the `egg` (which changes the egg tile into grass tile), or if the `nest` that is empty is on the direction of the egg (which changes the nest into a full nest), or if the `grass` is next to the egg (which changes the egg tile into grass tile and vice versa). The function returns a joined `line_list`, wherein the initial `line_list` is the value of `line` and the updated `line_list`is the one changed through index checking and changing of values on the list. It also returns `moved` if the eggs shifted and `points` if the player accumulated points for moving.

```python
def is_game_over(grid, num_moves):
    empty_nests = sum(row.count('🪹') for row in grid)
    eggs = sum(row.count('🥚') for row in grid)
    return empty_nests == 0 or eggs == 0 or num_moves == 0
```
The `is_game_over` function checks if the game is over by checking whether the `empty_nests == 0`, `eggs == 0`, or `num_moves == 0` through the function `.count()`. In the `empty_nests`, the count of empty nests will be checked for every row, and their sum will be added. Same goes for the `eggs` where the count of the eggs will be checked in every row. The function returns `True` if either the empty nests, eggs, or number of moves count is 0 and `False` if otherwise.
```python
def check_if_win_or_lose(grid):
    empty_nests = sum(row.count('🪹') for row in grid)
    if empty_nests == 0:
        return True
    else:
        return False
```
The `check_if_win_or_lose` function checks if at the end of the movement (or gaming session), the player loses or wins by checking the sum of the count of empty nests per row which is saved in the `empty nests` variable. If `empty_nests == 0`, the function returns `True`, signifying that the player wins the game, and `False` if otherwise, signifying that the player loses the game.
```python
def start_gui_with_level(filename, mode="light"):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ...
```
The `start_gui_with_level` function is responsible for doing everything that involves the `.in` files: from loading the files, applying the moves, checking if the game is over, and others by calling several functions throughout the `game.py` file. It starts by initializing the `pygame` through `pygame.init()`, the screen with width and height, the caption for the game window, and the clock for the time within the game (for the frame per second). The function accepts two arguments: the `filename` which is a path of the file and the `mode` (the default is `"light"`, and calling the function with one argument means that the function will load the game screen in light mode). The `load_assets` will then be called so that there will be scaled icons saved in `assets` variable. The file is then loaded by calling the `load_level` function, extracting the `grid`, number of moves, and initial points. It has a while loop which checks for every event or action that the player does on the keyboard or the game window. The `if` statements with the `KEYDOWN` and other conditions with `K` is for checking every event or action on the keyboard. If the X on the game window is pressed, the game window disappears. Pressing the `UP` arrow key or `F` calls the function `apply_move` with `'f'` as its `direction`, pressing the `DOWN`arrow key or `B` calls the function `apply_move` with `'b'` as its `direction`, pressing the `LEFT` arrow key or `L` calls the function `apply_move` with `'l'` as its `direction`, and pressing the `RIGHT` arrow key or `R` calls the function `apply_move` with `'r'` as its `direction`. The movement done is then appended on the `prev_moves`. The screen is shown through the `screen.blit(...)` call, which shows the light mode of the game interface if the `mode = "light"` and dark mode if `mode = "dark"`.  The function `display_grid` is called to display the contents of the file, substituting every emojis into their corresponding icons in the `assets`. The previous moves, number of moves available, and points are displayed through the code below. Note that the previous moves will only be shown the `prev_moves` is not an empty list.
```python
        if prev_moves == []:
            pass
        else:
            prev_moves_text = font.render(f"{''.join(prev_moves)}", True, (121,78,7))
            screen.blit(prev_moves_text, (315,583))
        moves_text = font.render(f"{num_moves}", True, (121, 78, 7))
        screen.blit(moves_text, (315,623))
        points_text = font.render(f"{points}", True, (121, 78, 7))
        screen.blit(points_text, (315, 668))
```
The `font.render()` is responsible for making a text object with arguments `str`, `bool` for smooth display of texts, and `(a,b,c)` representing the RGB code for the color of the text. The `is_game_over` is then called through `if` statements for every round to check if the game is over. After checking if the game was over, the `check_if_win_or_lose` is called to check if the player wins or lose which is used to determine what frame and texts to display (through `pygame.display.flip()`) on the screen. 

### The `assets` folder
The `assets` folder contains the icons for the empty nests, full nests, eggs, grass, walls, and frying pans to be used in the game interface. All of these icons were made using Canva elements.
 
### The `images` folder
The `images` folder contains the frames that we used in both the main menu and game interface. These frames were used in several features in the game such as the main menu itself, the level selector as you click the 'Play' button, the night mode frames, and many more. These frames were also made using Canva elements and the theme/palette for the design of the game is *Spring Color Palette* which incorporates colors such as green, yellow, brown, and orange that symbolize growth and enjoyment as the players immerse in the game.

### The `readme_docs` folder
The `readme_docs` folder contains other images used in the `README.md` file.

## Bonus Features
This section contains the bonus features that were implemented in the game. The game is supposed to be a simple terminal version, but the developers added features to improve the gaming experience. The following below contains these bonus features:
- Adding a main menu
- A fancier main menu interface using Canva and `pygame` library
- A fancier game interface using Canva and `pygame` library
- Adding multiple levels
- Adding levels selector
- Adding tutorial levels
- Adding tutorial levels selector
- Adding an icon for the game to be seen in the taskbar as you open the game (seen in the picture below)
![Icon on taskbar](/readme_docs/proof_of_icon.png)
- Integrating inputs such as arrow keys, lowercase letters, and uppercase letters (for L, R, F, and B) for easier gaming experience for players who are used to arrow keys
- Adding a settings menu
- Adding a night mode feature on both main menu and game interface
- Inclusion of control keys in the settings menu 
- Inclusion of credits in the settings menu
- Adding the main menu button on the level selectors 
- Adding the main menu button on the settings menu
- Adding the settings button on the tutorial level selectors
- Adding a loading screen in both levels and tutorial levels before loading the actual game interface
- Adding an exit game button on the main menu interface
- Adding a confirmation message as the player clicks the exit game button on the main menu interface
- Ability to see the previous moves made by the player in the game interface
- Ability to see the number of remaining moves that the player still has
- Ability to see the score that the player gains
- Adding the control keys in the game interface for players to be guided on what keys to click
- Adding the objective of the game under the control keys in the game interface for players to be informed of what they should be aiming in the game
- Adding the prompt to let the players know that they can use the `DELETE` key on their keyboard to restart their game
- Ability to restart the game via the `DELETE` key in the keyboard
- Showing on the screen that the players win or lose the level depending if they put all the eggs on the basket or not
## For Future Developers
This section contains the possible features or improvements that (future) developers may want to implement in the game. The list below contains the fixes or improvements that can be (or may be) added to the game in the future:
- Adding background music to the main menu and game interface
- Adding sound effects on clicking the buttons
- Adding sound effects when eggs are put in the frying pan
- Adding sound effects when eggs move
- Adding challenging levels to the game
- Adding buttons to restart the game in the game interface
- Adding buttons that direct to the levels or main menu in the game interface
- Adding a storyline to enhance the gaming experience
- Ability to undo moves
- Adding a power-up (like when an egg goes to a tile, that egg will have a 2x multiplier as it goes to a nest)
- Adding options that provide hints to the player 
- Adding in-game currency that the players can use to buy boosts such as 2x multiplier, adding hints, buying mode displays other than night mode, etc.
- Adding leaderboard so that the players can track their progress
- Adding a feature where players can know if they did the actual solution / if they achieved the intended highest possible score
- Adding an online leaderboard where players can battle each other on their scores (with rules like players will lose points the more that they have more tries solving the game)

Also, for developers, you may also run the game on terminal mode using WSL terminal by typing `python3 mp1.py <level filename>` and choose the appropriate filename in the folder. Moreover, to test the program, you may type `pytest test.py` since the file `mp1.py` file contains the test cases for the `mp1.py` file.

## Release and Patch Notes
This section contains the release and patch notes made by the developers of this game to fix minor bugs and improve the gaming experience of the users.
- **Version: 1.0.1**
  - (12/10/2024) Minor fixes have been made on the logic of the code in `gui.py`, as well as the resolution of the game. The game designs in `level4.in`, `level5.in`, and `tutorial4.in` were slightly fixed to ensure that the players will be able to put the eggs on all nests. 
## Acknowledgements and Task Delegations
This section shows the task delegations and acknowledgements of the team who created this project.

 - **John Harry Arciga**
   - Making of the `gui.py` file
   - Making of the `game.py` file
   - Editing of the `mp1.py` file
   - Making and editing of the `test.py` file
   - Making of the graphics for the game itself
   - Adding the [bonus features](#bonus-features)
   - Making the `README.md` documentation file
   - Compiling the images in the `assets`, `images`, and `readme_docs` folder
   - Doing the [release and patch notes](#release-and-patch-notes)
   
 - **David Pagaduan**
   - Making of the test cases to be put in the `test.py` file
   - Making the `mp1.py` file



We would like to thank our CS 11 instructors for teaching us the fundamentals of programming. We would also like to thank everyone who plays (and will play) this game in making this project serve its purpose: to provide enjoyment and fulfillment to the hearts of the gamers. Together, let us keep it rolling!
