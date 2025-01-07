"""
The test.py file contains the different test cases used to test the 
functions of the mp1.py file. You may check that it works through 
typing pytest test.py. You may insert a new test case by adding 
assert function_name('input_depending_on_args') == correct_output 
at the end of each function. The file imported the functions 
separate_moves, step_shift_eggs_with_rules, tilt_grid, and 
apply_moves from the mp1.py file.

"""
from typing import List, Tuple
from mp1 import (
    separate_moves,
    shift_eggs,
    tilt_grid,
    apply_move,
    process_lines
)

def test_separate_moves() -> None:
    """
    In the test_separate_moves function, there are several test cases 
    wherein we checked if the separate_moves function works correctly 
    for instances when a string of input (whether they are lowercase or 
    uppercase, or with LBRF or none) is given or when a number or 
    whitespace is given. When empty string, numbers, or whitespaces 
    are given as input, the separate_moves returns an empty list, 
    meaning that the function does not consider those inputs. 
    Also, we checked if the function correctly extracts the LFRB 
    letters in every possible input.

    """
    assert separate_moves('ZZZZZF') == ['f']
    assert separate_moves('') == []
    assert separate_moves('abcdefghijklmnopqrstuvwxyz') == ['b', 'f', 'l', 'r']
    assert separate_moves('1') == []
    assert separate_moves('1.00') == []
    assert separate_moves('lh') == ['l']
    assert separate_moves('h') == []
    assert separate_moves('lahkhhai') == ['l']
    assert separate_moves(' ') == []
    assert separate_moves('i am testing my input') == []
    assert separate_moves('i love cs 11 so much') == ['l']
    assert separate_moves('09176151201') == []
    assert separate_moves('us2 ko na magpasko yeah') == []
    assert separate_moves('lLfFrRbB') == ['l', 'l', 'f', 'f', 'r', 'r', 'b', 'b']
    assert separate_moves('LLLL') == ['l', 'l', 'l', 'l']
    assert separate_moves('RRRR') == ['r', 'r', 'r', 'r']
    assert separate_moves('FFFF') == ['f', 'f', 'f', 'f']
    assert separate_moves('BBBB') == ['b', 'b', 'b', 'b']


def test_shift_eggs() -> None:
    """
    In the test_shift_eggs function, there are several test cases 
    wherein we checked if the function correctly does the basic 
    shifting such as left or right when there are only grass and 
    eggs on the screen, penalty scenarios wherein there are frying 
    pans involved, reward scenarios wherein there are empty nests 
    involved, cases when there are two eggs and there is only one 
    empty nests, cases when there are eggs and full nests (if the 
    eggs will move or not), and empty strings if the rows do not 
    have any icons. Note that the function shift_eggs is a function 
    that shifts the eggs one tile at a time (so if the frying pan 
    is on the left, and there are three eggs moving to the left, 
    only one egg will disappear as in the mp1.py, it is in the 
    nested loop, one frame at a time).

    """
    assert shift_eggs('🟩🥚🟩', 0, 'left') == ('🥚🟩🟩', True, 0)
    assert shift_eggs('🟩🥚🟩', 0, 'right') == ('🟩🟩🥚', True, 0)
    assert shift_eggs('🍳🥚🟩', 0, 'left') == ('🍳🟩🟩', True, -5)
    assert shift_eggs('🟩🥚🍳', 0, 'right') == ('🟩🟩🍳', True, -5)
    assert shift_eggs('🪹🥚🟩', 0, 'left') == ('🪺🟩🟩', True, 10)
    assert shift_eggs('🟩🥚🪹', 0, 'right') == ('🟩🟩🪺', True, 10)
    assert shift_eggs('🪺🥚🟩', 0, 'left') == ('🪺🥚🟩', False, 0)
    assert shift_eggs('🟩🥚🪺', 0, 'right') == ('🟩🥚🪺', False, 0)
    assert shift_eggs('🥚🥚🟩', 0, 'left') == ('🥚🥚🟩', False, 0)
    assert shift_eggs('🟩🥚🥚', 0, 'right') == ('🟩🥚🥚', False, 0)
    assert shift_eggs('🟩🥚🥚🟩', 0, 'left') == ('🥚🥚🟩🟩', True, 0)
    assert shift_eggs('🟩🥚🥚🟩', 0, 'right') == ('🟩🟩🥚🥚', True, 0)
    assert shift_eggs('🪹🥚🥚🟩', 0, 'left') == ('🪺🥚🟩🟩', True, 10)
    assert shift_eggs('🟩🥚🥚🪹', 0, 'right') == ('🟩🟩🥚🪺', True, 10)
    assert shift_eggs('🪺🥚🥚🟩', 0, 'left') == ('🪺🥚🥚🟩', False, 0)
    assert shift_eggs('🟩🥚🥚🪺', 0, 'right') == ('🟩🥚🥚🪺', False, 0)
    assert shift_eggs('🍳🥚🥚🟩', 0, 'left') == ('🍳🥚🟩🟩', True, -5)
    assert shift_eggs('🟩🥚🥚🍳', 0, 'right') == ('🟩🟩🥚🍳', True, -5)
    assert shift_eggs('', 0, 'left') == ('', False, 0)
    assert shift_eggs('', 0, 'right') == ('', False, 0)
    assert shift_eggs('🟩🥚🥚🪹', 0, 'right') == ('🟩🟩🥚🪺', True, 10)
    assert shift_eggs('🍳🥚🥚🟩', 0, 'left') == ('🍳🥚🟩🟩', True, -5)

