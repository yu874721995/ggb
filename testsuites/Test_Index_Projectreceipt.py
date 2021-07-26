#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17:28
# @Author  : Carewn
# @Software: PyCharm


from pageobjects.ggb_Index_pageobject import IndexPage
from framwork.Get_login_token import Get_Login
from framwork.base_page import BassPage
from framwork.browser_engine import BrowserEngine
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import unittest,time
import requests


class Test_Index_projectreceipt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_Index_projectreceipt(cls):
        '''验证首页项目收款'''
        basepage = BassPage(cls.driver)
        driver = IndexPage(cls.driver)
        wait = WebDriverWait(cls.driver,20,0.5)
        wait.until(lambda d:d.find_element_by_xpath('/html/body/div[2]/div[1]/header/div/div[1]/span/img'))
        basepage.click(driver.IndexClick)
        basepage.click(driver.Indexmerchant_all)
        projectreceipt = basepage.find_element(driver.RevenueData[0]).text
        projectreceipt_text = projectreceipt
        try:
            assert '项目收款' in projectreceipt_text
            print ('Test pass')
        except Exception as e:
            print ('Test fail',e)
        token = Get_Login()
        data = {}
        headers = {
            'Authorization': token.get_test_token()
        }
        r = requests.post('https://saas.ydm01.cn/api/home_page/index_revenue_data',data=data,headers=headers)
        project_receipt = r.json()
        print (project_receipt['dataProjectRec'][-1]['value'])
        print (projectreceipt_text.split('¥')[1].replace('.',''))
        print (projectreceipt)
        try:
            assert str(project_receipt['dataProjectRec'][-1]['value']) in projectreceipt_text.split('¥')[1].replace('.','')
            print ('Test pass')
        except Exception as e:
            print ('Test fail',e)

    def test_Index_ProjectConsumption(cls):
        '''验证首页项目消耗'''
        basepage = BassPage(cls.driver)
        driver = IndexPage(cls.driver)
        wait = WebDriverWait(cls.driver, 20)
        wait.until(lambda d: d.find_element_by_xpath('/html/body/div[2]/div[1]/header/div/div[1]/span/img'))
        basepage.click(driver.IndexClick)
        basepage.click(driver.Indexmerchant_all)
        projectreceipt = basepage.find_element(driver.RevenueData[1]).text
        projectreceipt_text = projectreceipt
        try:
            assert '项目消耗' in projectreceipt_text
            print ('Test pass')
        except Exception as e:
            print ('Test fail',e)
        token = Get_Login()
        data = {}
        headers = {
            'Authorization': token.get_test_token()
        }
        r = requests.post('https://saas.ydm01.cn/api/home_page/index_revenue_data',data=data,headers=headers)
        project_receipt = r.json()
        try:
            assert str(project_receipt['dataProjectCon'][-1]['value']) in projectreceipt_text.replace(',','')
            print ('Test pass')
        except Exception as e:
            print ('Test fail',e)

    def test_Index_CommodityRetail(cls):
        '''验证首页商品零售'''
        basepage = BassPage(cls.driver)
        driver = IndexPage(cls)
        wait = WebDriverWait(cls.driver, 20)
        wait.until(lambda d: d.find_element_by_xpath('/html/body/div[2]/div[1]/header/div/div[1]/span/img'))
        basepage.click(driver.IndexClick)
        basepage.click(driver.Indexmerchant_all)
        projectreceipt = basepage.find_element(driver.RevenueData[2]).text
        projectreceipt_text = projectreceipt
        try:
            assert '商品零售' in projectreceipt_text
            print ('Test pass')
        except Exception as e:
            print ('Test fail', e)
        token = Get_Login()
        data = {}
        headers = {
            'Authorization': token.get_test_token()
        }
        r = requests.post('https://saas.ydm01.cn/api/home_page/index_revenue_data', data=data, headers=headers)
        project_receipt = r.json()
        try:
            assert str(project_receipt['dataGoodsRetail'][-1]['value']) in projectreceipt_text.replace(',', '')
            print ('Test pass')
        except Exception as e:
            print ('Test fail', e)

    def test_Index_ZjcReceivables(cls):
        '''验证美丽金收款'''
        basepage = BassPage(cls.driver)
        driver = IndexPage(cls.driver)
        wait = WebDriverWait(cls.driver, 20)
        wait.until(lambda d: d.find_element_by_xpath('/html/body/div[2]/div[1]/header/div/div[1]/span/img'))
        basepage.click(driver.IndexClick)
        basepage.click(driver.Indexmerchant_all)
        projectreceipt = basepage.find_element(driver.RevenueData[3]).text
        projectreceipt_text = projectreceipt
        try:
            assert '美丽金收款' in projectreceipt_text
            print ('Test pass')
        except Exception as e:
            print ('Test fail', e)
        token = Get_Login()
        data = {}
        headers = {
            'Authorization': token.get_test_token()
        }
        r = requests.post('https://saas.ydm01.cn/api/home_page/index_revenue_data', data=data, headers=headers)
        project_receipt = r.json()
        try:
            assert str(project_receipt['dataBeautyRec'][-1]['value']) in projectreceipt_text.replace(',', '')
            print ('Test pass')
        except Exception as e:
            print ('Test fail', e)

    def test_Index_ClubReceivables(cls):
        '''验证会员卡收款'''
        basepage = BassPage(cls.driver)
        driver = IndexPage(cls.driver)
        wait = WebDriverWait(cls.driver, 20)
        wait.until(lambda d: d.find_element_by_xpath('/html/body/div[2]/div[1]/header/div/div[1]/span/img'))
        basepage.click(driver.IndexClick)
        basepage.click(driver.Indexmerchant_all)
        projectreceipt = basepage.find_element(driver.RevenueData[4]).text
        projectreceipt_text = projectreceipt
        try:
            assert '会员卡收款' in projectreceipt_text
            print ('Test pass')
        except Exception as e:
            print ('Test fail', e)
        token = Get_Login()
        data = {}
        headers = {
            'Authorization': token.get_test_token()
        }
        r = requests.post('https://saas.ydm01.cn/api/home_page/index_revenue_data', data=data, headers=headers)
        project_receipt = r.json()
        try:
            assert str(project_receipt['dataCardRec'][-1]['value']) in projectreceipt_text.replace(',', '')
            print ('Test pass')
        except Exception as e:
            print ('Test fail', e)

    def test_Index_ProjectOrder(cls):
        '''验证项目订单数量'''
        basepage = BassPage(cls.driver)
        driver = IndexPage(cls.driver)
        wait = WebDriverWait(cls.driver, 20)
        wait.until(lambda d: d.find_element_by_xpath('/html/body/div[2]/div[1]/header/div/div[1]/span/img'))
        basepage.click(driver.IndexClick)
        basepage.click(driver.Indexmerchant_all)
        projectreceipt = basepage.find_element(driver.RevenueData[5]).text
        projectreceipt_text = projectreceipt
        try:
            assert '项目订单' in projectreceipt_text
            print ('Test pass')
        except Exception as e:
            print ('Test fail', e)
        token = Get_Login()
        data = {}
        headers = {
            'Authorization': token.get_test_token()
        }
        r = requests.post('https://saas.ydm01.cn/api/home_page/index_revenue_data', data=data, headers=headers)
        project_receipt = r.json()
        try:
            assert str(project_receipt['dataProjectOrder'][-1]['value']) in projectreceipt_text.replace(',', '')
            print ('Test pass')
        except Exception as e:
            print ('Test fail', e)

    def test_Index_commodityOrder(cls):
        '''验证商品订单数量'''
        basepage = BassPage(cls.driver)
        driver = IndexPage(cls.driver)
        wait = WebDriverWait(cls.driver, 20)
        wait.until(lambda d: d.find_element_by_xpath('/html/body/div[2]/div[1]/header/div/div[1]/span/img'))
        basepage.click(driver.IndexClick)
        basepage.click(driver.Indexmerchant_all)
        projectreceipt = basepage.find_element(driver.RevenueData[6]).text
        projectreceipt_text = projectreceipt
        try:
            assert '商品订单' in projectreceipt_text
            print ('Test pass')
        except Exception as e:
            print ('Test fail', e)
        token = Get_Login()
        data = {}
        headers = {
            'Authorization': token.get_test_token()
        }
        r = requests.post('https://saas.ydm01.cn/api/home_page/index_revenue_data', data=data, headers=headers)
        project_receipt = r.json()
        try:
            assert str(project_receipt['dataGoodsOrder'][-1]['value']) in projectreceipt_text.replace(',', '')
            print ('Test pass')
        except Exception as e:
            print ('Test fail', e)

if __name__ == "__main__":
    unittest.main()

