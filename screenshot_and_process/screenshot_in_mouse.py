#!/bin/python

import mss
import mss.tools
from pynput.mouse import Controller
import numpy as np
import cv2
# from PIL import Image

mouse = Controller()


with mss.mss() as sct:
    x = mouse.position[0]
    y = mouse.position[1]
    width = 100
    height = 100
    monitor = {"left": x, "top": y, "width": width, "height": height}

    # output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)
    img = np.array(sct_img)
    cv2.imshow("OpenCV/Numpy normal", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # if cv2.waitKey(25) & 0xFF == ord("q"):
    # cv2.destroyAllWindows()

    # Save to the picture file
    # mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    # print(output)

    # show in PIL
    # img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    # img.show()
