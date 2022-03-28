from pynput.mouse import Button, Controller
from pynput import mouse
import mss
import mss.tools
import numpy as np
import os
import cv2

# TODO list
# - 更简单的添加代码
# - 输入统计
# - 暂停一类的处理

# keyboard.press_and_release('shift+s, space')

# functionDict = {}
# functionDict['<esc>'] = on_activate_esc
shortcutFunction = []
keyBuildDict = {}

# 鼠标控制
mouse_controller = Controller()

# 屏幕
monitor = mss.mss().monitors[1]
screen_width = monitor['width']
screen_height = monitor['height']
needOpencv = False

if not os.path.exists("map_screen_coord.txt"):
    print("鼠标挪到地图左上角，切屏到此窗口敲回车")
    input()
    coord = mouse_controller.position
    left_x = coord[0]
    top_y = coord[1]
    print("鼠标挪到地图右下角，切屏到此窗口敲回车")
    input()
    coord = mouse_controller.position
    right_x = coord[0]
    bottom_y = coord[1]
    map_sc_file = open("map_screen_coord.txt", "w")
    map_sc_file.write(str(left_x) + " " + str(top_y) + " " + str(right_x) + " " + str(bottom_y))
    map_sc_file.close()
else:
    map_sc_file = open("map_screen_coord.txt", "r")
    line = map_sc_file.readline()
    sline = line.split(" ")
    left_x = int(sline[0])
    top_y = int(sline[1])
    right_x = int(sline[2])
    bottom_y = int(sline[3])
    map_sc_file.close()


# arcgis 窗口的坐标 （大概）
# left_x = int(232 / 1876 * screen_width)
# top_y = int(76 / 1024 * screen_height)
# right_x = int(1560 / 1876 * screen_width)
# bottom_y = int(720 / 1024 * screen_height)

# 屏幕坐标 1920*1080 可以用准确屏幕坐标覆盖
# left_x = 340
# right_x = 1655
# top_y = 180
# bottom_y = 1029

center_x = (left_x + right_x) / 2
center_y = (top_y + bottom_y) / 2

# 边缘范围的大小
edge_range_x = int(300 / 1876 * screen_width)
edge_range_y = int(140 / 1024 * screen_height)

# 截图
# sct = mss.mss()

# 图像匹配
# template_width = 100
# template_height = 100
# match_img_width = 200
# match_img_height = 200
template_width = int(60 / 1876 * screen_width)
template_height = int(60 / 1024 * screen_height)
match_img_width = int(160 / 1876 * screen_width)
match_img_height = int(130 / 1024 * screen_height)


# 只需要鼠标？
# 监听鼠标点击消息
# 如果发现在某个范围内
# 发送鼠标中键移动的消息

# 实现功能1 鼠标在地图边缘点击时，把地图移动到中间


def getScreenImgOpenCV(center_x, center_y, width, height):
    """
    sct为mss库的截屏对象
    TODO 超出范围会抛异常
    """
    left = int(center_x - width / 2)
    top = int(center_y - height / 2)
    monitor = {"left": left, "top": top, "width": width, "height": height}
    # print(monitor)

    # Grab the data
    try:
        with mss.mss() as sct:
            sct_img = sct.grab(monitor)
    except mss.exception.ScreenShotError:
        print("error")
        print(monitor)
        return None
    return np.array(sct_img)


def template_match(template, match_img):
    """
    在match_img中找到template
    返回template所在的中心点
    """
    method = cv2.TM_CCOEFF

    # 模板匹配
    res = cv2.matchTemplate(match_img, template, method)

    # 寻找最值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val, min_val)
    top_left = max_loc
    center_x = top_left[0] + template_width / 2
    center_y = top_left[1] + template_height / 2
    return (center_x, center_y)


# 鼠标点击响应
def on_click(x, y, button, pressed):
    if (not pressed) and (button == mouse.Button.left):
        # 如果在地图边缘范围内点击  在地图的范围内，且不在除边缘中间的区域内
        if (x > left_x and x < right_x and y > top_y and y < bottom_y) and (
                not (x > left_x + edge_range_x and x < right_x - edge_range_x
                     and y > top_y + edge_range_y
                     and y < bottom_y - edge_range_y)):

            # if (x < left_x + edge_range and x > left_x) or (
            # x > right_x - edge_range
            # and x < right_x) or (y < top_y + edge_range and y > top_y) or (
            # y > bottom_y - edge_range and y < bottom_y):

            # 通过鼠标中间拖动地图到中间多一点的位置
            map_move_x = int(x + (center_x - x) * 1.2)
            map_move_y = int(y + (center_y - y) * 1.2)
            mouse_controller.press(Button.middle)
            mouse_controller.position = (map_move_x, map_move_y)
            mouse_controller.release(Button.middle)

            mouse_move_x = x
            mouse_move_y = y
            # 需要在范围内才进行匹配，避免截图的exception
            if needOpencv and (x + match_img_width / 2 < right_x or x - match_img_width / 2 > 0 or y + match_img_height / 2 < top_y or y - match_img_height / 2 > 0):
                # 计算模板匹配
                template_img = getScreenImgOpenCV(map_move_x, map_move_y,
                                                  template_height,
                                                  template_width)
                match_img = getScreenImgOpenCV(x, y, match_img_width,
                                               match_img_height)
                if template_img is not None and match_img is not None:
                    (matched_x,
                     matched_y) = template_match(template_img, match_img)
                    # 图上的匹配坐标转为屏幕坐标
                    mouse_move_x = matched_x - match_img_width / 2 + x
                    mouse_move_y = matched_y - match_img_height / 2 + y

            mouse_controller.position = (mouse_move_x, mouse_move_y)


# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
