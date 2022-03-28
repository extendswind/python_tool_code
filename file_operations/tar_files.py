#!/bin/python

import os
import os.path
import shutil

# 如果文件夹中的文件超过15个，对文件分组打包
# 每组文件的大小超过tar_file_size
def mv_file_to_dir(dir, tar_file_size):
    files = os.listdir(dir)
    if len(files) > 15:
        dir_count = 0
        dir_file_size = 0
        os.mkdir(dir + "/" + str(dir_count))
        for file in files:
            dir_file_size += os.path.getsize(dir + "/" + file)
            shutil.move(dir + "/" + file, dir + "/" + str(dir_count) + "/")
            if dir_file_size/1024/1024 > tar_file_size:
                dir_file_size = 0
                dir_count += 1
                os.mkdir(dir + "/" + str(dir_count))
                print(file)

# 每个文件夹单独作为一个tar
def tar_files_in_dir(dir):
    files = os.listdir(dir)
    for file in files:
        os.system("cd " + dir + " && " + "tar czvf " + file + ".tar.gz " + file)

dir_name = "dir"
mv_file_to_dir(dir_name, 70)
tar_files_in_dir(dir_name)


