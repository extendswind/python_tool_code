#!/bin/python

# 键盘和鼠标锁
# python默认无法拦截ctrl+alt+delete消息，最好在edit group policy -> user configuration -> Administrative Template -> System -> Ctrl+Alt+Del Options，Remove Task

from pynput import mouse
from pynput import keyboard
import time

# 锁屏输入后退出
lockword = "abcdefg"  # 替换为个人密码
wordIndex = 0  # 用于锁屏密码验证，标记当前输入正确密码的位置
is_exit = False

# 鼠标点击响应
# pressed 标记是press还是release消息
def on_click(x, y, button, pressed):
    if is_exit:
        return False
    if pressed and button == mouse.Button.left:
        print("left button clicked: x = " + str(x) + "  y = " + str(y))
    return True
  
# 键盘按键响应
def on_press(key):
    global lockword
    global wordIndex
    global is_exit
    print("key pressed")
    if lockword[wordIndex] == key.char:
        wordIndex += 1
        if wordIndex == len(lockword):
            is_exit = True
    else:
        wordIndex = 0

print("keyboard and mouse locked.....")
# 这几个函数是非阻塞函数，可能是向操作系统注册类似钩子函数一类的操作
# 后面需要进一步处理
mouse_listener = mouse.Listener(on_click=on_click, suppress=True)
mouse_listener.start()
keyboard_listener = keyboard.Listener(on_press=on_press, suppress=True)
keyboard_listener.start()

# 默认的join函数无法马上退出
# 通过while循环的方式能够增加锁屏过程中其它操作的支持
while True:
    time.sleep(1)
    if is_exit:
        break
print("...unlocked...")
time.sleep(0.5)