def test_tilt_grid() -> None:
    """
    In the test_tilt_grid function, there are several test cases wherein 
    we checked if the function correctly does the basic left, right, down, 
    and up shifts in every scenario mentioned after this, penalty scenarios 
    that involves frying pans, reward scenarios that involve empty nests, 
    and scenarios that involve full nests. They were added as it was 
    integral to the adherence to the game mechanics, and to make sure 
    that the basic components of the game are correct in execution.

    """
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

def test_apply_move() -> None:
    """
    In the test_apply_move function, there are several test cases 
    wherein we checked if the function correctly returns the expected 
    output after applying a specific move depending on the players' 
    input. There are basic test cases that checks the result of the 
    function for different directions, penalty scenarios that involves 
    eggs moving to frying pans, reward scenarios that involve eggs 
    moving towards empty nests, and scenarios that involve eggs moving 
    towards full nests. They were added to the set of test cases as 
    they will check if the points are calculated correctly depending 
    on where the egg lands, and if the correct icon was displayed at 
    the end of every move.

    """
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


def test_process_lines() -> None:
    """
    In this function, there are several test cases wherein we checked if
    the function process_lines processed the lines containing eggs, pans, 
    nests, etc. We tested cases where the eggs have to shift to the left or
    right, and cases where there are only eggs on the picture, or when eggs
    have pans beside them.

    """
    assert process_lines(['🟩🥚🪹'], 0, 'right') == (['🟩🟩🪺'], 10, True)
    assert process_lines(['🟩🥚🍳'], 0, 'left') == (['🥚🟩🍳'], 0, True)
    assert process_lines(['🥚🥚🥚'], 0, 'left') == (['🥚🥚🥚'], 0, False)
    assert process_lines(['🪹🥚🥚'], 0, 'right') == (['🪹🥚🥚'], 0, False)
    assert process_lines(['🟩🥚🪹', '🍳🥚🟩'], 0, 'right') == (['🟩🟩🪺', '🍳🟩🥚'], 10, True)
    assert process_lines(['🪺🥚🟩', ''], 0, 'left') == (['🪺🥚🟩', ''], 0, False)


# The following below is added for the Sphinx documentation generation:
# if __name__ == "__main__":
#    test_apply_move()
#    test_process_lines()
#    test_tilt_grid()
#    test_shift_eggs()
#    test_separate_moves()
