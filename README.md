# PlantsVsZombies
A basic plant hotbar selector using pynput

Designed for monitors of 1920x1080 resolution, if running a different resolution read "Using a Different Resolution" below

Use [1-0] to select your plant!

If you have a plant selected when you press a number, the program uses the variable "mouse_zero_tuple" to right click an unused location, deselecting the plant. This breaks at different resolutions also, instructions to fix this are below.
## Requirements:

The only requirement is [pynput](https://pypi.org/project/pynput/)

### To install
pip install pynput

## Run

python PlantsVsZombies.py

## Using a Different Resolution

Pressing "Space" while the program is running prints out a tuple showing (x, y) of the current mouse position

Using this, hover your mouse over each plant and press space one after another. Take those tuples and update the dictionary "mouse_position_dict".

You may also need to change "mouse_zero_tuple" as mentioned at the top, again you can use the space print to find this. This tuple must be in the game space (as PvZ cuts off the sides of the screen with black bars, it should be just to the right of the left black bar, top left).

This behaviour can be removed by removing or commenting out lines 17, 18, and 19.
