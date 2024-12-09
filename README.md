# Welcome to Egg Roll!

Good day! Are you egg-cited to play the greatest game of all time? If you are seeing this, this is your sign to roll with us in ***Egg Roll***.

**Egg Roll** is a 2D puzzle game that aims to put the eggs on all nests. Several eggs are scattered throughout the screen, and by performing a series of tilts and directions, you will be able to roll the eggs on their respective nests. But beware: you should avoid getting all your eggs into the frying pan as it will lower your points. 

What are you waiting for? Let's get rolling!

# Overview
Here are the contents of the user manual / documentation:

 1. [Getting Started](#getting-started)
 2. [Opening the Game](#opening-the-game)
 3. [Navigating the Game Interface](#navigating-the-game-interface)
 4. [Game Levels](#game-levels)
 5. [For Instructors and Developers](#for-instructors-and-developers)


# Getting Started

Before playing the game, here are the prerequisites or steps that you should follow to setup your device and ensure a smooth experience in playing the game: 

 1. Make sure that you are using Windows 10 or higher that supports WSL. If so, click on the Windows Icon 🪟 and search for **`Command Prompt`** in the Start Menu. Right-click it and select **`Run as administrator`**. Click **`Yes`** to gain rights to install WSL in your computer.

 2.   Install WSL on your computer / PC through **`Command Prompt`** or **`Windows Powershell`**. Type **`wsl --install`** in your terminal. This will install WSL which has the terminal to create the commands needed to run the game. After installing, you may be asked for your username and password. 

 3. In your WSL terminal, type **`sudo apt update`** followed by **`sudo apt install python3.12`** to install Python in your WSL system. To verify if you already installed Python, type **`python3 --version`** in your terminal. It should show you something like **`Python 3.12.7`** in your screen - this means you have Python in version 3.12.7.

 4. Also, type **`pip install pygame`** to install PyGame. This is the third-party library that is utilized for the game program.

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
![Main Menu Interface](/images/main-menu-light.png)

In this section, we will be navigating the Egg Roll interface.  The picture above shows the `Main Menu` interface of the game. It has three buttons: [`Play`](##play), [`Settings`](##settings), and [`Exit Game`](##exit-game) which will be explained in the next sections.

## Play
![Levels Interface](/images/levels_light.png)

As you click the `Play` button, you can see the interface (just like the one shown above) containing the levels for the game. It also has the `Main Menu` button to go back to the main menu of the game.

There are five levels named: *U-Turn, Shake It Off, Mitosis, Clockwise,* and *Into The Void*. When you click a level here (example: U-Turn), a loading screen will be shown which directs you to the game itself *(as shown in the pictures below).*

![Loading Screen Interface](/images/loading_1_light.png)

![Game Interface](/readme_docs/game_interface.png)


More details on these levels, as well as the mechanics and solutions, are shown in the [Game Levels](#game-levels) section.

# Game Levels
1. Content
 
# For Instructors and Developers
1. Content
 
