"""
The gui.py file contains the different functions that enable our 
team to create the main menu interface. To give an overview on 
how the whole file works, we used the pygame library to create 
features such as button and loading images onto the screen. 
The idea on how the file works is that the gui.py contains 
functions that represent the 'buttons' and their functionalities 
('Play', 'Settings', 'Exit Game' and other buttons in the game). 
It is like a 'slideshow' presentation wherein when you click a 
button (like for example, 'Play'), you will be 'directed' to 
another frame or in Python sense, a new frame will be shown 
through the screen.blit() function which is seen across the 
document. Every function contains clickable buttons and event 
handling methods which will be explained further below.

The pygame library was imported as it is one of the libraries 
in Python used to make games and its features. The sys module 
was imported to let the program interact with the system such 
as when the player wants to exit the game (removing the game 
screen on the system). The game module was imported as this 
represents game.py - the file used to load the game interface, 
as well as implementation of game mechanics such as adding the 
number of points, checking the remaining number of moves, and 
others. In the gui.py file, the game module is mostly used to 
call the function start_with_gui_level() in game.py, which 
opens the files such as level1.in which are used to set-up 
the game itself. The EventHandler class from the mp1_classes.py
file was also used for handling interactions such as when ESC
button is pressed or when the mouse is clicked.

The block of code from mainClock to pygame.display.set_mode 
is for the setting up of the game itself. The pygame.time.Clock() 
creates a clock object to be used in functions where time delays 
are needed. The from pygame.locals import * is for importing 
constants from pygame library such as KEYDOWN and QUIT for 
managing inputs like arrow keys and letter keys. 
The pygame.display.set_caption('Egg Roll') sets the name of the 
game window to 'Egg Roll'. The icon for the game is located on 
the images folder, and the pygame.display.set_icon() function 
displays the icon.png on the taskbar whenever the game is opened. 
The pygame.display.set_mode() function makes the resolution of 
the game to be set to 960 x 768. All the frames used for the 
game were set to this resolution.

Every function has pygame.mouse.get_pos() which is responsible 
for finding the position of the mouse pointer on the game screen, 
and this position are saved as position_x and position_y. Also, 
every rectangular area is made by pygame.Rect() which has four 
arguments: starting x position, starting y position, width, and 
height. These rectangle areas are saved in variables such as 
exit_game_button. There are also if statements with the function 
.collidepoint() with position_x and position_y as its argument. 
These statements check if the mouse pointer is within the 
rectangular area of the button and if the area is clicked on 
the mouse. Once clicked, a new frame will be shown on the screen 
as other functions will be called such as settings(mode).

"""

from typing import Literal
import sys
import pygame
import game
from mp1_classes import EventHandler, LevelsLightImages, LevelsDarkImages
from mp1_classes import SettingsLightImages, SettingsDarkImages

#This is to set-up the main menu itself.
mainClock = pygame.time.Clock()
pygame.init() # pylint: disable=no-member
pygame.display.set_caption('Egg Roll')

#This is to load the icon on the desktop taskbar.
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

#This is the screen resolution of the game
screen = pygame.display.set_mode((960, 768),0,32)


# If editing the gui.py file, you may uncomment the lines
# below to show where the buttons are located.

# Main Menu Buttons
# transparent_play_button = pygame.Surface((285,90), pygame.SRCALPHA)
# transparent_play_button.fill((255,0,0,128))
# transparent_settings_button = pygame.Surface((285,90), pygame.SRCALPHA)
# transparent_settings_button.fill((255,0,0,128))
# transparent_exit_game_button = pygame.Surface((310,90), pygame.SRCALPHA)
# transparent_exit_game_button.fill((255,0,0,128))

# Levels Buttons
# transparent_level1_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_level1_button.fill((255,0,0,128))
# transparent_level2_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_level2_button.fill((255,0,0,128))
# transparent_level3_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_level3_button.fill((255,0,0,128))
# transparent_level4_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_level4_button.fill((255,0,0,128))
# transparent_level5_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_level5_button.fill((255,0,0,128))
# transparent_main_menu_levels_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_main_menu_button.fill((255,0,0,128))

# Settings Button
# transparent_tutorial_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_tutorial_button.fill((255,0,0,128))

