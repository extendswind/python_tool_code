
服务器的配置，token的申请等等此处忽略，具体参考官方文档。

向公众号中发送文字，或产生订阅、取消订阅等消息时，微信服务器会向开发文档中设置的服务器发送POST请求，根据POST请求返回的结果回复给用户。

# 代码文件

view.py 包含使用django中用于处理POST请求的函数，用于服务器的验证和消息的回复。

wechatUtil.py 将输入的几个参数转换为合适格式返回的xml字符串。

postMessage.py 直接向用户通过POST请求发送消息（有权限限制）。

token_server 每隔一段时间向服务器请求一次token，并保存在本地用于其它的请求任务。

imgUpload.py 上传图片使用的两个接口。


# 收到消息的格式

普通文本消息

```xml
<xml>
  <ToUserName><![CDATA[toUser]]></ToUserName>
  <FromUserName><![CDATA[fromUser]]></FromUserName>
  <CreateTime>1348831860</CreateTime>
  <MsgType><![CDATA[text]]></MsgType>
  <Content><![CDATA[this is a test]]></Content>
  <MsgId>1234567890123456</MsgId>
</xml>
```

事件消息

```xml
<xml>
  <ToUserName><![CDATA[toUser]]></ToUserName>
  <FromUserName><![CDATA[FromUser]]></FromUserName>
  <CreateTime>123456789</CreateTime>
  <MsgType><![CDATA[event]]></MsgType>
  <Event><![CDATA[subscribe]]></Event>
</xml>
```

其中 Event 事件类型，subscribe(订阅)、unsubscribe(取消订阅)

# 回复消息的格式

回复文本消息

```xml
<xml>
  <ToUserName><![CDATA[toUser]]></ToUserName>
  <FromUserName><![CDATA[fromUser]]></FromUserName>
  <CreateTime>12345678</CreateTime>
  <MsgType><![CDATA[text]]></MsgType>
  <Content><![CDATA[你好]]></Content>
</xml>
```

回复图片消息

<xml>
  <ToUserName><![CDATA[toUser]]></ToUserName>
  <FromUserName><![CDATA[fromUser]]></FromUserName>
  <CreateTime>12345678</CreateTime>
  <MsgType><![CDATA[image]]></MsgType>
  <Image>
    <MediaId><![CDATA[media_id]]></MediaId>
  </Image>
</xml>

回复图文消息

<xml>
  <ToUserName><![CDATA[toUser]]></ToUserName>
  <FromUserName><![CDATA[fromUser]]></FromUserName>
  <CreateTime>12345678</CreateTime>
  <MsgType><![CDATA[news]]></MsgType>
  <ArticleCount>1</ArticleCount>
  <Articles>
    <item>
      <Title><![CDATA[title1]]></Title>
      <Description><![CDATA[description1]]></Description>
      <PicUrl><![CDATA[picurl]]></PicUrl>
      <Url><![CDATA[url]]></Url>
    </item>
  </Articles>
</xml>
