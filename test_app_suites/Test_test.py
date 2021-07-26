# -*- coding : utf-8 -*-
# @Auther    : Careslten
# @time      : 2021/1/30 18:27
# @File      : Test_app.py
# @SoftWare  : appium_jskj

from framwork.app_engine import BrowserEngine
from framwork.app_base_page import app_BassPage
import unittest,time
from random import randint
import requests

class Test_Index_projectreceipt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls,noReset="True")
        cls.driver = browser.open_browser()
        cls.app = app_BassPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.app.close_app()
        cls.driver.quit()

    def test_Index_commodityOrder(cls):
        '''验证app登录'''
        phone = str(randint(17100000001, 17100001000))
        time.sleep(1)
        current_package = cls.driver.current_package
        cls.app.app_find_elements('com.dengta.date:id/icon')[1].click()
        cls.app.click('com.dengta.date:id/iv_item_personal_live_pic')
        cls.app.click('com.dengta.date:id/tv_live_bottom_say_something')
        cls.app.send_keys('com.dengta.date:id/et_dialog_live_edit_comment',111)
        cls.app.click('com.dengta.date:id/tv_dialog_live_edit_comment_send')


        time.sleep(3)


















if __name__ == "__main__":
    unittest.main()