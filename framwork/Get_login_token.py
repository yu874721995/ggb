#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 22:09
# @Author  : Carewn
# @Software: PyCharm

import requests
import json
import time,os
import configparser
from .logger import Logger

mylog = Logger(logger="Getlogin").getlog()

class Get_Login():

    def get_mp_login_interface(self):
        '''获取平台端token'''
        config = configparser.ConfigParser()
        path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(path,encoding='utf-8')
        mp_host = config.get("Host",'mp_host')
        mp_login_api = config.get("Api",'mp_login')
        mp_pic_api = config.get("Api",'picture_list')
        mp_login_url = mp_host+mp_login_api
        mp_pic_url = mp_host+mp_pic_api
        return mp_login_url,mp_pic_url

    def get_test_login_interface(self):
        '''获取商家端token'''
        config = configparser.ConfigParser()
        path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(path,encoding='utf-8')
        mp_host = config.get("Host", 'test_host')
        mp_login_api = config.get("Api", 'test_login')
        mp_login_url = mp_host + mp_login_api
        return mp_login_url

    def get_mp_token(self):
        url = self.get_mp_login_interface()[0]
        data = {
            "account":"admin",
            "pwd":"e10adc3949ba59abbe56e057f20f883e"
        }
        r = requests.post(url,data=data)
        token = r.json()['token']
        token = "Bearer "+token
        return token

    def get_test_token(self):
        url = self.get_test_login_interface()
        data = {
            "account": "13530852030",
            "pwd": "e10adc3949ba59abbe56e057f20f883e"
        }
        r = requests.post(url, data=data)
        token = r.json()['token']
        token = "Bearer " + token
        return token

    def get_picurl(self):
        url = self.get_mp_login_interface()[1]
        data = {
            "pageNumber": 1,
            "pageSize": 10,
            "range": [],
            "type": []
        }
        headers = {
            "Authorization": self.get_mp_token(),
        }
        r = requests.post(url, data=data, headers=headers)
        rs = r.json()
        return rs

if __name__  == '__main__':
    s = Get_Login()
    s.get_test_token()
    s.get_picurl()
