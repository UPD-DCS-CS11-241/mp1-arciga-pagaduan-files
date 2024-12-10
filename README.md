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
This section contains the code documentation and explanation of the `.py` files that are important for this project. The main library used for this project are the `pygame` library for the graphical user interface (GUI) and `pytest` library for the testing of the files.
> This part is not yet finished.

### The `mp1.py` file
Content


### The `test.py` file
Content


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
# For creating clickable buttons
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
This particular code block is seen across functions in different variations. This code block is responsible for creating clickable buttons, as well as making sure that an action is done when these buttons are clicked. The one with the `pygame.mouse.get_pos()` is responsible for finding the position of the mouse pointer on the game screen, and this position are saved as `position_x` and `position_y`. 

> To be continued

```python
def main_menu(mode = 'light'):
    click = False
    while True:
        if mode == "light":
            screen.blit(main_menu_light, (0, 0))
        else:
            screen.blit(main_menu_dark, (0, 0))
            
        position_x, position_y = pygame.mouse.get_pos()   
		...
        exit_game_button = pygame.Rect(590, 570, 310, 90)
...
screen.blit(transparent_exit_game_button, (590, 570))	
```
The `enter code here`


### The `game.py` file
Content

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
