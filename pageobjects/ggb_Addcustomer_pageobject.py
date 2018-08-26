#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11:33
# @Author  : Carewn
# @Software: PyCharm


class AddCustomer(object):

    #客户姓名
    CustomerName = 'xpath=>/html/body/div[5]/div[2]/div[1]/div[1]/form/div/div/div[2]/div[1]/div/input'
    #客户昵称
    CustomerNames = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[2]/div/input'
    #客户手机号
    CustomerTelphone = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[3]/div/input'
    #备用手机
    CusetomerTelphoneTwo = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[4]/div/input'
    #性别
    CustomerSex = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[5]/div/input'
    #生日
    CustormerBirthday = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[6]/div/input'
    #所属顾问门店
    CustomerMerchant = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[7]/div[1]/select'
    #所属顾问姓名
    CustomerMerchantGuwen = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[7]/div[2]/select'
    #是否是股东
    IsShareholder = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[8]/div[2]/div/div[1]/label'
    NoShareholder = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[8]/div[1]/div/div[1]/label'
    #微信号
    Careslten = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[10]/div/input'
    #邮箱
    CustormerEmail = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[12]/div/input'
    #工作单位
    WorkUnit = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[14]/div/input'
    #客户来源
    CustorSource = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[18]/div/select'
    #地址（省）
    Address_shen = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[20]/div[1]/select'
    #地址（市）
    Address_shi = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[20]/div[2]/select'
    #地址（区）
    Address_qu = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[20]/div[3]/select'
    #详细地址
    DetailedAddress = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[20]/div[4]/input'
    #特殊需求
    SpecialNeeds = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[22]/div/textarea'
    #客户简介
    CustormerProfile = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[24]/div/textarea'
    #兴趣爱好
    Hobby = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[26]/div/textarea'
    #保存按钮
    Preservation = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[29]/button[1]'
    #取消按钮
    Cancel = 'xpath=>/html/body/div[5]/div[2]/div/div/form/div/div/div[2]/div[29]/button[2]'
    #确定取消
    IsCancel = 'xpath=>/html/body/div[6]/div[3]/a[1]'
    #不取消
    NoCancel = 'xpath=>/html/body/div[6]/div[3]/a[2]'
    #提示信息
    Prompt = 'xpath=>/html/body/div[-1]/div/div'

