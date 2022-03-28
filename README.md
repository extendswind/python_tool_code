
每次搜索需要的库和代码略麻烦，在这个仓库把用过的一些东西单独做个分类，放些简单的代码实现。


- [django web应用框架](#django-web应用框架)
- [生成二维码](#生成二维码)
- [微信公众号操作](#微信公众号操作)
- [sqlite数据库操作](#sqlite数据库操作)
- [键盘鼠标控制](#键盘鼠标控制)
- [简单文件操作](#简单文件操作)


# [django web应用框架](django_code)

创建项目，简单的处理对应链接的get、post请求，以及图片处理等。


# [生成二维码](qrcode)

依赖qrcode模块

https://github.com/lincolnloop/python-qrcode


# [微信公众号操作](wechat_official_account)

只考虑了基本的账户，没有企业认证多了很多限制。

- 服务器认证
- 自动获取token
- 基本的消息收取（文本消息、事件消息[订阅、取消订阅]）
- 基本的消息回复（图文消息、文字消息）
- 主动发送消息
- 向服务器上传图片（返回URL或mediaid）

# [sqlite数据库操作](sqlite)

一个简单的sqlite数据库操作

# [键盘鼠标控制](keyboard_mouse_control)

可以使用三个库，PyAutoGUI、pynput、keyboard。

PyAutoGUI使用比较方便，可以直接用函数调用的形式发送键盘和鼠标消息，获取当前鼠标位置，但不能响应键盘消息。pynput用函数回调的方式能够响应鼠标消息。pynput的快捷键修改映射在使用组合键时有点小问题，keyboard库使用没有问题，添加快捷键更容易，还多了一个录制键盘操作的功能。

- 获取键盘按键以及发出键盘按键消息
- 键盘全局快捷键响应
- 获取鼠标位置以及移动鼠标位置

几个库默认都没有默认支持全局键盘消息处理的机制，而是通过注册globalhotkey的快捷键，对快捷键调用回调函数的方式进行实现，通过这种方式避免python处理大量事件效率低的问题。

这几个库在windows上功能比较齐全而且出问题较少，在当前使用的archlinux+awesome上快捷键的处理有些问题。不支持快捷键消息的屏蔽（suppressed），发送快捷键如ctrl+f时，会触发先前的查找快捷键，而且将ctrl+f的响应函数设置为按下right键时，得到的效果是ctrl+right（可以用传出right键消息之前先release后press ctrl键），还有些按一次触发多次的坑不确定原因。

文档在，感觉几个文档的示例代码都很简单，仓库就不放了。

- `https://pyautogui.readthedocs.io/en/latest/quickstart.html`
- `https://pynput.readthedocs.io/en/latest/index.html`
- `https://github.com/boppreh/keyboard`

TODO: 

- [x]测试响应键盘消息的cpu消耗  注册的globalhotkey没有太大量的情况下，cpu消耗可以忽略，使用的事件传递机制而非循环检测的机制。
- xxx 实现一个像autohotkey一样的脚本定义（这几个库在linux上都不支持屏蔽先前的快捷键，只能在没有键冲突时才有用，而且还有些modifier的问题，在win10上实现有睡眠后唤醒失效的问题需要解决，后面整理代码）

# [简单文件操作](file_operations)

`list_files_in_directory.py` 遍历文件夹中的所有文件写入一个文件列表。

`tar_files.py` 调用linux的tar命令，将文件按照大小分组后打包。


# [鼠标位置截图和处理](screenshot_and_process)

主要实现功能：

- 鼠标所在位置的屏幕截图
- 截图的位置识别

使用OpenCV的模板匹配实现了一个简单的鼠标位置图片和周边的位置对比，移动到最近的相似位置。

windows上有bug，代码未整理，仅参考。
