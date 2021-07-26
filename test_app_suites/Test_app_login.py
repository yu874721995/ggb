# -*- coding : utf-8 -*-
# @Auther    : Careslten
# @time      : 2021/1/30 11:07
# @File      : Test_app_login.py
# @SoftWare  : appium_jskj



from framwork.app_engine import BrowserEngine
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framwork.app_base_page import app_BassPage
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
        '''验证app登录'''

        ioc = ('id', "com.android.permissioncontroller:id/permission_allow_button")
        try:
            WebDriverWait(cls.driver,1,0.5).until(EC.presence_of_element_located(ioc)).click()
        except Exception as e:
            print(e)
        time.sleep(3)
        cls.driver.find_element_by_id("com.dengta.date:id/btn_user_privacy_policy_summary_agree").click()
        cls.app.app_find_element("id=>com.dengta.date:id/ll_login_select_cellphone_login_register").click()
        cls.app.app_find_element("id=>com.dengta.date:id/et_login_phone_number_new").send_keys('15989510397')
        cls.app.app_find_element("id=>com.dengta.date:id/et_login_code").send_keys('80008')
        cls.app.app_find_element("id=>com.dengta.date:id/btn_login_sure").click()
        cls.app.app_find_element("id=>com.android.permissioncontroller:id/permission_allow_button").click()

if __name__ == "__main__":
    unittest.main()

