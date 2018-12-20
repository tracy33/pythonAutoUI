#coding=utf-8
import requests
import unittest
from selenium.common.exceptions import NoSuchElementException
import json

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


sys.path.append(".\\public")
import globalcookie

class Get_myAPI(unittest.TestCase):
    '''我的信息获取接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=get_my"
        self.cookies=globalcookie.cookiestr

    def test_get_my_me(self):
        u'''uid为0获取当前登录用户信息'''
        payload={
        'uid':0
        }
        headers={
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json',
        'Cookie':self.cookies
        }
        r=requests.get(url=self.url,params=payload,headers=headers,verify=False)
        self.result=r.json()
        j=json.dumps(self.result)
        dict2=j.decode("unicode-escape")
        print dict2        
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['data']['me'],1)

    def test_get_my_other(self):
        u'''uid指定时获取其他人的信息'''
        other_uid=10454768#10382440
        payload={
        'uid':other_uid
        }
        headers={
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json',
        'Cookie':self.cookies
        }
        r=requests.get(url=self.url,params=payload,headers=headers,verify=False)
        self.result=r.json()
        # j=json.dumps(self.result)
        # dict2=j.decode("unicode-escape")
        # print dict2        
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['data']['me'],0)
        self.assertEqual(self.result['data']['uid'],other_uid)


    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
