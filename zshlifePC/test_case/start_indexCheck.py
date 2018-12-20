#coding=utf-8
from selenium import webdriver
#import requests
import unittest,time
from selenium.common.exceptions import NoSuchElementException
import json
# from pyquery import PyQuery as pq
#from pyvirtualdisplay import Display

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# sys.path.append(".\\public")
# from public import *
# un=''
# pw=''
# cookiestr=""
# cookiestr=zshlogin.login(un,pw)
# display=Display(visible=0,size=(800,600))
# display.start()

class ZshIndex(unittest.TestCase):
    '''首页'''
    def setUp(self):
        # self.driver=webdriver.Firefox()
        self.driver=webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        self.base_url="https://gz.qqzsh.com/portal.php"
        self.verificationsErrors=[]
        self.accept_next_alert=True

    def test_indexCheck(self):
        u'''首页空白页检测'''
        driver=self.driver
        startTime = time.time()
        print "首页加载start time is: %0.3f"%startTime
        #设定页面加载限制时间
        driver.set_page_load_timeout(60)
        try:
            driver.get(self.base_url)
        except:
            print '首页加载time out after 60 seconds when loading page'
            driver.execute_script('window.stop()') #当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作
        # driver=webdriver.Firefox()
        zhuanti=driver.find_elements_by_class_name("zhanzhuai_imga")
        print u"专题滑动图片数：%d\n" %len(zhuanti)
        hot_forum=driver.find_element_by_css_selector("div[class='sidebar_con con_list_t']").find_elements_by_tag_name("img")
        print u"热门板块图标数：%d\n" %len(hot_forum)
        zhuanti_tjimg=driver.find_elements_by_css_selector("div[class='zhanzhuai_imgteaser']")
        print u"专题推荐图片数：%d\n" %len(zhuanti_tjimg)
        zhuanti_tjtid=driver.find_element_by_css_selector("div[class='recommend_article_list clearfix']").find_elements_by_tag_name("a")
        print u"专题推荐帖子链接数：%d\n" %len(zhuanti_tjtid)
        jingcai_acti=driver.find_element_by_id("frameWyB4Yw_left").find_elements_by_tag_name("a")
        print u"精彩活动列表活动数：%d\n" %len(jingcai_acti)
        # dayhottab=driver.find_element_by_css_selector("div[class='tab-key active']").click()
        # dayhotthread=driver.find_element_by_css_selector("div[class='sidebar_con sidebar_recommend tab-views']").find_elements_by_tag_name("a")
        # print "每日热帖数：%d\n" %len(dayhotthread)
        rank=driver.find_element_by_id("framecUZnwB").find_elements_by_tag_name("a")
        print u"荣耀榜人数：%d\n" %len(rank)
        zhuanti=driver.find_elements_by_id("zhanzhuai_p_list")
        print u"专题区域帖子数：%d\n" %len(zhuanti)






    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

# display.stop()
