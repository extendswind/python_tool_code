#!/bin/python

import cv2
from matplotlib import pyplot as plt

# 根据一张图片，在另一张图片上找这张图片的中心位置

img = cv2.imread('test_target.png', 0)
# img2 = img.copy()
template = cv2.imread('test_template.png', 0)

w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
method = cv2.TM_CCOEFF
# img = img2.copy()
# eval 语句用来计算存储在字符串中的有效 Python 表达式
# method = eval(method)

# 模板匹配
res = cv2.matchTemplate(img, template, method)

# 寻找最值
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

center_x = (top_left[0] + bottom_right[0]) / 2
center_y = (top_left[1] + bottom_right[1]) / 2
print(center_x, center_y)
print(max_val)

cv2.rectangle(img, top_left, bottom_right, 255, 2)
plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(method)
plt.show()