# transparent_leaderboard_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_leaderboard_button.fill((0,127,127,128))

# transparent_control_keys_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_control_keys_button.fill((255,127,0,128))

# transparent_dark_mode_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_dark_mode_button.fill((255,255,0,128))

# transparent_credits_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_credits_button.fill((0,127,127,128))

# transparent_main_menu_settings_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_main_menu_settings_button.fill((0,0,255,128))


# transparent_back_to_settings_button = pygame.Surface((305,60), pygame.SRCALPHA)
# transparent_back_to_settings_button.fill((255,0,0,128))



# Exit_Game Buttons
# transparent_yes_button = pygame.Surface((260,80), pygame.SRCALPHA)
# transparent_yes_button.fill((255,0,0,128))
# transparent_no_button = pygame.Surface((260,80), pygame.SRCALPHA)
# transparent_no_button.fill((255,0,0,128))


def main_menu(mode: Literal['light', 'dark'] = 'light') -> None:
    """
    The main_menu function is responsible for showing the main menu 
    interface. It accepts a single argument: mode which as a default 
    value "light" meaning that the game will load the light mode of 
    the main menu interface by default, and when it is called again 
    in other functions with mode = "dark", it will show the dark mode. 
    The screen will then be updated by the .display.update() function 
    and the .tick() function is responsible for the frame per second 
    to be passed when updating the screen.

    Args:
        mode: Literal['light', 'dark'] = 'light': The mode for the
        screen to be flashed on screen; light is the default

    Returns:
        None

    """
    event_handler = EventHandler() # This is to initialize the event handler
    while True:
        if mode == "light":
            screen.blit(LevelsLightImages.main_menu_light, (0, 0))
        else:
            screen.blit(LevelsDarkImages.main_menu_dark, (0, 0))

        position_x, position_y = pygame.mouse.get_pos()

        play_button = pygame.Rect(600, 330, 285, 90)
        settings_button = pygame.Rect(583, 450, 285, 90)
        exit_game_button = pygame.Rect(590, 570, 310, 90)

        if play_button.collidepoint((position_x, position_y)) and event_handler.click:
            levels(mode)
        if settings_button.collidepoint((position_x, position_y)) and event_handler.click:
            settings(mode)
        if exit_game_button.collidepoint((position_x, position_y)) and event_handler.click:
            exit_game(mode)

        event_handler.reset_click()

        event_handler.process_events("main_menu")

        pygame.display.update()
        mainClock.tick(60)


def levels(mode: Literal['light', 'dark'] = 'light', tutorial: Literal['yes', 'no'] = 'no') -> None:
    """
    The levels() function is responsible for displaying the level 
    selector interface for the main levels and tutorial levels, 
    depending on the mode (light or dark) and if the function is 
    called with yes or no as the tutorial. The function has two 
    default values, mode = "light" and tutorials = "no", meaning 
    that it loads the main level selector in the light mode as 
    default. This function is called mainly in the main_menu function 
    wherein when the player clicks the Play button, the said function 
    will call the levels function.

    Args:
        mode (Literal['light', 'dark']): This determines the theme of the screen.
        tutorial (Literal['yes', 'no']): This indicates if tutorial mode is on or not.
    
    Returns:
        None

    """
    event_handler = EventHandler()
    running = True
    while running:
        if mode == "light" and tutorial == "no":
            screen.blit(LevelsLightImages.levels_light,(0,0))
        elif mode == "light" and tutorial == "yes":
            screen.blit(SettingsLightImages.tutorials_light, (0,0))
        elif mode != "light" and tutorial == "no":
            screen.blit(LevelsDarkImages.levels_dark,(0,0))
        elif mode != "light" and tutorial == "yes":
            screen.blit(SettingsDarkImages.tutorials_dark,(0,0))

        position_x, position_y = pygame.mouse.get_pos()

        level1_button = pygame.Rect(575, 248, 305, 60)
        level2_button = pygame.Rect(575, 325, 305, 60)
        level3_button = pygame.Rect(580, 400, 305, 60)
        level4_button = pygame.Rect(575, 475, 305, 60)
        level5_button = pygame.Rect(580, 550, 305, 60)
        main_menu_levels_button = pygame.Rect(580, 625, 305, 60)


        if level1_button.collidepoint((position_x, position_y)) and event_handler.click:
            loading(1, mode, tutorial)
        if level2_button.collidepoint((position_x, position_y)) and event_handler.click:
            loading(2, mode, tutorial)
        if level3_button.collidepoint((position_x, position_y)) and event_handler.click:
            loading(3, mode, tutorial)
        if level4_button.collidepoint((position_x, position_y)) and event_handler.click:
            loading(4, mode, tutorial)
        if level5_button.collidepoint((position_x, position_y)) and event_handler.click:
            loading(5, mode, tutorial)
        if main_menu_levels_button.collidepoint((position_x, position_y)) and event_handler.click:
            (settings if tutorial == "yes" else main_menu)(mode)

        event_handler.reset_click()

        escape = event_handler.process_events("levels")
        if escape is True:
            (settings if tutorial == "yes" else main_menu)(mode)

        pygame.display.update()
        mainClock.tick(60)


