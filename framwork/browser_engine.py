#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import configparser
import os.path
from selenium import webdriver
from framwork.logger import Logger
from pageobjects.ggb_Index import indexElement
import time

logger = Logger(logger="EngineLOG").getlog()

#定义浏览器类
class BrowserEngine(object):
    #浏览器的路径，因为只有谷歌的weidriver，所以只加了一个
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
        #初始化这个类
    def __init__(self,driver):
        self.indexelement = indexElement(self)
        self.driver = driver

    def open_browser(self,driver):
        #这个是python调用配置文件的类
        config = configparser.ConfigParser()
        #读取配置文件的位置
        file_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        #从这个位置读取配置文件
        config.read(file_path,encoding='utf-8')

        #读取配置文件中的浏览器
        browser = config.get('browserType','browserName')
        logger.info('you had select %s browser.' % browser)
        #读取配置文件中的网址
        url = config.get('Host','test_host')
        logger.info('The test server url is %s' %url)
        #打开浏览器
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info('Starting Firefox browser')
        elif browser == "Chrome":
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            prefs = {
                'profile.default_content_setting_values': {
                    'notifications': 2
                }
            }
            option.add_experimental_option('prefs', prefs)
            #option.add_argument('headless')
            driver = webdriver.Chrome(executable_path=self.chrome_driver_path,chrome_options = option,desired_capabilities = None)
            logger.info('Starting Chrome browser')
        elif browser == 'IE':
            driver = webdriver.Ie()
            logger.info('Starting IE browser')
        #打开网页、最大化、等10毫秒
        driver.get(url)
        logger.info("open url:%s." %url)
        driver.maximize_window()
        logger.info("zhe window max")
        driver.implicitly_wait(3000)
        logger.info("set implicitly wait 30 seconds")
        # driver.find_element_by_xpath(self.indexelement.username).send_keys('13530852030')
        # driver.find_element_by_xpath(self.indexelement.password).send_keys('123456')
        # driver.find_element_by_xpath(self.indexelement.submit).click()
        return driver


    #退出的方法
    def quit_browser(self):
        logger.info(' Now,close the browser')
        self.driver.quit()

