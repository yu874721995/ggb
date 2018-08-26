#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9:36
# @Author  : Carewn
# @Software: PyCharm

from framwork.base_page import BassPage



class Customer_page(BassPage):

    #新增客户
    NewAddCustomer = 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/div[1]/button'
    #搜索输入框
    FindInput = 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/div/input'
    #搜索按钮
    FindClick = 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/div/div/button'
    #高级搜索
    AdvancedSearch = 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/button'\
    #生日
    Today_birthday = ['xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[2]/ul/li[2]',
                      'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[2]/ul/li[3]',
                      'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[2]/ul/li[4]']
    #预约
    Subscribe = ['xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[3]/ul/li[2]',
                 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[3]/ul/li[3]',
                 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[3]/ul/li[4]']
    #客户类型
    CustomerType = ['xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[4]/ul/li[2]',
                    'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[4]/ul/li[3]',
                    'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[4]/ul/li[4]']
    #客户身份
    CustomerIdentity = ['xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[5]/ul/li[2]',
                        'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[5]/ul/li[3]',
                        'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[5]/ul/li[4]',
                        'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[5]/ul/li[5]',
                        'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/ul/li[5]/ul/li[6]'
                        ]
    #取消所选店铺
    Delmerchant = 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/p/span/i'
    #客户信息
    customer = 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[1]/table/tbody/tr[1]'
    #第二页
    SecondPages = 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/ul/li[4]/span'
    #下一页
    NextPage = 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/ul/li[7]/span'
    #客户数量
    CusetomerNumber = 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/ul/li[10]'





