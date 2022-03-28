#!/bin/python

from pynput import mouse
from pynput import keyboard

is_mouse_move_print = False


# 鼠标点击响应
# pressed 标记是press还是release消息
def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        print("x = " + str(x))
        print("y = " + str(y))
    else:
        print("click release")
    if x < 10 and y < 10:
        # exit
        return False


def on_move(x, y):
    if is_mouse_move_print:
        print('Pointer moved to {0}'.format((x, y)))


# 键盘按键响应
def on_press(key):
    print('pressed key: ' + str(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def on_activate_q():
    print('<ctrl>+<alt>+q pressed')
    global is_mouse_move_print
    is_mouse_move_print = not is_mouse_move_print


# Collect events until released
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

keyboard_hotkey = keyboard.GlobalHotKeys({'<ctrl>+<alt>+q': on_activate_q})
keyboard_hotkey.start()

# Collect events until released
with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
    listener.join()

print("exit")
