#coding=utf-8
from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")
from public import *
logindata=open(".\\test_case\\public\\data.txt",'r')
#logindata=open(".\\public\\data.txt",'r')
un=''
pw=''
line=logindata.readline()
un,pw=line.split(',')
un=un.strip('\t\r\n')
pw=pw.strip('\t\r\n')

class ZshLogin(unittest.TestCase):
    '''最生活登录'''
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.verificationsErrors=[]
        self.accept_next_alert=True

    def test_QQlogin(self):
        u'''最生活QQ登录'''
        cookiestr=zshlogin.login(un,pw,self.driver)
        # print cookiestr







    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
