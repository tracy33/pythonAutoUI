#coding=utf-8
from selenium import webdriver
import unittest,time,os,re,requests
from selenium.common.exceptions import NoSuchElementException
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")
from public import *



class ThreadDetail(unittest.TestCase):
    def setUp(self):
        # self.driver=webdriver.Firefox()
        self.driver=webdriver.Chrome()
        self.base_url="https://gz.qqzsh.com/t-2095430-1.htm"  #https://gz.qqzsh.com/t-2099089-1.htm
        self.verificationsErrors=[]
        self.accept_next_alert=True

    def test_Detail(self):
        u'''帖子详情测试'''
        driver=self.driver
        startTime = time.time()
        print "start time is: %0.3f"%startTime
        #设定页面加载限制时间
        driver.set_page_load_timeout(60)
        #driver.maximize_window()
        try:
            driver.get(self.base_url)
        except:
            print 'time out after 60 seconds when loading page'
            driver.execute_script('window.stop()') #当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作
        # time.sleep(10)
        # driver=webdriver.Firefox()
        #检查详情页面的所有图片是否显示正常（requests返回200即可）
        imgs=driver.find_element_by_class_name("zhanzhuai_viewthread").find_elements_by_css_selector("img[onclick^='zoom(this, this.getAttribute']")
        print ("帖子详情图片总数：%s" %len(imgs))
        for img in imgs:
            imgurl=img.get_attribute('src')
            print ("图片链接：%s" %(imgurl))
            self.assertEqual(requests.get(imgurl).status_code,200)
        #检查评论区域的个数：总数=list的头像总数
        posts=driver.find_element_by_class_name("zhanzhuai_viewtitle").find_element_by_tag_name("h4").text
        postsnum=re.findall(r'\d+',posts)[0] #提取出来的字符串是list形式，用读取列表形式(如list[0])即可获得想要的值
        print ("评论统计数：%s" %(postsnum))
        p_lists=driver.find_elements_by_class_name("zhanzhuai_replythread")
        postlists=[]
        for p_list in p_lists:
            # for imgl in p_list.find_elements_by_css_selector("img[src*='avatar/']"):
            for imgl in p_list.find_elements_by_css_selector("a[class^='avtm']"):
                postlists.append(imgl)
        print ("回复列表头像数：%s" %len(postlists))
        self.assertEqual(string.atoi(postsnum),len(postlists))

        #板块推荐
        recomnum=driver.find_element_by_id("portal_block_133_content").find_elements_by_tag_name("img")
        self.assertTrue(len(recomnum)==12)
        print  ("板块推荐数：%s" %len(recomnum))        

        #检查全站推荐总数（第一个需要检查图片的显示)
        recomtrd=driver.find_element_by_id("portal_block_132_content").find_elements_by_tag_name("a")
        self.assertTrue(len(recomtrd)==11)
        print  ("全站推荐帖子数：%s" %len(recomtrd))
        recomimg_url=driver.find_element_by_id("portal_block_132_content").find_element_by_tag_name("img").get_attribute('src')
        print ("全站推荐图片链接：%s" %(recomimg_url))
        self.assertEqual(requests.get(recomimg_url).status_code,200)

        #检查电梯直达的有效性
        #js判断元素是否在可视区域内
        driver.find_element_by_css_selector("input[class='px p_fre z']").send_keys("2")
        time.sleep(3)
        #driver.find_element_by_css_selector("input[class='px p_fre z']").send_keys(Keys.TAB)
        element=driver.find_element_by_id("fj_btn")
        #点击电梯直达后会刷新界面，也设置一个超时时间
        startTime_left = time.time()
        print "电梯直达的start time is: %0.3f"%startTime_left
        try:
            driver.execute_script("arguments[0].click();",element)
        except:
            print 'time out after 60 seconds when click jump_left_button'
            driver.execute_script('window.stop()') #当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作
        # time.sleep(5)
        #调试滚动到底部的 postnum24764006 https://gz.qqzsh.com/t-2099089-1.htm
        '''
        jsscr = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(jsscr)
        time.sleep(3) 
        '''
        #postnum24757516  
        js="var obj=document.getElementById('postnum24618670');"+"var top = obj.getBoundingClientRect().top;"+"var se = document.documentElement.clientHeight;"+"visibl=false;"+"if(top<=se){visibl=true;};"+"return visibl;"
        flag=driver.execute_script(js)
        # print flag
        if flag:
            print ("电梯直达功能使用正常")
        else:
            # self.assertTrue(flag)
            print ("电梯直达功能使用有问题")










    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

