#coding=utf-8
import requests
import unittest
from selenium.common.exceptions import NoSuchElementException
import json

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class Get_activityAPI(unittest.TestCase):
    '''活动列表接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=get_activity"

    def test_get_activity(self):
        u'''从接口获取活动列表'''
        payload={
        'page':1
        }
        headers={
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json'
        }
        r=requests.post(url=self.url,data=payload,headers=headers)
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        self.assertEqual(len(self.result['data']['list']),20)
        self.assertEqual(len(self.result['data']['slide']),5)
        self.assertEqual(len(self.result['data']['zshRecommend']),5)        



    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()