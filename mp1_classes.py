"""
The mp1_classes.py file is for creating classes
that define the different movements and 
emojis used for the creation of the game.
These classes will then be used for the mp1.py
file, specifically for the apply_move and
shift_eggs functions.

"""
from typing import Optional, Literal
from dataclasses import dataclass
import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_ESCAPE, K_DELETE # pylint: disable=no-name-in-module

@dataclass
class Moves:
    """
    This class is for defining the leftward,
    rightward, forward, and backward movements 
    to be used for the apply_move function in
    the mp1.py file.
    
    """
    leftward: str = 'l'
    rightward: str = 'r'
    forward: str = 'f'
    backward: str = 'b'


@dataclass
class Board:
    """
    This class is for defining the wall, grass,
    pan, egg, empty nest, and full nest emojis
    to be used for the shift_eggs function in 
    the mp1.py file.
    
    """
    wall: str = '🧱'
    grass: str = '🟩'
    pan: str = '🍳'
    egg: str = '🥚'
    empty_nest: str = '🪹'
    full_nest: str = '🪺'

@dataclass
class LevelsLightImages:
    """
    The class Levels_Light_Images is for assigning the object or picture 
    for the main menu, level selector, and loading screens into variables. 
    As seen in the code, pygame.image.load() is primarily used to load 
    the images and frames for the interfaces of the game. These frames are 
    stored in the images folder. When you just put the filename as the argument, 
    the game will not load and the terminal will tell you that the 
    images are not in the current directory or folder. The variables 
    are also named according to whether the frames are for light or 
    dark mode.

    """
    # These are the images for the light mode.
    main_menu_light: pygame.Surface = pygame.image.load('images/main_menu_light.png')

    levels_light: pygame.Surface = pygame.image.load('images/levels_light.png')
    loading_1_light: pygame.Surface = pygame.image.load('images/loading_1_light.png')
    loading_2_light: pygame.Surface = pygame.image.load('images/loading_2_light.png')
    loading_3_light: pygame.Surface = pygame.image.load('images/loading_3_light.png')
    loading_4_light: pygame.Surface = pygame.image.load('images/loading_4_light.png')
    loading_5_light: pygame.Surface = pygame.image.load('images/loading_5_light.png')


@dataclass
class SettingsLightImages:
    """
    The class Settings_Light_Images is for assigning the object or picture 
    for the settings, tutorials, leaderboard, etc. into variables. As seen in 
    the code, pygame.image.load() is primarily used to load the images and frames 
    for the interfaces of the game. These frames are stored in the images 
    folder. When you just put the filename as the argument, the 
    game will not load and the terminal will tell you that the 
    images are not in the current directory or folder. The variables 
    are also named according to whether the frames are for light or 
    dark mode.

    """
    # These are the images for the light mode.
    settings_light: pygame.Surface = pygame.image.load('images/settings_light.png')
    tutorials_light: pygame.Surface = pygame.image.load('images/tutorials_light.png')
    leaderboard_light: pygame.Surface = pygame.image.load('images/leaderboard_light.png')
    control_keys_light: pygame.Surface = pygame.image.load('images/control_keys_light.png')
    credits_light: pygame.Surface = pygame.image.load('images/credits_light.png')

    sure_light: pygame.Surface = pygame.image.load('images/sure_light.png')


@dataclass
class LevelsDarkImages:
    """
    The class Levels_Dark_Images is for assigning the object or picture 
    for the main menu, level selector, and loading screens into variables. 
    As seen in the code, pygame.image.load() is primarily used to 
    load the images and frames for the interfaces of the game. These 
    frames are stored in the images folder. When you just put the 
    filename as the argument, the game will not load and the terminal 
    will tell you that the images are not in the current directory or 
    folder. The variables are also named according to whether the frames 
    are for light or dark mode.

    """
    # These are the images for the dark mode.
    main_menu_dark: pygame.Surface = pygame.image.load('images/main_menu_dark.png')

    levels_dark: pygame.Surface = pygame.image.load('images/levels_dark.png')
    loading_1_dark: pygame.Surface = pygame.image.load('images/loading_1_dark.png')
    loading_2_dark: pygame.Surface = pygame.image.load('images/loading_2_dark.png')
    loading_3_dark: pygame.Surface = pygame.image.load('images/loading_3_dark.png')
    loading_4_dark: pygame.Surface = pygame.image.load('images/loading_4_dark.png')
    loading_5_dark: pygame.Surface = pygame.image.load('images/loading_5_dark.png')


@dataclass
class SettingsDarkImages:
    """
    The class Settings_Dark_Images is for assigning the object or picture 
    for the settings, tutorials, leaderboard, etc. into variables. 
    As seen in the code, pygame.image.load() is primarily used to 
    load the images and frames for the interfaces of the game. These 
    frames are stored in the images folder. When you just put the 
    filename as the argument, the game will not load and the terminal 
    will tell you that the images are not in the current directory or 
    folder. The variables are also named according to whether the frames 
    are for light or dark mode.

    """
    # These are the images for the dark mode.
    settings_dark: pygame.Surface = pygame.image.load('images/settings_dark.png')
    tutorials_dark: pygame.Surface = pygame.image.load('images/tutorials_dark.png')
    leaderboard_dark: pygame.Surface = pygame.image.load('images/leaderboard_dark.png')
    control_keys_dark: pygame.Surface = pygame.image.load('images/control_keys_dark.png')
    credits_dark: pygame.Surface = pygame.image.load('images/credits_dark.png')

    sure_dark: pygame.Surface = pygame.image.load('images/sure_dark.png')


class EventHandler:
    """
    This class is for handling event handling of the gui.py which makes
    the code in the gui.py much cleaner and simpler.

    """
    def __init__(self) -> None:
        """
        This is for initializing the click (for almost all functions
        of the gui.py code and active_level (for the leaderboard 
        function of the gui.py code). 

        """
        self.click: bool = False
        self.active_level: Optional[str] = None # This is for the leaderboard function

    def process_events(self,
        function: Literal["main_menu",
        "levels",
        "settings",
        "leaderboard",
        "control",
        "exit",
        "end_game"]) -> Optional[bool]:
        """
        The block of code above is responsible for event handling. 
        Each function has this block of code, wherein it checks if 
        there are specific keys in the if statements that are clicked. 
        For instance, if the X on the top of the game window is clicked, 
        the program will stop; if the left key on the mouse is clicked, 
        the click will be equal to True -- meaning that a specific 
        button is clicked; and if the ESC button is clicked, the 
        function will return to True which is needed to carry out the 
        different functions in the gui.py code. Also, the DELETE key
        is functional here when DELETE key is pressed after the game
        round in the game.py.

        """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  # pylint: disable=no-member
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.click = True
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                if function == "main_menu":
                    pygame.quit() # pylint: disable=no-member
                    sys.exit()
                elif function in ("levels", "settings", "leaderboard", "control", "exit"):
                    return True
            if event.type == KEYDOWN and event.key == K_DELETE and function == "end_game":
                return True

        return None

    def reset_click(self) -> None:
        """
        This function is for resetting the click to False in the
        gui.py file.

        """
        self.click = False
