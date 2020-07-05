#!/bin/python
# -*- coding: utf-8 -*-
# filename: basic.py

from urllib import request
import time
import json
import os


script_dir = os.path.split(os.path.realpath(__file__))[0]                   

class TokenServer:    
    def __init__(self): 
        self.__accessToken = ''        
        self.__leftTime = 0    

    def __real_get_access_token(self): 
        appId = "TODO"      
        appSecret = "TODO"
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
                   "client_credential&appid=%s&secret=%s" % (appId, appSecret))   
        urlResp = request.urlopen(postUrl) 
        urlResp = json.loads(urlResp.read())       
        print(urlResp)
        self.__accessToken = urlResp['access_token']    
        self.__leftTime = urlResp['expires_in']   
        tokenFile = open(script_dir + '/token', 'w')
        tokenFile.write(self.__accessToken)
        tokenFile.close()
        print(self.__accessToken)
        print(self.__leftTime)

    def get_access_token(self):  
        if self.__leftTime < 10:   
            self.__real_get_access_token()  
        return self.__accessToken  

    def run(self):  
        while(True):       
            if self.__leftTime > 120:        
                time.sleep(120)       
                self.__leftTime -= 120      
            else:        
                self.__real_get_access_token()


server = TokenServer()
server.run()
