
Python第三方库大多以简单作为哲学之一，提供的API大多几行代码能够搞定。每次都搜索需要的库和代码略麻烦，在这个仓库把用过的一些东西单独做个分类，放些简单的代码实现和使用，当个简单功能的字典查。


- [django web应用框架](#django-web应用框架)
- [生成二维码](#生成二维码)
- [微信公众号操作](#微信公众号操作)
- [sqlite数据库操作](#sqlite数据库操作)
- [键盘鼠标控制](#键盘鼠标控制)


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


文档在，感觉两个文档的示例代码都很简单，仓库就不放了。

- `https://pyautogui.readthedocs.io/en/latest/quickstart.html`
- `https://pynput.readthedocs.io/en/latest/index.html`
- `https://github.com/boppreh/keyboard`

TODO: 

- 测试响应键盘消息的cpu消耗
- 实现一个像autohotkey一样的脚本定义

