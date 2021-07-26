#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17:28
# @Author  : Carewn
# @Software: PyCharm


from selenium.webdriver.support.ui import WebDriverWait
from framwork.app_engine import BrowserEngine
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framwork.base_page import BassPage
import selenium

import unittest,time



class Test_Index_projectreceipt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        cls.driver.implicitly_wait(3)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_Index_commodityOrder(cls):
        '''验证商品订单数量'''
        app = BassPage(cls.driver)
        ioc = ('id', "com.android.permissioncontroller:id/permission_allow_button")
        try:
            WebDriverWait(cls.driver,1,0.5).until(EC.presence_of_element_located(ioc)).click()
        except Exception as e:
            print(e)
        time.sleep(3)
        cls.driver.find_element_by_id("com.dengta.date:id/btn_user_privacy_policy_summary_agree").click()
        app.app_find_element("id=>com.dengta.date:id/ll_login_select_cellphone_login_register").click()
        app.app_find_element("id=>com.dengta.date:id/et_login_phone_number_new").send_keys('15989510397')
        app.app_find_element("id=>com.dengta.date:id/tv_login_get_code").click()

        # code = ('id','com.dengta.date:id/web_view')
        # WebDriverWait(cls.driver,3,1).until(EC.presence_of_element_located(code))
        app.app_find_element("id=>com.dengta.date:id/et_login_code").send_keys('28351')
        app.app_find_element("id=>com.dengta.date:id/btn_login_sure").click()
        app.app_find_element("id=>com.android.permissioncontroller:id/permission_allow_button").click()

        #处理签到弹窗
        qiandao = ('id','com.dengta.date:id/btn_sign_in')
        if cls.findelement(cls.driver,'com.dengta.date:id/btn_sign_in'):
            app.app_find_element('id=>com.dengta.date:id/btn_sign_in').click()
            app.app_find_element('id=>	com.dengta.date:id/btn_confirm').click()

        cls.driver.find_elements_by_id('com.dengta.date:id/icon')[1].click()#跳转直播列表
        app.app_find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click() #青少年模式
        app.app_find_element("id=>com.dengta.date:id/btn_open").click()#点击开启地理位置
        app.app_find_element("id=>com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()#开启地理位置
        cls.driver.find_elements_by_id("com.dengta.date:id/iv_item_personal_live_pic")[0].click()#点击第一个直播间

        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("id=>com.dengta.date:id/btn_youth_mode_i_know").click()
        # app.find_element("xpath=>//*[@text='其他号码登录']").click()
        time.sleep(20)


    def findelement(cls,driver,id):
        try:
            WebDriverWait(driver,5, 1).until(driver.find_element_by_id(id))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            return False

if __name__ == "__main__":
    unittest.main()

