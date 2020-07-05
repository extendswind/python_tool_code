
- [django web应用框架](#django-web应用框架)
- [生成二维码](#生成二维码)
- [微信公众号操作](#微信公众号操作)
- [sqlite数据库操作](#sqlite数据库操作)


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

