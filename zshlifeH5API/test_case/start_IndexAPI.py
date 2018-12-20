#coding=utf-8
import requests
import unittest
from selenium.common.exceptions import NoSuchElementException
import json

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")
from public import *


class ZshIndexAPI(unittest.TestCase):
    '''首页数据接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url_index="https://m.qqzsh.com/api/mobile/h5.php?mod=get_index"

    def test_index_hdp(self):
        u'''page参数为空或为1时返回幻灯片、最姐推荐、热帖列表等数据'''
        payload={'page':'1'}
        # r=requests.get(url=url_index,params=payload)
        r=requests.get(self.url_index)
        self.result=r.json()
        # print self.result
        self.assertEqual(self.result['status'],0)
        self.assertTrue(len(self.result['data']['slide'])>1)
        print ("幻灯片个数：%s\n" %len(self.result['data']['slide']))
        self.assertTrue(len(self.result['data']['zshRecommend'])>1)
        print ("最姐推荐列表帖子个数：%s\n" %len(self.result['data']['zshRecommend']))
        self.assertTrue(len(self.result['data']['hotList'])>1)
        print ("热帖列表帖子个数：%s\n" %len(self.result['data']['hotList']))
        self.assertTrue(len(self.result['data']['mall']['goods'])==3)
        print ("企鹅商城推荐列表商品个数：%s\n" %len(self.result['data']['mall']['goods']))        

    def test_index_HotTurnPage(self):
        u'''page 大于1 时仅返回热帖翻页数据'''
        payload={'page':'2'}
        r=requests.get(url=self.url_index,params=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        self.assertTrue(len(self.result['data']['hotList'])==20)
        # print ("热帖翻页第二页数据%s\n" %len(self.result['data']['hotList']))
        self.assertNotIn("slide",self.result)
        self.assertNotIn("zshRecommend",self.result)
        self.assertNotIn('mall":{"goods"',self.result)           

  

    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()