def render_scr(file: int, mode: Literal['light', 'dark'], tutorial: Literal['yes', 'no']) -> None:
    """
    This function creates dictionaries for the level_files, tutorial_files,
    light_screens, and dark_screens. The function loads the screen depending
    on the specific file level as represented by file and if the tutorial
    level is on or not.

    Args:
        file (int): This is the level or tutorial number (1-5).
        mode (Literal['light', 'dark']): This determines the theme of the screen.
        tutorial (Literal['yes', 'no']): This indicates if tutorial mode is on or not.

    Returns:
        None
    """
    level_files = {
        1: "level1.in",
        2: "level2.in",
        3: "level3.in",
        4: "level4.in",
        5: "level5.in",
    }
    tutorial_files = {
        1: "tutorial1.in",
        2: "tutorial2.in",
        3: "tutorial3.in",
        4: "tutorial4.in",
        5: "tutorial5.in",
    }
    light_screens = {
        1: LevelsLightImages.loading_1_light,
        2: LevelsLightImages.loading_2_light,
        3: LevelsLightImages.loading_3_light,
        4: LevelsLightImages.loading_4_light,
        5: LevelsLightImages.loading_5_light,
    }
    dark_screens = {
        1: LevelsDarkImages.loading_1_dark,
        2: LevelsDarkImages.loading_2_dark,
        3: LevelsDarkImages.loading_3_dark,
        4: LevelsDarkImages.loading_4_dark,
        5: LevelsDarkImages.loading_5_dark,
    }

    loading_screen = light_screens[file] if mode == "light" else dark_screens[file]
    file_to_load = tutorial_files[file] if tutorial != "no" else level_files[file]

    screen.blit(loading_screen, (0, 0))
    pygame.display.flip()
    pygame.time.wait(5000)

    if tutorial == "no":
        game.start_gui_with_level(file_to_load, mode, False)
    else:
        game.start_gui_with_level(file_to_load, mode, True)


def loading(file: int,
    mode: Literal['light', 'dark'] = 'light',
    tutorial: Literal['yes', 'no'] = 'no') -> None:
    """
    This function handles the loading screen logic. If the file number is 
    within 1-5, it will call the render_screen function. However, it will
    tell the user that the file number is not in range 1-5 if otherwise.
    
    Args:
        file (int): The level or tutorial number (1-5).
        mode (Literal['light', 'dark']): This determines the theme of the screen.
        tutorial (Literal['yes', 'no']): This indicates if tutorial mode is on or not.
    
    Returns:
        None

    """
    running = True
    while running:
        if file in range(1, 6):
            render_scr(file, mode, tutorial)
        else:
            print(f"File not in the range 1-5: {file}")
            running = False

        pygame.display.update()
        mainClock.tick(60)


