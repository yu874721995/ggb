#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 14:50
# @Author  : Carewn
# @Software: PyCharm

from framwork.base_page import BassPage

class indexElement(BassPage):

    username = '//*[@id="home_img_bg"]/div/div[2]/div/form/div[4]/input'
    password = '//*[@id="home_img_bg"]/div/div[2]/div/form/div[5]/input'
    submit = '//*[@id="home_img_bg"]/div/div[2]/div/form/div[6]/button'
