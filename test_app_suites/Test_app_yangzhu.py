# -*- coding : utf-8 -*-
# @Auther    : Careslten
# @time      : 2021/1/30 11:07
# @File      : Test_app_login.py
# @SoftWare  : appium_jskj



from selenium.webdriver.support.ui import WebDriverWait
from framwork.app_engine import BrowserEngine
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framwork.app_base_page import app_BassPage
import selenium
from random import randint

import unittest,time



class Test_Index_projectreceipt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_app(2)
        cls.app = app_BassPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.app.close_app()

    def test_Index_commodityOrder(cls):
        '''验证app注册'''

        time.sleep(10)
        cls.app.click('xpath=>//android.widget.LinearLayout[@content-desc=\"红包群\"]/android.widget.FrameLayout/android.widget.TextView')
        cls.app.click('xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout')
        for i in cls.app.app_find_elements('com.yiqunkeji.yqlyz:id/lyt_hb'):
            i.click()
            cls.app.click('com.yiqunkeji.yqlyz:id/btn_open')
            time.sleep(30)
            cls.app.click('xpath=>/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView')
            cls.app.click('com.yiqunkeji.yqlyz:id/btn_close')

        time.sleep(3)






if __name__ == "__main__":
    unittest.main()