def settings(mode: Literal['light', 'dark'] = "light") -> None:
    """
    The settings function loads the settings interface. When called, 
    it has the default value mode = "light", meaning that the default 
    settings interface is in light mode. It also has sections in the 
    code that creates clickable buttons and event handling.
    
    Args:
        mode (Literal['light', 'dark']): This determines the theme of the screen.
        The default is light mode.
    
    Returns:
        None

    """
    event_handler = EventHandler()
    running = True
    while running:
        if mode == "light":
            screen.blit(SettingsLightImages.settings_light,(0,0))
        else:
            screen.blit(SettingsDarkImages.settings_dark,(0,0))

        position_x, position_y = pygame.mouse.get_pos()

        tutorial_button = pygame.Rect(590, 210, 305, 60)
        leaderboard_button = pygame.Rect(590, 285, 305, 60)
        control_keys_button = pygame.Rect(590, 375, 305, 60)
        dark_or_day_mode_button = pygame.Rect(595, 450, 305, 60)
        credits_button = pygame.Rect(590, 535, 305, 60)
        main_menu_settings_button = pygame.Rect(590, 615, 305, 60)


        if tutorial_button.collidepoint((position_x, position_y)) and event_handler.click:
            levels(mode, "yes")
        if leaderboard_button.collidepoint((position_x, position_y)) and event_handler.click:
            leaderboard(mode)
        if control_keys_button.collidepoint((position_x, position_y)) and event_handler.click:
            control_keys_or_credits(mode)
        if dark_or_day_mode_button.collidepoint((position_x, position_y)) and event_handler.click:
            if mode == "light":
                settings("dark")
            else:
                settings("light")
        if credits_button.collidepoint((position_x, position_y)) and event_handler.click:
            control_keys_or_credits(mode, "credits")
        if main_menu_settings_button.collidepoint((position_x, position_y)) and event_handler.click:
            main_menu(mode)

        event_handler.reset_click()

        escape = event_handler.process_events("settings")
        if escape is True:
            main_menu(mode)

        pygame.display.update()
        mainClock.tick(60)


def leaderboard(mode: Literal['light', 'dark'] = "light") -> None:
    """
    This function displays the leaderboard interface. It contains buttons
    for Levels 1-5, as well as the Settings screen which directs you back
    to the settings interface. It calls the get_leaderboard_scores 
    function when Levels 1-5 are clicked.
    
    Args:
        mode (Literal['light', 'dark']): This determines the theme of the screen.
    
    Returns:
        None
    """
    event_handler = EventHandler()
    running = True

    while running:
        if mode == "light":
            screen.blit(SettingsLightImages.leaderboard_light, (0, 0))
        else:
            screen.blit(SettingsDarkImages.leaderboard_dark, (0, 0))

        position_x, position_y = pygame.mouse.get_pos()

        leaderboard_level1_button = pygame.Rect(575, 248, 305, 60)
        leaderboard_level2_button = pygame.Rect(575, 325, 305, 60)
        leaderboard_level3_button = pygame.Rect(580, 400, 305, 60)
        leaderboard_level4_button = pygame.Rect(575, 475, 305, 60)
        leaderboard_level5_button = pygame.Rect(580, 550, 305, 60)
        leaderboard_back_to_settings_button = pygame.Rect(580, 625, 305, 60)

        if leaderboard_level1_button.collidepoint((position_x, position_y)) and event_handler.click:
            event_handler.active_level = 'level1.in'
        if leaderboard_level2_button.collidepoint((position_x, position_y)) and event_handler.click:
            event_handler.active_level = 'level2.in'
        if leaderboard_level3_button.collidepoint((position_x, position_y)) and event_handler.click:
            event_handler.active_level = 'level3.in'
        if leaderboard_level4_button.collidepoint((position_x, position_y)) and event_handler.click:
            event_handler.active_level = 'level4.in'
        if leaderboard_level5_button.collidepoint((position_x, position_y)) and event_handler.click:
            event_handler.active_level = 'level5.in'
        if leaderboard_back_to_settings_button.collidepoint((position_x, position_y)):
            if event_handler.click:
                settings(mode)

        if event_handler.active_level:
            top1, top2, top3 = game.get_leaderboard_scores(event_handler.active_level)
            display_scores(top1, top2, top3)

        event_handler.reset_click()

        escape = event_handler.process_events("levels")
        if escape is True:
            settings(mode)

        pygame.display.update()
        mainClock.tick(60)


