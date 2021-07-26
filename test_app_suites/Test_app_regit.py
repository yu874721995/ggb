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
        cls.driver = browser.open_browser()
        cls.app = app_BassPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.app.close_app()

    def test_Index_commodityOrder(cls):
        '''验证app注册'''

        ioc = ('id', "com.android.permissioncontroller:id/permission_allow_button")
        try:
            WebDriverWait(cls.driver,1,0.5).until(EC.presence_of_element_located(ioc)).click()
        except Exception as e:
            print(e)
        time.sleep(3)
        cls.app.click("com.dengta.date:id/btn_user_privacy_policy_summary_agree")
        cls.app.click("com.dengta.date:id/ll_login_select_cellphone_login_register")
        cls.app.send_keys("com.dengta.date:id/et_login_phone_number_new",randint(17100000001,17100001000))
        cls.app.send_keys("com.dengta.date:id/et_login_code",'80008')
        cls.app.click("com.dengta.date:id/btn_login_sure")
        cls.app.click('com.dengta.date:id/btn_inviteCode_cancel')
        cls.app.click('com.dengta.date:id/iv_register_sex_girl')
        cls.app.click('com.dengta.date:id/btn_register_sex_sure')
        cls.app.send_keys('com.dengta.date:id/et_nick_name','兮兮')
        time.sleep(2)
        cls.app.click('com.dengta.date:id/ll_register_info_nickname')
        cls.app.click('com.dengta.date:id/iv_register_avatar_set_avatar')
        cls.app.click('com.dengta.date:id/tv_select_avatar_select_from_album')
        cls.app.click('com.android.permissioncontroller:id/permission_allow_button')
        cls.app.click('com.android.permissioncontroller:id/permission_allow_button')
        cls.app.click('com.dengta.date:id/tvCheck')
        cls.app.click('com.dengta.date:id/picture_send')
        cls.app.click('com.dengta.date:id/menu_crop')
        cls.app.click('com.dengta.date:id/btn_register_info_next_step')

if __name__ == "__main__":
    unittest.main()

