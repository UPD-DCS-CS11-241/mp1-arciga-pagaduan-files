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
      - [mp1.py](#mp1-py)
      - [test.py](#test-py)
      - [gui.py](#gui-py)
      - [game.py](#game-py)
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
This section contains the code documentation and explanation of the `.py` files that are important for this project.
> This part is not yet finished.
### `mp1.py`
### `test.py`
### `gui.py`
### `game.py`

## Bonus Features
This section contains the bonus features that were implemented in the game. The game is supposed to be a simple terminal version, but the developers added features to improve the gaming experience. The following below contains these bonus features:
- Adding a main menu
- A fancier main menu interface using Canva and `pygame` library
- A fancier game interface using Canva and `pygame` library
- Adding multiple levels
- Adding levels selector
- Adding tutorial levels
- Adding tutorial levels selector
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
