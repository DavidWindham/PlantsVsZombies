from pynput import keyboard
from pynput.mouse import Controller, Button


def handle_keyboard_key_press(key):
    try:
        k = key.char
    except:
        k = key.name

    if k in mouse_position_dict:
        # Get the current mouse position as tuple
        pre_move_mouse_tuple = mouse.position

        # Right click in case you need to deselect a currently selected plant
        # This tuple may need to be changed if not running at 1920x1080, see below on how to change this
        mouse.position = mouse_zero_tuple
        mouse.press(Button.right)
        mouse.release(Button.right)

        # Move to the tuple from the association dict
        mouse.position = mouse_position_dict[k]

        # Click to select the plant
        mouse.press(Button.left)
        mouse.release(Button.left)
        # Move back to the original position
        mouse.position = pre_move_mouse_tuple

    if k == "space":
        print(mouse.position)


# This dict is for 1920x1080
# The function above allows for printing the mouse position if you press the "space" key
# Track your mouse over each plant pressing space on each one and use those tuples given to adjust this dict
mouse_position_dict = {
    "1": (440, 70),
    "2": (530, 70),
    "3": (625, 70),
    "4": (720, 70),
    "5": (815, 70),
    "6": (900, 70),
    "7": (1000, 70),
    "8": (1090, 70),
    "9": (1175, 70),
    "0": (1270, 70)
}
# A position for the mouse to right click, potentially deselecting the current selected plant
mouse_zero_tuple = (241, 0)

# Init the mouse
mouse = Controller()

# Init the keyboard and start loop listening to key presses
listener = keyboard.Listener(on_press=handle_keyboard_key_press)
listener.start()
listener.join()
