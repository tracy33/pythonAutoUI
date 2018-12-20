#coding=utf-8
from selenium import webdriver
import unittest,time,os,re,string
from selenium.common.exceptions import NoSuchElementException

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")
from public import *



class Forumtest(unittest.TestCase):
    '''论坛'''
    def setUp(self):
        # self.driver=webdriver.Firefox()
        self.driver=webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        self.base_url="https://gz.qqzsh.com/forum.php"
        self.verificationsErrors=[]
        self.accept_next_alert=True
        # cookiestr=zshlogin.login(un,pw,self.driver)

    def test_Forum(self):
        u'''论坛列表测试'''
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(10)
        # driver=webdriver.Firefox()
        todaynum=driver.find_element_by_xpath("//*[@id='chart']/p/em[1]").text
        # if(string.atoi(todaynum)>=0):
        #     print ("'今日'数字正常：%s" %(todaynum))
        # else:
        #     print ("'今日'数字异常：%s" %(todaynum))
        self.assertTrue(string.atoi(todaynum)>=0)
        print ("'今日'数字：%s" %(todaynum))
        yesterdaynum=driver.find_element_by_xpath("//*[@id='chart']/p/em[2]").text
        self.assertTrue(string.atoi(yesterdaynum)>=0)
        print ("'昨日'数字：%s" %(yesterdaynum))
        threadnum=driver.find_element_by_xpath("//*[@id='chart']/p/em[3]").text
        self.assertTrue(string.atoi(threadnum)>=0)
        print ("'帖子'数字：%s" %(threadnum))
        member=driver.find_element_by_xpath("//*[@id='chart']/p/em[4]").text
        self.assertTrue(string.atoi(member)>=0)
        print ("'会员'数字：%s" %(member))
        newmember=driver.find_element_by_xpath("//*[@id='chart']/p/em[5]").text        
        self.assertTrue(newmember)
        print ("'欢迎新会员'内容：%s" %(newmember))

        # categorys=driver.find_elements_by_css_selector("a[href^='forum.php?gid=']")
        categorys=driver.find_elements_by_css_selector("div[id^='category_']")
        self.assertTrue(len(categorys)>0)
        print ("论坛大分类数：%s" %(len(categorys)))
        i=1
        #subs=0
        for category in categorys:
            subcategorys=category.find_elements_by_tag_name("img")
            self.assertTrue(len(subcategorys)>0)
            print ("大分类%d的子分类数：%s" %(i,len(subcategorys)))
            i=i+1
            #subs=subs+len(subcategorys)

        #查看所有子分类的今日发帖数
        #statis=driver.find_elements_by_css_selector("em[title='今日']")
        #self.assertEqual(subs,len(statis))
        #print ("所有子分类总数：%s=%s" %(subs,len(statis)))
        #j=1
        #for stati in statis:
        #    tnum=re.findall('\((.*?)\)', stati.text)[0]
        #    self.assertTrue(tnum>=0)
        #    print ("子分类%d的今日发帖数：%s" %(j,tnum))
        #    j=j+1




    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

