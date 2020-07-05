  
import random
import qrcode

from token_server import getToken
import requests
from sqliteUtil import SqliteOperator
import sys


class ImageOperator(object):

  # 输入本地路径与token
  # 返回 url
  # 本接口所上传的图片不占用公众号的素材库中图片数量的100000个的限制。图片仅支持jpg/png格式，大小必须在1MB以下。
  # 貌似反应时间略慢
  def upload_img(self, imgPath, token):
    postUrl = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" + token
    data = open(imgPath, 'rb').read()
    files = { 'media' : (imgPath, data,'image/png')}
    r = requests.post(postUrl, files = files)
    text = r.text
    print("upload image result: " + text )
    return text.split("\"")[3].replace('\\', '')
 
  # 输入本地路径与token
  # 返回 mediaId
  # 本接口所上传的图片有100000个的限制。图片仅支持jpg/png格式，大小必须在1MB以下。
  # 貌似反应时间略慢
  def upload_img_return_mediaId(self, imgPath, token):
    postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=" + token + "&type=image"
    data = open(imgPath, 'rb').read()
    files = { 'media' : (imgPath, data,'image/png')}
    r = requests.post(postUrl, files = files)
    text = r.text
    print("upload image result: " + text )
    return text.split("\"")[3]

  # luckyid : str
  def generate(self, qrString):
    print("generate qr image: " + qrString)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=1,
    )
    qr.add_data(qrString)
    qr.make(fit=True)
    img = qr.make_image()
    qrFile = 'imgs/' + qrString + '.png'
    # img = qrcode.make(str)
    with open(qrFile, 'wb') as f:
        img.save(f)
    return qrFile
   

if __name__ == '__main__':

  helpStr = """
    加图片名上传图片
      默认返回url
      -mediaid 返回media id
  """
  accessToken = getToken.get()
  oper = ImageOperator()

  url = oper.upload_img(qrfile, accessToken)

  print(sys.argv)
 
  if len(sys.argv >= 2) and 
    (sys.argv[1].endswith(".png") or sys.argv[1].endswith(".jpg")) :

    if len(sys.argv) == 3 and (sys.argv[2] == "-mediaid"):
      print(oper.upload_img_return_mediaId(sys.argv[1], accessToken))
    else:
      print(oper.upload_img(sys.argv[1], accessToken))
  else:
    print(helpStr)
      
