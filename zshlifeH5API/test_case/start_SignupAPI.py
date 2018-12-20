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


class SignUpAPI(unittest.TestCase):
    '''每日签到接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=sign"
        self.cookies=globalcookie.cookiestr

    def test_unlogin_signup(self):
        u'''未登录时签到'''
        r=requests.get(self.url)
        self.result=r.json()
        print self.result
        self.assertEqual(self.result['status'],10004)
        self.assertEqual(self.result['msg'],u'请先登录')

    def test_login_signup(self):
        u'''已登录时签到'''
        headers={'cookie':self.cookies}
        r=requests.get(url=self.url,headers=headers)
        res=r.json()
        print res
        if res['status']==2:
            self.assertEqual(res['status'],2)
            self.assertEqual(res['msg'],'您已经签过到啦，请下期再来！')
        else:
            self.assertEqual(res['status'],0)
            self.assertEqual(res['msg'],'签到成功!')
        
        

    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()