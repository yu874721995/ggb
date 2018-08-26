#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 15:30
# @Author  : Carewn
# @Software: PyCharm

import requests
from framwork.Get_login_token import Get_Login

# l = Get_Login()
# headers = {
# 'Authorization':l.get_test_token()
# }
# data = {
#
# }
# r = requests.post('https://saas.ydm01.cn/api/home_page/index_revenue_data',data=data,headers=headers )
# rs = r.json()
# print r.text

import os
Test_path = os.path.dirname(os.path.dirname(__file__))
print (os.path.dirname(os.path.dirname(__file__)))
print (os.path.dirname(os.path.abspath('.')))
print (os.path.dirname(os.path.abspath('.')+'\\'))

