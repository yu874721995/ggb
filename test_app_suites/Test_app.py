# -*- coding : utf-8 -*-
# @Auther    : Careslten
# @time      : 2021/1/30 18:27
# @File      : Test_app.py
# @SoftWare  : appium_jskj

from framwork.app_engine import BrowserEngine
from framwork.app_base_page import app_BassPage
import unittest,time
from random import randint
import requests

class Test_Index_projectreceipt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_app(1)
        cls.app = app_BassPage(cls.driver)
        cls.driver2 = BrowserEngine(cls).open_app(0)
        cls.app2 = app_BassPage(cls.driver2)

    @classmethod
    def tearDownClass(cls):
        cls.app.close_app()
        cls.driver.quit()
        cls.app2.close_app()
        cls.driver2.quit()

    def test_Index_commodityOrder(cls):
        '''验证app登录'''
        phone = str(randint(17100000001, 17100010000))
        app1_current_package = cls.driver.current_package
        app2_current_package = cls.driver2.current_package
        cls.app.click(app1_current_package + ':id/permission_allow_button')#允许权限
        cls.app.click("com.dengta.date:id/btn_user_privacy_policy_summary_agree")#同意协议
        cls.app.click("com.dengta.date:id/ll_login_select_cellphone_login_register")#其他手机号码注册
        cls.app.send_keys("com.dengta.date:id/et_login_phone_number_new", phone)#输入手机
        cls.app.send_keys("com.dengta.date:id/et_login_code", '80008')#输入验证码
        cls.app.click("com.dengta.date:id/btn_login_sure")#点击登录
        cls.app.click('com.dengta.date:id/btn_inviteCode_cancel')#跳过邀请码
        cls.app.click('com.dengta.date:id/iv_register_sex_girl')#选择性别

        cls.app2.click(app2_current_package + ':id/permission_allow_button')#允许权限
        time.sleep(3)
        cls.app2.click("com.dengta.date:id/btn_user_privacy_policy_summary_agree")#同意协议

        cls.app.click('com.dengta.date:id/btn_register_sex_sure')#确认性别
        cls.app.send_keys('com.dengta.date:id/et_nick_name', '兮兮')#输入昵称
        cls.app.click('com.dengta.date:id/ll_register_info_nickname')#随机昵称
        cls.app.click('com.dengta.date:id/iv_register_avatar_set_avatar')#点击头像
        cls.app.click('com.dengta.date:id/tv_select_avatar_select_from_album')#选择相册
        cls.app.click(app1_current_package + ':id/permission_allow_button')#点击允许
        cls.app.click(app1_current_package + ':id/permission_allow_button')#点击允许
        cls.app.click('com.dengta.date:id/tvCheck')#选择一张图片
        cls.app.click('com.dengta.date:id/picture_send')#点击确定
        cls.app.click('com.dengta.date:id/menu_crop')#裁剪确定
        cls.app.click('com.dengta.date:id/btn_register_info_next_step')#确定注册
        cls.app.click('com.dengta.date:id/btn_sign_in')
        cls.app.click('com.dengta.date:id/btn_confirm')#签到
        cls.app.click('com.dengta.date:id/iv_recharge_activities_close')

        cls.app2.click("com.dengta.date:id/ll_login_select_cellphone_login_register")#其他手机号码注册
        cls.app2.send_keys("com.dengta.date:id/et_login_phone_number_new", '15900001016')#输入手机
        cls.app2.send_keys("com.dengta.date:id/et_login_code", '80008')#输入验证码
        cls.app2.click("com.dengta.date:id/btn_login_sure")#点击登录

        cls.app.click('com.dengta.date:id/item_short_video_avatar_civ')#视频头像
        cls.app.click('com.dengta.date:id/simpleDraweeView_user_info_avatar')#点击头像
        cls.app.back()
        cls.app.click('com.dengta.date:id/frag_user_info_guardian_tv')#返回
        cls.app.click('com.dengta.date:id/iv_title_common_back')
        cls.app.click('com.dengta.date:id/frag_detail_bottom_attention_ll')
        assert cls.app.app_find_element('com.dengta.date:id/tv_commit')#是否出现私密分组的弹窗
        cls.app.click('com.dengta.date:id/tv_commit')#点击确定
        #设置私密分组密码密码
        cls.app.send_keys('com.dengta.date:id/et_pwd','666666')
        cls.app.click('com.dengta.date:id/tv_commit')
        cls.app.send_keys('com.dengta.date:id/et_pwd','888888')
        cls.app.click('com.dengta.date:id/tv_commit')
        cls.app.click('com.dengta.date:id/tv_commit')
        cls.app.click('com.dengta.date:id/tv_commit')
        cls.app.click('com.dengta.date:id/frag_user_info_guardian_tv')#点击守护榜
        cls.app.click('com.dengta.date:id/iv_title_common_back')#点击返回
        cls.app.click('com.dengta.date:id/frag_user_detail_followed_iv')#点击取消关注
        cls.app.click('com.dengta.date:id/dialog_comm_confirm_tv')#点击确定
        cls.app.back()
        cls.app.click('com.dengta.date:id/home_page_video_search_iv')#点击搜索
        cls.app.send_keys('com.dengta.date:id/et_video_search_content','123456')#输入搜索内容
        cls.app.click('com.dengta.date:id/tv_video_search_search')#点击搜索


        cls.app2.click(app2_current_package + ':id/permission_allow_button')#允许权限
        try:
            cls.app2.click('com.dengta.date:id/iv_recharge_activities_close')
        except:
            pass
        cls.app2.app_find_elements('com.dengta.date:id/icon')[1].click()#点击直播
        cls.app2.click('com.dengta.date:id/btn_youth_mode_i_know')#青少年模式
        cls.app2.click('com.dengta.date:id/btn_open')
        cls.app2.click(app2_current_package + ':id/permission_allow_button')

        cls.app.app_find_elements('com.dengta.date:id/iv_item_user_detail_short_video_pic')[0].click()#点击搜索结果中的第一个
        cls.app.click('com.dengta.date:id/frag_short_video_video_back_iv')#点击返回
        cls.app.click('com.dengta.date:id/tv_video_search_type')#点击更换搜索方式
        cls.app.click('com.dengta.date:id/tv_video_search_title')#点击标题
        cls.app.click('com.dengta.date:id/tv_video_search_search')#点击搜索
        cls.app.click('com.dengta.date:id/iv_item_user_detail_short_video_pic')#点击第一个
        cls.app.click('com.dengta.date:id/frag_short_video_video_back_iv')#点击返回
        cls.app.click('com.dengta.date:id/iv_video_search_back')#再返回
        cls.app.click('com.dengta.date:id/tem_short_video_like_svgiv')
        cls.app.click('com.dengta.date:id/item_short_video_comment_tv')
        cls.app.click('com.dengta.date:id/layout_comment_input_tv')
        cls.app.send_keys('com.dengta.date:id/layout_edit_comment_input_edt','test')#输入test
        cls.app.click('com.dengta.date:id/layout_edit_comment_submit_tv')
        assert cls.app.text('com.dengta.date:id/item_video_comment_content_tv') == 'test'
        cls.app.click('com.dengta.date:id/item_video_comment_like_iv')#点赞评论
        cls.app.back()
        cls.app.click('com.dengta.date:id/item_short_video_forward_tv')#点击分享
        cls.app.click('com.dengta.date:id/item_share_item_icon_iv')#分享到微信
        time.sleep(3)
        cls.app.click('com.dengta.date:id/dialog_share_confirm_text_tv')#点击分享
        cls.app.back()
        cls.app.app_find_elements('com.dengta.date:id/icon')[1].click()#点击直播
        cls.app.click('com.dengta.date:id/btn_youth_mode_i_know')#青少年模式
        cls.app.click('com.dengta.date:id/btn_open')#开启定位
        try:
            cls.app.click(app1_current_package + ':id/permission_allow_foreground_only_button')
        except:
            cls.app.click(app1_current_package + ':id/permission_allow_button')#同意权限
        cls.app.click('com.dengta.date:id/iv_ta_live_live_like')#点击关注的主播
        cls.app.back()

        cls.app2.click('com.dengta.date:id/iv_ta_live_start_live')#开播
        cls.app2.click(app2_current_package + ':id/permission_allow_button')
        cls.app2.click(app2_current_package + ':id/permission_allow_button')
        cls.app2.click(app2_current_package + ':id/permission_allow_button')

        cls.app.click('com.dengta.date:id/iv_ta_live_start_live')#点击开播
        cls.app.click(app1_current_package + ':id/permission_allow_button')#同意权限
        cls.app.click('com.dengta.date:id/btn_common_sure_no_bg_sure')#去申请
        cls.app.send_keys('com.dengta.date:id/et_input_real_name','余孛')
        cls.app.send_keys('com.dengta.date:id/et_input_card_id','454602154545321234541')
        cls.app.click('com.dengta.date:id/img_bg_two')
        cls.app.click('com.dengta.date:id/tv_select_avatar_select_from_album')
        cls.app.click('com.dengta.date:id/tvCheck')  # 选择一张图片
        cls.app.click('com.dengta.date:id/picture_send')  # 点击确定
        cls.app.click('com.dengta.date:id/img_bg_three')
        cls.app.click('com.dengta.date:id/tv_select_avatar_select_from_album')
        cls.app.click('com.dengta.date:id/tvCheck')  # 选择一张图片
        cls.app.click('com.dengta.date:id/picture_send')  # 点击确定
        cls.app.click('com.dengta.date:id/btn_submit')#提交申请
        cls.app.click('com.dengta.date:id/btn_back')#点击返回
        cls.app.click('com.dengta.date:id/et_ta_live_search')
        cls.app.send_keys('com.dengta.date:id/et_user_search_content','的')
        cls.app.click('com.dengta.date:id/tv_user_search_search')#点击搜索
        assert cls.app.app_find_elements('com.dengta.date:id/fl_item_homepage_list_avatar')
        cls.app.click('com.dengta.date:id/fl_item_homepage_list_avatar')#点击进入用户主页
        cls.app.back()
        cls.app.click('com.dengta.date:id/iv_user_search_back')#返回
        cls.app.click('com.dengta.date:id/banner_general_blind_date')#点击banner
        cls.app.click('com.dengta.date:id/top_bar_left_iv')#点击返回
        cls.app.click('com.dengta.date:id/iv_ta_live_all_net_list')#点击全网榜单
        cls.app.click('xpath=>//androidx.appcompat.app.ActionBar.Tab[@content-desc="上周榜"]/android.widget.TextView')
        assert cls.app.app_find_elements('com.dengta.date:id/tv_item_net_list_noun')
        cls.app.click('xpath=>//androidx.appcompat.app.ActionBar.Tab[@content-desc="PK榜"]/android.view.ViewGroup')#pk榜
        cls.app.click('xpath=>//androidx.appcompat.app.ActionBar.Tab[@content-desc="富豪榜"]/android.view.ViewGroup')#富豪榜
        cls.app.click('xpath=>//androidx.appcompat.app.ActionBar.Tab[@content-desc="上月榜"]/android.widget.TextView')#上月榜
        cls.app.back()






        cls.app2.click('com.dengta.date:id/btn_i_know')#我知道了
        cls.app2.click('com.dengta.date:id/et_start_live_title')
        cls.app2.send_keys('com.dengta.date:id/et_start_live_title','test')
        cls.app2.click('com.dengta.date:id/tv_start_live_theme')#主题
        cls.app2.click('com.dengta.date:id/tv_theme_content')
        cls.app2.click('com.dengta.date:id/btn_commit')
        while 1:
            if cls.app2.text('com.dengta.date:id/tv_start_live_position') == '深圳市':
                break
            else:
                continue
        cls.app2.click('com.dengta.date:id/btn_start_live_open_live')#开播
        cls.app2.click('com.dengta.date:id/iv_live_bottom_more')#工具箱
        cls.app2.click('com.dengta.date:id/tv_personal_live_tool_box_beauty')#美颜
        cls.app2.back()
        cls.app2.click('com.dengta.date:id/iv_live_bottom_more')#工具箱
        cls.app2.click('com.dengta.date:id/iv_personal_live_tool_box_fee_setting_anim')#收费设置
        cls.app2.click('com.dengta.date:id/iv_personal_live_fee_setting_apply_seat_arrow')#进入设置
        cls.app2.click('com.dengta.date:id/btn_confirm')#点击确定
        cls.app2.click('com.dengta.date:id/tv_personal_live_base_alert_dialog_positive')#保存成功弹窗


        cls.app.click('com.dengta.date:id/title_img')
        cls.app.click('com.dengta.date:id/iv_item_personal_live_pic')#点击直播间
        cls.app.click('com.dengta.date:id/tv_live_top_group_status')#关注
        cls.app.click('com.dengta.date:id/iv_live_top_anchor_avatar')#查看主播资料卡
        cls.app.click('com.dengta.date:id/tv_other_user_info_manager')#举报
        cls.app.click('com.dengta.date:id/frag_report_rv')#选一个
        cls.app.click('com.dengta.date:id/item_src_iv')
        cls.app.click('com.dengta.date:id/tv_select_avatar_select_from_album')
        cls.app.click('com.dengta.date:id/tvCheck')  # 选择一张图片
        cls.app.click('com.dengta.date:id/picture_send')  # 点击确定
        cls.app.click('com.dengta.date:id/frag_report_content_commit_tv')#提交
        zhubo_ziliaoka_name = cls.app.text('com.dengta.date:id/tv_other_user_info_name')
        cls.app.click('com.dengta.date:id/iv_other_user_info_noble_avatar')
        zhubo_name = cls.app.text('com.dengta.date:id/frag_user_detail_user_nickname_tv')
        assert zhubo_ziliaoka_name == zhubo_name
        cls.app.back()
        cls.app.click('com.dengta.date:id/iv_live_top_anchor_avatar')
        try:
            cls.app.click('com.dengta.date:id/iv_other_user_info_guard_avatar')
            shouhuname = cls.app.text('com.dengta.date:id/frag_user_detail_user_nickname_tv')
            assert zhubo_ziliaoka_name != shouhuname
            cls.app.back()  # 返回
        except Exception:
            pass
        cls.app.click('com.dengta.date:id/tv_other_user_info_ait_ta')#@ta
        cls.app.send_keys('com.dengta.date:id/et_dialog_live_edit_comment','test')
        cls.app.click('com.dengta.date:id/tv_dialog_live_edit_comment_send')#发送
        cls.app.click('com.dengta.date:id/tv_live_top_members_count')#在线用户
        assert cls.app.app_find_elements('com.dengta.date:id/fl_audience_online_user_avatar_frame')
        cls.app.click('com.dengta.date:id/iv_live_room_online_user_close')
        cls.app.click('com.dengta.date:id/iv_reward_top')
        cls.app.click('xpath=>//androidx.appcompat.app.ActionBar.Tab[@content-desc="贡献总榜"]/android.widget.TextView')
        cls.app.back()
        cls.app.click('com.dengta.date:id/tv_live_bottom_say_something')#点击消息一层
        cls.app.send_keys('com.dengta.date:id/et_dialog_live_edit_comment',111)#发消息
        cls.app.click('com.dengta.date:id/tv_dialog_live_edit_comment_send')#点击确定
        cls.app.click('com.dengta.date:id/iv_live_bottom_audience_share')#点击分享
        cls.app.click('com.dengta.date:id/tv_personal_live_share_wechat_friends')
        cls.app.back()
        cls.app.click('com.dengta.date:id/iv_live_bottom_audience_share')  # 点击分享
        cls.app.click('com.dengta.date:id/tv_personal_live_share_date_friends')#分享到等他
        cls.app.click('xpath=>//androidx.appcompat.app.ActionBar.Tab[@content-desc="关注 2"]/android.widget.TextView')
        cls.app.click('com.dengta.date:id/item_friend_select_cb')
        cls.app.click('com.dengta.date:id/frag_friend_main_toolbar_complete_tv')#确定


        cls.app.click('com.dengta.date:id/iv_live_bottom_call')#连麦
        cls.app.click('com.dengta.date:id/tv_apply_unapply_seat')
        while 1:
            if cls.app2.element_is('com.dengta.date:id/ll_live_audience_apply_call'):
                break
            else:
                continue
        cls.app2.click('com.dengta.date:id/ll_live_audience_apply_call')#接受
        cls.app2.click('com.dengta.date:id/tv_user_info_common_status')#接受
        time.sleep(3)
        assert cls.app.element_is('com.dengta.date:id/rl_audience_preview')
        cls.app.click('com.dengta.date:id/iv_switch_camera')#翻转摄像头
        cls.app.click('com.dengta.date:id/iv_audience_close_video')#关闭连麦
        try:
            cls.app.click('com.dengta.date:id/tv_personal_live_base_alert_dialog_positive')
        except:
            pass
        time.sleep(3)
        assert cls.app2.element_is('com.dengta.date:id/rl_audience_preview') == False


        cls.app.click('com.dengta.date:id/iv_live_bottom_flower')
        cls.app.click('com.dengta.date:id/btn_send_flower_handsel')
        cls.app.click('com.dengta.date:id/iv_live_bottom_audience_gift')#礼物盒
        cls.app.click('com.dengta.date:id/iv_send_personal_live_gift_item_icon')#第一个礼物
        assert cls.app.element_is('com.dengta.date:id/svgaimg_user_level_up')


        cls.app.click('com.dengta.date:id/iv_live_bottom_private_room')  # 转私密房
        cls.app.click('com.dengta.date:id/tv_apply_private_room_confirm_dialog_sure')  # 点击确定
        time.sleep(1)
        assert cls.app2.element_is('com.dengta.date:id/ll_live_audience_apply_private_room')
        cls.app2.click('com.dengta.date:id/ll_live_audience_apply_private_room')
        cls.app2.click('com.dengta.date:id/tv_user_info_common_status')#接受私密房
        cls.app2.click('com.dengta.date:id/tv_apply_private_room_confirm_dialog_sure')
        time.sleep(3)
        cls.app2.click('com.dengta.date:id/tv_personal_room_settlement_close')
        cls.app2.click('com.dengta.date:id/rl_open_live_income')#开播收益
        cls.app.click('com.dengta.date:id/iv_live_top_close')#关闭直播间
        cls.app.click('com.dengta.date:id/tv_personal_live_base_alert_dialog_positive')
        cls.app2.click('com.dengta.date:id/tv_anchor_live_end_click_exit')#退出开播结束页

        r = requests.post('http://192.168.10.197:9001/zhuboshenhe',data={
            'phone':phone,
            'config':'4'
        })
        assert r.json()['status'] == 1
        cls.app.click('com.dengta.date:id/iv_ta_live_start_live')#1号开播
        cls.app2.click('com.dengta.date:id/iv_ta_live_start_live')#2号开播
        cls.app.click('com.dengta.date:id/btn_i_know')
        cls.app.click('com.dengta.date:id/btn_start_live_open_live')
        cls.app2.click('com.dengta.date:id/btn_start_live_open_live')

        #pk
        cls.app.click('com.dengta.date:id/iv_live_bottom_pk')
        cls.app2.click('com.dengta.date:id/iv_live_bottom_pk')
        cls.app.click('com.dengta.date:id/iv_personal_live_create_pk_reward')
        cls.app2.click('com.dengta.date:id/iv_personal_live_create_pk_reward')
        cls.app.click('com.dengta.date:id/iv_personal_live_reward_pk_random_match')
        cls.app2.click('com.dengta.date:id/iv_personal_live_reward_pk_random_match')
        assert cls.app.element_is('com.dengta.date:id/ll_anchor_video')
        assert cls.app2.element_is('com.dengta.date:id/ll_anchor_video')
        cls.app.click('com.dengta.date:id/btn_live_pk_state')
        cls.app2.click('com.dengta.date:id/btn_live_pk_state')
        time.sleep(3)
        assert cls.app.text('com.dengta.date:id/tv_live_pk_start_count_down') != '' and \
               cls.app.text('com.dengta.date:id/tv_live_pk_start_count_down').split(':')[0] == '05'
        assert cls.app2.text('com.dengta.date:id/tv_live_pk_start_count_down') != '' and \
               cls.app2.text('com.dengta.date:id/tv_live_pk_start_count_down').split(':')[0] == '05'
        cls.app.click('com.dengta.date:id/iv_live_pk_top_close')
        cls.app.click('com.dengta.date:id/tv_personal_live_base_alert_dialog_positive')
        cls.app.click('com.dengta.date:id/iv_live_top_close')
        cls.app2.click('com.dengta.date:id/iv_live_top_close')




        time.sleep(10)









if __name__ == "__main__":
    unittest.main()