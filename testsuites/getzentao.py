#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19:36
# @Author  : Carewn
# @Software: PyCharm


from pageobjects.ggb_Index_pageobject import IndexPage
from pageobjects.ggb_customer_pageobject import Customer_page
from pageobjects.ggb_Addcustomer_pageobject import AddCustomer
from framwork.Get_login_token import Get_Login
from framwork.base_page import BassPage
from framwork.browser_engine import BrowserEngine
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import unittest,time
import requests
import random


class CheckProject(unittest.TestCase):

    def setUp(self):
        Engin = BrowserEngine(self)
        self.driver = Engin.open_browser(self)

    def tearDown(self):
        self.driver.close()

    def test_projectList(self):
        basePage = BassPage(self.driver)
        wait = WebDriverWait(self.driver, 20)
        wait.until(lambda d: d.find_element_by_xpath('/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[2]/a/span[1]/span[2]'))
        basePage.click('xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[2]/a')
        wait = WebDriverWait(self.driver, 20)
        wait.until(lambda d: d.find_element_by_xpath('/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[2]/a/span[1]/span[2]'))
        time.sleep(2)
        basePage.click('name=>searchParam')
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()







