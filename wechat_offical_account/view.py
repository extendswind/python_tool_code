import qrcode
import io
import base64
from django.http import HttpResponse

from lxml import etree
from .wechatUtil import NewsMsg
from .wechatUtil import TextMsg
from .wechatUtil import ImageMsg
from .sqliteUtil import SqliteOperator

import datetime
# from .wechatUtil import ImageOperator


# 用于公众号设置服务器时的验证
def wechatCheck(request):
  if request.method == 'GET':
    try:
      echostr = request.GET['echostr']
      print(echostr)
      print("wechat server check finished")
    except Exception:
      echostr = "error in wechat server check"
      print(echostr)
  return HttpResponse(echostr)


# 回复消息
# 当订阅公众号的用户在公众号中发送文字时，会向指定服务器URL发送POST请求，
# 可以将处理POST请求的函数设置为此函数
def replyMsg(request):
  if request.method == 'POST':
    body = request.body
    xmlTree = etree.fromstring(str(body, encoding='utf-8')).getroottree()

    toUserName = xmlTree.xpath('//ToUserName')[0].text
    fromUserName = xmlTree.xpath('//FromUserName')[0].text
    msgType = xmlTree.xpath('//MsgType')[0].text

    print(toUserName)
    print(fromUserName)
    print(msgType)
    print(body)

    msg = TextMsg(fromUserName, toUserName, "Sorry, I can not answer you")

    # 处理文字消息
    if msgType == 'text' :
      content = xmlTree.xpath('//Content')[0].text

      if content == '111':
        print("reply message for 111")
        msg = NewsMsg(fromUserName, toUserName, url, url, "title", "reply for 111")

    # 处理事件消息
    elif msgType == 'event':
      event = xmlTree.xpath('//Event')[0].text
      print("处理事件： " + event)
      if event == 'subscribe':
        msg = ImageMsg(fromUserName, toUserName, "userid")
    
    return HttpResponse(msg.getXML())
