#!/bin/python

import os
import os.path


# 将dir目录下的所有文件的文件名写入到结果文件files_list.txt中
# 使用递归遍历

dir = '.'
result_file = open("files_list.txt", "w")


def walk_file_in_dir(dir):
    print(dir)
    result_file.write(dir + "\n")
    indent_count = dir.count("/")
    indent_str = ""
    for i in range(indent_count):
        indent_str += "  "
    for file in os.listdir(dir):
        relative_path = dir + "/" + file
        if(os.path.isdir(relative_path)):
            walk_file_in_dir(relative_path)
        else:
            result_file.write(indent_str + file + "\n")

walk_file_in_dir(dir)
result_file.close()

