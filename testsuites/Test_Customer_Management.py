#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17:33
# @Author  : Carewn
# @Software: PyCharm

from pageobjects.ggb_Index_pageobject import IndexPage
from pageobjects.ggb_customer_pageobject import Customer_page
from pageobjects.ggb_Addcustomer_pageobject import AddCustomer
from framwork.Get_login_token import Get_Login
from framwork.base_page import BassPage
from framwork.app_engine import BrowserEngine
from selenium.webdriver.support.ui import WebDriverWait
from framwork.logger import Logger
from selenium import webdriver
import unittest,time
import requests
import random


mylog = Logger(logger='customer-log').getlog()
class Test_Customer_Managements(unittest.TestCase):

    def setUp(self):
        Broswer = BrowserEngine(self)
        self.driver = Broswer.open_browser(self)
        mylog.info(u'登录成功')


    def tearDown(self):
        self.driver.quit()

    def test_AddCustomer(self):
        # Goto = BassPage(self.driver)
        #
        # Goto.click('xpath=>//*[@id="defaultImg"]/div/a/img')
        # Goto.click('xpath=>//*[@id="header"]/div[1]/div/div[1]/div/div/a[1]')
        #
        # Goto.type('xpath=>//*[@id="username"]','15989510396')
        #
        # Goto.type('xpath=>//*[@id="password"]','5454yu')
        #
        # Goto.click('xpath=>//*[@id="login"]')
        #
        # asserts = self.driver.find_element_by_xpath('//*[@id="top-userName"]').text
        # assert asserts == 'zhhej'
        pass



if __name__ =='__main__':
    unittest.main()



