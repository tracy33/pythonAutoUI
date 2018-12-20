#coding=utf-8
import requests,time
import unittest
from selenium.common.exceptions import NoSuchElementException
import json

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")


class SearchAPI(unittest.TestCase):
    '''搜索接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=search"

    def test_search_user(self):
        u'''搜索用户：对应搜索关键字有结果'''
        search_keyword='mary1ivy'
        payload={'type':'user','page':'1','keyword':search_keyword}
        time.sleep(8)
        r=requests.post(url=self.url,data=payload)
        self.result=r.json()
        # print self.result
        self.assertEqual(self.result['status'],0)
        self.assertTrue(len(self.result['data']['user'])>=1)
        print ("搜索第一页用户个数：%s" %len(self.result['data']['user']))
        self.assertIn(search_keyword,self.result['data']['user'][0]['username'])

    def test_search_user_no(self):
        u'''搜索用户：对应搜索关键字无结果'''
        search_keyword='坑卡坑卡'
        payload={'type':'user','page':'1','keyword':search_keyword}
        r=requests.post(url=self.url,data=payload)
        self.result=r.json()
        # print self.result
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['data'],None)
        

    def test_search_forum(self):
        u'''搜索帖子:对应搜索关键字有结果'''
        search_keyword='测试'
        payload={'type':'forum','page':'1','keyword':search_keyword}
        r=requests.post(url=self.url,data=payload)
        self.result=r.json()
        # print self.result
        self.assertEqual(self.result['status'],0)
        self.assertTrue(len(self.result['data']['thread'])>=1)
        print ("搜索第一页帖子个数：%s" %len(self.result['data']['thread']))
        self.assertIn(search_keyword,self.result['data']['thread'][0]['subject'])

    def test_search_forum_no(self):
        u'''搜索帖子：对应搜索关键字无结果'''
        search_keyword2='坑卡坑卡2'
        payload2={'type':'forum','page':'1','keyword':search_keyword2}
        time.sleep(10)
        r=requests.post(url=self.url,data=payload2)
        self.result=r.json()
        print self.result
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['data'],None)


    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
