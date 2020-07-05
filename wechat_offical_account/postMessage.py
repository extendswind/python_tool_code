

import token_server
import token_server.getToken
import requests

import json


token = token_server.getToken.get()
postUrl = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=" + token

msg = {
    "touser":"userid_TODO",
    "msgtype":"text",
    "text":
    {
         "content":"Hello World"
    }
}


r = requests.post(postUrl, data=json.dumps(msg))
print(r.text)
