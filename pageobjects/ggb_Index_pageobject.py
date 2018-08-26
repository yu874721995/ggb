#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16:40
# @Author  : Carewn
# @Software: PyCharm

from framwork.base_page import BassPage
import os,time
from selenium import webdriver



class IndexPage(BassPage):

    #首页图标
    IndexClick = 'xpath=>/html/body/div[2]/div[1]/header/div/div[1]'
    #全部门店
    Indexmerchant_all = 'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/ul/li/ul/li[1]'
    #客户管理
    Customer = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[1]/a/span[1]/span[2]'
    #项目订单
    ProjectReceipt = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[2]/a/span[1]/span[2]'
    #预定表
    Booking = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[3]/a/span[1]/span[2]'
    #商品订单
    CommodityOrder = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[4]/a/span[1]/span[2]'
    #美丽金管理
    ZjcAdministration = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[5]/a/span[1]/span[2]'
    #会员卡管理
    ClubAmministration = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[6]/a/span[1]/span[2]'
    #品项管理
    ItemManagement = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[7]/a/span[1]/span[2]'
    #活动管理
    ActivityManagement = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[8]/a/span[1]/span[2]'
    #财务结算
    Financialsettlement = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[9]/a/span[1]/span[2]'
    #数据报表
    Datareport = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[10]/a/span[1]/span[2]'
    #报表中心
    Reportcenter = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[10]/a/span[1]/span[2]'
    #团队管理
    TeamManagement = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[12]/a'
    #人事管理
    PersonnelManagement = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[13]/a/span[1]/span[2]'
    #分红管理
    DividendManagement = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[14]/a/span[1]/span[2]'
    #参数设置
    ParameterSetting = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[15]/a/span[1]/span[2]'
    #系统管理
    SystemManagement = 'xpath=>/html/body/div[2]/div[2]/aside/div/div[1]/ul/li[16]/a/span[1]/span[2]'
    #营收数据
    RevenueData = ['xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]',
                   'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]',
                   'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div[1]',
                   'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[4]/div/div[1]',
                   'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[5]/div/div[1]',
                   'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[6]/div/div[1]',
                   'xpath=>/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[7]/div/div[1]',
                   ]

    def Indexclickall(self):
        self.click(self.Indexmerchant_all)

    def projectrecript_Num(self):
        self.click(self.ProjectReceipt)





