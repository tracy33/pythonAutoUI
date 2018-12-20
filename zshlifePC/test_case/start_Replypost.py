#coding=utf-8
from selenium import webdriver
import unittest,time,os,re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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



class ReplyPost(unittest.TestCase):
    '''回帖'''
    def setUp(self):
        # self.driver=webdriver.Firefox()
        self.driver=webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        self.base_url="https://gz.qqzsh.com/f-65-1.htm"
        self.verificationsErrors=[]
        self.accept_next_alert=True
        cookiestr=zshlogin.login(un,pw,self.driver)

    def test_Replypost(self):
        u'''回帖测试（文字、表情、上传图片）'''
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
        nowhandle=driver.current_window_handle
        print "nowhandle:%s"%nowhandle        
        #下面这句点击会打开新窗口
        #driver.find_element_by_link_text("自动化脚本测试发帖").click()
        normal_list=driver.find_elements_by_class_name("bankuaizhuti")
        normal_list[0].find_element_by_class_name("xst").click()       
        time.sleep(3)

        #获得所有窗口
        allhandles=driver.window_handles
        print allhandles
        #循环判断窗口是否为当前窗口
        for handle in allhandles:
            if handle !=nowhandle:
                driver.switch_to_window(handle)
                print handle

        #发帖之前先看回复list的数目
        # post=driver.find_element_by_id("postlistreply").find_elements_by_class_name("zhanzhuai_replythread")
        post=driver.find_elements_by_css_selector("td[id^='postmessage_']")
        postnum=len(post)
        print postnum
        jsscr = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(jsscr)
        time.sleep(3)       
        driver.find_element_by_id("fastpostmessage").send_keys(u"自动化脚本测试回帖")
        driver.find_element_by_id("fastpostsml").click()
        ele=driver.find_element_by_id("fastpostsml_menu")
        ActionChains(driver).move_to_element(ele).perform()
        time.sleep(3)
        # the_element=False
        the_element=ElementJudge.is_element_visible(self,(By.ID,'smilie_83'))
        if the_element:
            driver.find_element_by_id("smilie_83").click()      
        else:
            js='document.getElementById("fastpostsml_menu").style.display="block";'
            driver.execute_script(js)
            driver.find_element_by_id("smilie_83").click()

        time.sleep(2)
        driver.find_element_by_id("fastpost_imgupload_fast").click()
        time.sleep(15)

        #当前文件的路径
        pwd=os.getcwd()
        #picdir=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"."+os.path.sep+"data")
        #有all_tests统一执行就不需要父路径了，如下
        picdir=os.path.abspath(pwd+os.path.sep+"data")
        picpath=os.path.join(picdir,"testpic.JPG")

        # print picpath

        guiUpFile.win32Up(driver,picpath)
        time.sleep(15)
        imgs=len(driver.find_elements_by_css_selector("a[onclick*='insertAttachimgTag']"))
        # print (u"图片数量：%s"%(imgs))
        if imgs>0:
            print u"图片上传成功"

        else:
            print u"图片上传失败"

        driver.find_element_by_id("fastpostsubmit").submit()
        time.sleep(10)
        #验证发帖是否成功
        driver.refresh()
        # post2=driver.find_element_by_id("postlistreply").find_elements_by_class_name("zhanzhuai_replythread")
        post2=driver.find_elements_by_css_selector("td[id^='postmessage_']")
        postnum2=len(post2)
        print postnum2
        if postnum2==postnum+1:
            print u"回帖成功" 
        else:
            print u"回帖失败"
        time.sleep(5)








    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

