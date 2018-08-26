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
from framwork.browser_engine import BrowserEngine
from selenium.webdriver.support.ui import WebDriverWait
from framwork.logger import Logger
from selenium import webdriver
import unittest2,time
import requests
import random


mylog = Logger(logger='customer-log').getlog()
class Test_Customer_Managements(unittest2.TestCase):

    def setUp(self):
        Broswer = BrowserEngine(self)
        self.driver = Broswer.open_browser(self)
        mylog.info(u'登录成功')

    def tearDown(self):
        self.driver.quit()

    def test_AddCustomer(self):
        AddCustomers = AddCustomer()
        driver = Customer_page(self)
        Index = IndexPage(self)
        basepage = BassPage(self.driver)
        wait = WebDriverWait(self.driver,20)
        wait.until(lambda d:d.find_element_by_xpath(Index.Customer.split('=>')[1]))
        basepage.click(Index.Customer)
        basepage.click(driver.NewAddCustomer)
        # js = 'document.querySelectorAll("form")[0].style.display="block";'
        # self.driver.execute_script(js)
        print (type(AddCustomers.CustomerName.split('=>')[1]))
        basepage.type(AddCustomers.CustomerName,u'测试姓名')
        basepage.type(AddCustomers.CustomerNames,u'测试昵称')
        time.sleep(3)
        s = random.randint(15900000000,15910000000)
        r = requests.get('https://saas.ydm01.cn/api/setting/addWhiteList?phone=%s'%(str(s)),params=None)
        basepage.type(AddCustomers.CustomerTelphone,str(s))
        basepage.click(AddCustomers.Preservation)
        Prompt = ''
        if basepage.find_element(AddCustomers.Prompt):
            Prompt = basepage.find_element(AddCustomers.Prompt).text.json()
        try:
            assert '请选择所属顾问门店' in Prompt
            print ('Test pass')
        except Exception as e:
            print ('Test fail',e)

if __name__ =='__main__':
    unittest2.main()



