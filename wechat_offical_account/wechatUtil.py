# -*- coding: utf-8 -*-

"""
两个类，主要用于构造返回消息的xml字符串。

一个用于文字消息，一个用于文字消息。
"""

from urllib import request
import requests
import json
import os
import time


class TextMsg(object):
  def __init__(self, toUserName, fromUserName, content):
    self.__dict = dict()
    self.__dict['ToUserName'] = toUserName
    self.__dict['FromUserName'] = fromUserName
    self.__dict['CreateTime'] = int(time.time())
    self.__dict['Content'] = content
  def getXML(self):
    XmlForm = """
    <xml>
      <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
      <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
      <CreateTime>{CreateTime}</CreateTime>
      <MsgType><![CDATA[text]]></MsgType>
      <Content><![CDATA[{Content}]]></Content>
    </xml>
    """
    return XmlForm.format(**self.__dict)


class ImageMsg(object):
  def __init__(self, toUserName, fromUserName, mediaId):
    self.__dict = dict()
    self.__dict['ToUserName'] = toUserName
    self.__dict['FromUserName'] = fromUserName
    self.__dict['CreateTime'] = int(time.time())
    self.__dict['MediaId'] = mediaId
  def getXML(self):
    XmlForm = """
    <xml>
    <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
    <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
    <CreateTime>{CreateTime}</CreateTime>
    <MsgType><![CDATA[image]]></MsgType>
    <Image>
    <MediaId><![CDATA[{MediaId}]]></MediaId>
    </Image>
    </xml>
    """
    return XmlForm.format(**self.__dict)


# 图文消息
# 本身支持多条图文，此类只放入了一个
class NewsMsg(object):
  def __init__(self, toUserName, fromUserName, picUrl, url, title="一个title", 
              description="一个描述\n"):
    self.__dict = dict()
    self.__dict['ToUserName'] = toUserName
    self.__dict['FromUserName'] = fromUserName
    self.__dict['CreateTime'] = int(time.time())
    self.__dict['PicUrl'] = picUrl
    self.__dict['Url'] = url
    self.__dict['Title'] = title
    self.__dict['Description'] = description
  def getXML(self):
    XmlForm = """
    <xml>
      <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
      <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
      <CreateTime>{CreateTime}</CreateTime>
      <MsgType><![CDATA[news]]></MsgType>
      <ArticleCount>1</ArticleCount>
      <Articles>
        <item>
          <Title><![CDATA[{Title}]]></Title>
          <Description><![CDATA[{Description}]]></Description>
          <PicUrl><![CDATA[{PicUrl}]]></PicUrl>
          <Url><![CDATA[{Url}]]></Url>
        </item>
      </Articles>
    </xml>
    """
    return XmlForm.format(**self.__dict)

