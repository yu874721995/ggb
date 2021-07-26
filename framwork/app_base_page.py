#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''基类，存放所有操作方法'''
import time
import os.path
from selenium.common.exceptions import NoSuchElementException
from .logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from functools import wraps
from selenium.webdriver.support import expected_conditions as EC

mylog = Logger(logger='Baselog').getlog()


class app_BassPage(object):

    def __init__(self, driver):
        self.driver = driver

    def contexts(self):
        '''返回当前会话中的所有上下文，使用后可以识别H5页面的控件'''
        contexts = self.driver.contexts()
        mylog.info(u'查询当前上下文：{}'.format(contexts))
        return contexts

    def current_context(self):
        '''返回当前会话的"当前上下文",即当前处于哪一个上下文'''
        current_context = self.driver.current_context()
        return current_context

    def context(self):
        '''返回当前会话的当前上下文'''
        context = self.driver.context()
        return context

    def close_app(self):
        '''关闭app'''
        try:
            self.driver.close_app()
            mylog.info(u'关闭app')
        except NameError as e:
            mylog.error(u'%s' % e)

    def get_window(self):
        '''截图，file方法截取的图片为全屏，另外两个截图方法分别为get_screenshot_as_base64和get_screenshot_as_png'''
        file_path = os.path.dirname(os.getcwd()) + '/screenshots/'
        file_time = time.strftime('%y%m%d%H%m', time.localtime(time.time()))
        file_name = file_path + file_time + str(time.time()) + '.png'
        try:
            self.driver.get_screenshot_as_file(file_name)
            mylog.info(u'截图并保存至：%s' % file_name)
        except NameError as a:
            mylog.error(u'截图失败，失败原因：%s' % a)
            self.get_window()


    def element_is_display(self, element):
        '''场景无法使用'''
        def element_loc(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                mylog.info('执行函数：{}'.format(func.__name__))
                elements = WebDriverWait(self.driver, 3, 0.5).until(self.app_find_element(element))
                if elements:
                    return func(*args, **kwargs)
                else:
                    raise NoSuchElementException('没有找到元素')
            return wrapper
        return element_loc

    def app_find_element(self, selector=None):
        '''查找元素'''
        if selector == None:
            raise NameError('元素定位信息不能为空!')
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        try:
            if selector_by == 'id':
                '''通过元素的resource-id属性'''
                element = self.driver.find_element_by_id(selector_value)

            elif selector_by == 'ios_uiautomation':
                element = self.driver.find_element_by_ios_uiautomation(selector_value)

            elif selector_by == 'class_name':
                '''通过元素的class属性'''
                element = self.driver.find_element_by_class_name(selector_value)

            elif selector_by == 'accessibility_id':
                '''android独有的定位方式，具体属性为：content-desc'''
                element = self.driver.find_element_by_accessibility_id(selector_value)

            elif selector_by == 'name':
                '''通过元素的text属性定位，1.5版本以上已弃用'''
                element = self.driver.find_element_by_name(selector_value)

            elif selector_by == 'link_text':
                '''通过元素的可见链接文本定位'''
                element = self.driver.find_element_by_link_text(selector_value)

            elif selector_by == 'partial_link_text':
                '''通过元素 部分 可见链接文本定位'''
                element = self.driver.find_element_by_partial_link_text(selector_value)

            elif selector_by == 'tag_name':
                '''操作webview时用于定位H5页面的html标签'''
                element = self.driver.find_element_by_tag_name(selector_value)

            elif selector_by == 'xpath':
                '''xpath，在appnium中定位非常慢切可靠性极低的一种方式'''
                element = self.driver.find_element_by_xpath(selector_value)

            elif selector_by == 'css_selector':
                element = self.driver.find_element_by_css_selector(selector_value)
            else:
                raise NameError(u'请输入一个正确的元素定位方式')
            return element
        except NoSuchElementException:
            self.get_window()
            raise NoSuchElementException(u'定位不到元素哦')

    def app_find_elements(self, selector=None):
        if selector == None:
            raise NameError('元素定位信息不能为空!')
        if '=>' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        try:
            if selector_by == 'id':
                '''通过元素的resource-id属性'''
                element = self.driver.find_elements_by_id(selector_value)

            elif selector_by == 'ios_uiautomation':
                element = self.driver.find_elements_by_ios_uiautomation(selector_value)

            elif selector_by == 'class_name':
                '''通过元素的class属性'''
                element = self.driver.find_elements_by_class_name(selector_value)

            elif selector_by == 'accessibility_id':
                '''android独有的定位方式，具体属性为：content-desc'''
                element = self.driver.find_elements_by_accessibility_id(selector_value)

            elif selector_by == 'name':
                '''通过元素的text属性定位，1.5版本以上已弃用'''
                element = self.driver.find_elements_by_name(selector_value)

            elif selector_by == 'link_text':
                '''通过元素的可见链接文本定位'''
                element = self.driver.find_elements_by_link_text(selector_value)

            elif selector_by == 'partial_link_text':
                '''通过元素 部分 可见链接文本定位'''
                element = self.driver.find_elements_by_partial_link_text(selector_value)

            elif selector_by == 'tag_name':
                '''操作webview时用于定位H5页面的html标签'''
                element = self.driver.find_elements_by_tag_name(selector_value)

            elif selector_by == 'xpath':
                '''xpath，在appnium中定位非常慢切可靠性极低的一种方式'''
                element = self.driver.find_elements_by_xpath(selector_value)

            elif selector_by == 'css_selector':
                element = self.driver.find_elements_by_css_selector(selector_value)
            else:
                raise NameError(u'请输入一个正确的元素定位方式')
            return element
        except NoSuchElementException:
            self.get_window()
            raise NoSuchElementException(u'定位不到元素哦')

    def scroll(self, origin_el, destination_el):
        element1 = WebDriverWait(self.driver, 3, 0.5).until(self.app_find_element(origin_el))
        element2 = WebDriverWait(self.driver, 3, 0.5).until(self.app_find_element(destination_el))
        if element1 and element2:
            pass
        else:
            return NoSuchElementException('没有找到元素')
        '''从元素origin_el滚动至元素destination_el'''
        self.driver.scroll(origin_el, destination_el)

    def element_is(self, element):
        try:
            if '=>' in element:
                elements = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((element.split('=>')[0],element.split('=>')[1])))
            else:
                elements = WebDriverWait(self.driver, 5, 0.5).until(
                    EC.presence_of_element_located(('id',element)))
            return True
        except:
            return False

    def drag_and_drop(self, origin_el, destination_el):
        element1 = WebDriverWait(self.driver, 3, 0.5).until(self.app_find_element(origin_el))
        element2 = WebDriverWait(self.driver, 3, 0.5).until(self.app_find_element(destination_el))
        if element1 and element2:
            pass
        else:
            return NoSuchElementException('没有找到元素')
        '''将元素origin_el拖到目标元素destination_el'''
        self.driver.drag_and_drop(origin_el, destination_el)

    def tap(self, positions, duration=None):
        '''模拟手指点击（最多五个手指），可设置按住时间长度（毫秒）'''
        '''
        positions:手指点击的位置，class:list
        duration:毫秒，为空时单击，设置后为长按
        '''
        self.driver.tap(positions, duration)

    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        '''
        从A点滑动至B点，滑动时间为毫秒
        :param start_x:开始的位置 x坐标
        :param start_y:开始的位置 y坐标
        :param end_x:结束的位置 x坐标
        :param end_y:结束的位置 y坐标
        :param duration:滑动时间
        :return:
        '''
        self.driver.swipe(start_x, start_y, end_x, end_y, 500)

    def flick(self, start_x, start_y, end_x, end_y):
        '''
        按住A点后快速滑动至B点
        :param start_x:开始的位置 x坐标
        :param start_y:开始的位置 y坐标
        :param end_x:结束的位置 x坐标
        :param end_y:结束的位置 y坐标
        :return:
        '''
        self.driver.flick(start_x, start_y, end_x, end_y)

    def pinch(self, element, percent=200, steps=50):
        '''
        在元素上执行模拟双指捏（缩小操作）
        :param element:缩小的元素
        :param percent:缩小的比例
        :param steps:
        :return:
        '''
        self.element_is(element)
        self.driver.pinch(element)

    def zoom(self, element, percent=200, steps=50):
        '''
        在元素上执行放大操作
        :param element:
        :param percent:
        :param steps:
        :return:
        '''
        self.element_is(element)
        self.driver.zoom(element)

    def reset(self):
        '''
        重置app
        :return:
        '''
        self.driver.reset()

    def hide_keyboard(self, key_name=None, key=None, strategy=None):
        '''
        隐藏键盘,iOS使用key_name隐藏，安卓不使用参数
        :param key_name: ios需要，android不需要
        :param key:
        :param strategy:
        :return:
        '''
        if key_name != None:
            self.driver.hide_keyboard(key_name)
        else:
            self.driver.hide_keyboard()

    def keyevent(self, keycode, metastate=None):
        '''
        按键码，例如返回、桌面等手机自带按钮,还有一个keycode方法与其功能一致
        :param keycode: 按键码
            左上键（菜单） ：KEYCODE_MENU 82
            电话键： KEYCODE_CALL 5
            上键： KEYCODE_DPAD_UP 19
            左键： KEYCODE_DPAD_LEFT 21
            下键： KEYCODE_DPAD_DOWN 20
            右键： KEYCODE_DPAD_RIGHT 22
            返回键： KEYCODE_BACK 4
            1键： KEYCODE_1 8
            2键： KEYCODE_2 9
            3键： KEYCODE_3 10
            4键： KEYCODE_4 11
            5键： KEYCODE_5 12
            6键： KEYCODE_6 13
            7键： KEYCODE_7 14
            8键： KEYCODE_8 15
            9键： KEYCODE_9 16
            *键： KEYCODE_STAR 19
            0键： KEYCODE_0 7
            #键： KEYCODE_POUND 18
        :param metastate:
        :return:
        '''
        self.driver.keyevent(keycode)

    def long_press_keycode(self, keycode, metastate=None):
        '''
        发送一个长按的按键码（长按某键）
        :param keycode:
        :param metastate:
        :return:
        '''
        self.driver.long_press_keycode(keycode)

    def current_activity(self):
        '''
        获取当前的activity
        :return:
        '''
        return self.driver.current_activity()

    def wait_activity(self, activity, timeout, interval=1):
        '''
        等待指定的activity出现直至超时
        :param activity: 指定的activity
        :param timeout:超时时间
        :param interval:扫描间隔
        :return:
        '''
        self.driver.wait_activity(activity, timeout, interval)

    def background_app(self, seconds):
        '''
        后台运行app
        :param seconds: 后台运行时间
        :return:
        '''
        self.driver.background_app(seconds)

    def is_app_installed(self, appPackages):
        '''
        检查app是否安装
        :param bundle_id:包名
        :return:
        '''
        self.driver.is_app_installed(appPackages)

    def install_app(self, app_path):
        '''
        install app
        :param app_path:
        :return:
        '''
        self.driver.install_app(app_path)

    def remove_app(self, appPackages):
        '''
        uninstall app
        :param appPackages:
        :return:
        '''
        self.driver.remove_app(appPackages)

    def launch_app(self):
        '''
        start app
        :return:
        '''
        self.driver.launch_app()

    def start_activity(self, app_package, app_activity, **opts):
        '''
        在测试过程中打开任意活动。如果活动属于另一个应用程序，该应用程序的启动和活动被打开。
        :param app_package:
        :param app_activity:
        :param opts:
        - app_wait_package - 在该app启动后开始自动化 (optional).
        - app_wait_activity - 在该活动启动后开始自动化(optional).
        - intent_action - Intent to start (optional).
        - intent_category - Intent category to start (optional).
        - intent_flags - Flags to send to the intent (optional).
        - optional_intent_arguments - Optional arguments to the intent (optional).
        - stop_app_on_reset - Should the app be stopped on reset (optional)?
        :return:
        '''
        self.driver.start_activity(app_package, app_activity)

    def lock(self, seconds):
        '''
        锁屏，仅ios可用
        :param seconds:
        :return:
        '''
        self.driver.lock(seconds)

    def shake(self):
        '''
        摇一摇手机
        :return:
        '''
        self.driver.shake()

    def open_notifications(self):
        '''
        打开系统通知栏，仅支持android
        :return:
        '''
        self.driver.open_notifications()

    def network_connection(self):
        '''
        获取当前网络类型
        :return:
        '''
        self.driver.network_connection()

    def set_network_connection(self, type):
        '''
        设置网络类型
        :param type:
            无网络 = 0
            飞行模式 = 1
            只使用wifi = 2
            只使用数据流量 = 4
            所有网络都打开 = 6
        :return:
        '''
        self.driver.set_network_connection(type)

    def available_ime_engines(self):
        '''
        返回android设备所有可用的输入法
        :return:
        '''
        return self.driver.available_ime_engines()

    def activate_ime_engine(self, engine):
        '''
        激活某一输入法，需要先使用available_ime_engines获取
        :param engine:
        :return:
        '''
        self.driver.activate_ime_engine(engine)

    def toggle_location_services(self):
        '''
        :return:位置信息
        '''
        return self.driver.toggle_location_services()

    def set_location(self, latitude, longitude, altitude):
        '''
        设置经纬度
        :param latitude: 纬度
        :param longitude:经度
        :param altitude:高度
        :return:
        '''
        self.driver.set_location(latitude, longitude, altitude)

    def text(self,element):
        '''
        返回元素的text
        :return:
        '''
        self.element_is(element)
        el = self.app_find_element(element)
        return el.text

    def click(self, element):
        '''

        :return:
        '''
        try:
            mylog.info(element)
            if self.element_is(element):
                el = self.app_find_element(element)
                el.click()
                time.sleep(0.5)
            else:
                self.get_window()
                raise NoSuchElementException
        except Exception as e:
            mylog.error(e)
            self.get_window()

    def clear(self, element):
        '''
        清除输入的内容
        :return:
        '''
        self.element_is(element)
        self.driver.app_find_element(element).clear()

    def get_attribute(self, element, name):
        '''
        获取元素的属性，暂时用不上
        :param element:元素
        :param name: 要取的属性
        :return:
        '''
        self.element_is(element)
        el = self.app_find_element(element)
        return self.driver.app_find_element(element).get_attribute(name)

    def is_enabled(self, element):
        '''
        返回元素是否可用
        :return:
        '''
        self.element_is(element)
        return self.driver.is_enabled(element)

    def is_selected(self, element):
        '''
        检查一个元素是否被选中
        :return:
        '''
        self.element_is(element)
        return self.driver.is_selected(element)

    def send_keys(self, element, text):
        '''
        输入
        :param element: 输入元素
        :param text: 文字内容
        :return:
        '''
        self.element_is(element)
        el = self.app_find_element(element)
        el.send_keys(text)

    def is_displayed(self, element):
        '''
        元素是否可见，确定是否被挡住、隐藏、是否可点击等（selenium可使用，appnium不可）
        :return:
        '''
        self.element_is(element)
        el = self.app_find_element(element)
        el.is_displayed()

    def size(self, element):
        '''
        返回元素的大小
        :param element:
        :return:
        '''
        self.element_is(element)
        el = self.app_find_element(element)
        return el.size()

    def location(self, element, type):
        '''
        返回元素的坐标
        :param element: 元素
        :param type: x为纵坐标，y为横坐标
        :return:
        '''
        self.element_is(element)
        el = self.app_find_element(element)
        return el.location.get(type)

    def rect(self, element):
        '''
        一次性返回元素的位置和大小
        :return: dict
        '''
        self.element_is(element)
        el = self.app_find_element(element)
        return el.rect()

    def get_window_size(self):
        '''
        获取当前屏幕分辨率
        :return:
        '''
        return self.driver.get_window_size()

    def back(self):
        '''

        :return:
        '''
        self.driver.back()
