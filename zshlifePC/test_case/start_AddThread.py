#coding=utf-8
from selenium import webdriver
import unittest,time,os,re
from selenium.common.exceptions import NoSuchElementException

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")
from public import *
logindata=open(".\\test_case\\public\\data.txt",'r')
un=''
pw=''
line=logindata.readline()
un,pw=line.split(',')
un=un.strip('\t\r\n')
pw=pw.strip('\t\r\n')
cookiestr=""



class AddThread(unittest.TestCase):
    '''发帖'''
    def setUp(self):
        # self.driver=webdriver.Firefox()
        self.driver=webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        self.base_url="https://gz.qqzsh.com/forum.php?mod=post&action=newthread&fid=65"
        self.verificationsErrors=[]
        self.accept_next_alert=True
        cookiestr=zshlogin.login(un,pw,self.driver)

    def test_addThread(self):
        u'''发帖测试'''
        driver=self.driver
        driver.get(self.base_url)
        # driver=webdriver.Firefox()
        time.sleep(3)
        driver.find_element_by_id("subject").send_keys(u"自动化脚本测试发帖")
        driver.find_element_by_id("e_controls").find_element_by_id("e_adv_s1").find_element_by_css_selector("a[id='e_image']").click()
        time.sleep(3)
        driver.find_element_by_id("e_image_menu").find_element_by_id("imgattachnew_1").click()
        time.sleep(3)

        #当前文件的路径
        pwd=os.getcwd()
        #picdir=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"."+os.path.sep+"data")
        
        #有all_tests统一执行就不需要父路径了，如下
        picdir=os.path.abspath(pwd+os.path.sep+"data")
        picpath=os.path.join(picdir,"testpic.JPG")

        # print picpath

        guiUpFile.win32Up(driver,picpath)
        time.sleep(20)
        imgs=len(driver.find_elements_by_css_selector("img[onclick*='insertAttachimgTag']"))
        if imgs>0:
            print u"图片上传成功"
            #插入图片
            driver.find_element_by_xpath("//*[@id='e_imgattachlist']/div[2]/button/strong").click()

        else:
            print u"图片上传失败"
            #关闭上传图片框
            driver.find_element_by_xpath("//*[@id='e_image_ctrl']/li[1]/span").click()

        
        time.sleep(5)
        driver.switch_to_frame("e_iframe")
        #输入发帖文字内容
        driver.find_element_by_tag_name("body").send_keys(u"测试发帖文字内容")
        #跳出iframe
        driver.switch_to_default_content()
        driver.find_element_by_id("postsubmit").submit()
        time.sleep(5)
        startTime = time.time()
        print "发帖后加载页面start time is: %0.3f"%startTime
        #设定页面加载限制时间
        driver.set_page_load_timeout(60)
        try:
            driver.refresh()
        except:
            print '发帖后加载页面time out after 60 seconds when loading page'
            driver.execute_script('window.stop()') #当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作
        #验证发帖是否成功
        sb=driver.find_element_by_id("thread_subject").text
        if sb==u"自动化脚本测试发帖":
            print u"发帖成功" 
        else:
            print u"发帖失败"
        #time.sleep(5)








    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

