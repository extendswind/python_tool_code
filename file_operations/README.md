python基本的文件操作

# 遍历所有的文件

`list_files_in_directory.py` 文件通过递归的形式遍历所有目录，将文件写入到结果文件。


# 文件分组打包

`tar_files.py` 用于文件的tar打包和压缩，使用os.system命令调用了linux的tar命令打包。

针对以下文件目录

dir
├── subdir1
├── subdir2 
├── subdir3
└── subdir4

逻辑不复杂就不进一步封装了，对每一个subdir，如果文件夹中的文件超过15个，对文件分组打包，每组文件的大小超过设定的大小（最后一组除外）。


# 用到的函数

os.path.isdir(dir) 判断是否为文件目录。

os.mkdir(dir) 创建目录

os.listdir(dir) 获取dir下的所有文件，获取的是不带路径的文件名，递归时需要加上dir路径。

os.walk(dir) 直接得到递归遍历的所有文件。

shutil.move("a", "b") 移动和重命名文件 

os.system("cd " + dir + " && " + "tar czvf " + file + ".tar.gz " + file) 调用Linux命令打包

