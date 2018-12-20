#coding=utf-8
from selenium import webdriver
import unittest,time,os,re,requests
from selenium.common.exceptions import NoSuchElementException

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")
from public import *



class ForumList(unittest.TestCase):
    '''板块'''
    def setUp(self):
        # self.driver=webdriver.Firefox()
        self.driver=webdriver.Chrome()
        self.base_url="https://gz.qqzsh.com/f-201-1.htm"
        self.verificationsErrors=[]
        self.accept_next_alert=True

    def test_ForumList(self):
        u'''板块列表测试'''
        driver=self.driver
        startTime = time.time()
        print "板块列表加载start time is: %0.3f"%startTime
        #设定页面加载限制时间
        driver.set_page_load_timeout(60)
        try:
            driver.get(self.base_url)
        except:
            print '板块列表time out after 60 seconds when loading page'
            driver.execute_script('window.stop()') #当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作
        # driver=webdriver.Firefox()
        #全站置顶检测
        topnum=driver.find_elements_by_css_selector("img[alt='全局置顶']")
        self.assertTrue(len(topnum)>1)
        print ("全局置顶贴子数：%s" %len(topnum))

        recomnum=driver.find_elements_by_css_selector("img[alt='本版推荐']")
        self.assertTrue(len(recomnum)>1)
        print ("本版推荐贴子数：%s" %len(recomnum))

        #翻页到第二页
        driver.find_element_by_xpath("//*[@id='fd_page_bottom']/div/a[1]").click()
        time.sleep(5)
        threadnum=driver.find_elements_by_class_name("bankuaizhuti")
        self.assertTrue(len(threadnum)==30)
        print  ("第二页板块主题数：%s" %len(threadnum))

        #查看热门板块图片数
        hotnum=driver.find_element_by_id("portal_block_130_content").find_elements_by_tag_name("img")
        self.assertTrue(len(hotnum)==12)
        print  ("热门板块数：%s" %len(hotnum))

        #检查右侧第二个广告图,需要先switch到iframe
        driver.switch_to_frame(driver.find_element_by_css_selector("iframe[src$='details2']"))
        links=driver.find_element_by_id("gd_sq_sy_Rectangle2").find_elements_by_tag_name("a")
        self.assertTrue(len(links)==2)
        print  ("第二个广告位包含链接数：%s" %len(links))
        bgimg=links[0].value_of_css_property("background-image")
        imgurl=re.findall('\"(.*?)\"',bgimg) #提取出来的字符串是list形式，用读取列表形式(如list[0])即可获得想要的值
        #用requests的方法验证图片是否可以访问（能方位即可以正常显示）
        self.assertEqual(requests.get(imgurl[0]).status_code,200)
        print ("第二个广告位背景图链接：%s" %imgurl[0])


        #检查右侧第三个广告位图，需要先switch到iframe
        driver.switch_to_default_content() #先跳出上面这个iframe
        driver.switch_to_frame(driver.find_element_by_css_selector("iframe[src$='details3']"))
        links_3=driver.find_element_by_id("gd_sq_sy_Rectangle3").find_elements_by_tag_name("a")
        print  ("第三个广告位包含链接数：%s" %len(links_3))
        bgimg3=links_3[0].value_of_css_property("background-image")
        imgurl3=re.findall('\"(.*?)\"',bgimg3)
        self.assertEqual(requests.get(imgurl3[0]).status_code,200)
        print ("第三个广告位背景图链接：%s" %imgurl3[0])









    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