def display_scores(first_score: int, second_score: int, third_score: int) -> None:
    """
    This function displays the Top 3 scores on the leaderboard interface
    through the font.render and screen.blit. The True in the .render() is
    for anti-aliasing and the (121,78,7) is for the font color.
    
    Args:
        first_score (int): The highest score.
        second_score (int): The second highest score.
        third_score (int): The third highest score.

    Returns:
        None
    """
    font = pygame.font.Font(None, 36)

    first_score_text = font.render(f"{first_score}", True, (121, 78, 7))
    second_score_text = font.render(f"{second_score}", True, (121, 78, 7))
    third_score_text = font.render(f"{third_score}", True, (121, 78, 7))

    screen.blit(first_score_text, (275,355))
    screen.blit(second_score_text, (275,395))
    screen.blit(third_score_text, (275,437))

def control_keys_or_credits(mode: Literal['light', 'dark'] = "light",
    use: Literal['control_keys',
    'credits'] = "control_keys") -> None:
    """
    The control_keys_or_credits function loads either the control keys 
    interface or the credits interface, depending if the function has 
    only 0-1 arguments or if the mode is set to "control_keys" or 
    "credits". We combined the loading of credits and control keys 
    interface since they have the same interface with different contents. 
    The if statements handle whether the one being loaded on the screen 
    is the control keys or the credits interface and whether they will 
    be in light or dark mode. Same as the other functions, it also has 
    sections in the code that creates clickable buttons and event handling.
    
    Args:
        mode (Literal['light', 'dark']): This determines the theme of the screen.
        use (Literal['control_keys', 'credits']): This indicates whether to show the 
        control keys or credits screen.

    Returns:
        None

    """
    event_handler = EventHandler()
    running = True
    while running:
        if mode == "light" and use == "control_keys":
            screen.blit(SettingsLightImages.control_keys_light,(0,0))
        elif mode != "light" and use == "control_keys":
            screen.blit(SettingsDarkImages.control_keys_dark, (0,0))
        elif mode == "light" and use != "control_keys":
            screen.blit(SettingsLightImages.credits_light,(0,0))
        else:
            screen.blit(SettingsDarkImages.credits_dark,(0,0))

        position_x, position_y = pygame.mouse.get_pos()

        back_to_settings_button = pygame.Rect(580, 645, 305, 60)

        if back_to_settings_button.collidepoint((position_x, position_y)) and event_handler.click:
            settings(mode)

        event_handler.reset_click()

        escape = event_handler.process_events("control")
        if escape is True:
            settings(mode)

        pygame.display.update()
        mainClock.tick(60)


def exit_game(mode: Literal['light', 'dark'] = "light") -> None:
    """
    The exit_game function loads the confirmation screen if the 
    player clicked the Exit Game button at the main menu interface. 
    It accepts one argument: mode which has the default value "light", 
    meaning that if the exit_game is called under the main_menu 
    function with 0-1 argument, provided that when 1 argument is 
    used ("light"), it will show the light mode of the confirmation 
    screen. When the Yes button is clicked, it will exit the game, 
    and clicking the No button will call the main_menu() function 
    with the argument mode that depends on the mode passed onto the 
    exit_game function. Same as the other functions, it also has 
    sections in the code that creates clickable buttons and event 
    handling.
    
    The main_menu() is at the last part of the gui.py code which 
    is important since when python3 gui.py is called, it will show 
    the main menu interface. If this is removed, the main menu will 
    not show up.

    Args:
        mode (Literal['light', 'dark']): This determines the theme of the screen.
    
    Returns:
        None

    """
    event_handler = EventHandler()
    running = True
    while running:
        if mode == "light":
            screen.blit(SettingsLightImages.sure_light,(0,0))
        else:
            screen.blit(SettingsDarkImages.sure_dark,(0,0))

        position_x, position_y = pygame.mouse.get_pos()

        yes_button = pygame.Rect(200, 450, 260, 80)
        no_button = pygame.Rect(530, 450, 260, 80)

        if yes_button.collidepoint((position_x, position_y)) and event_handler.click:
            pygame.quit() # pylint: disable=no-member
            sys.exit()
        if no_button.collidepoint((position_x, position_y)) and event_handler.click:
            main_menu(mode)

        event_handler.reset_click()

        escape = event_handler.process_events("levels")
        if escape is True:
            main_menu(mode)

        pygame.display.update()
        mainClock.tick(60)

main_menu()
