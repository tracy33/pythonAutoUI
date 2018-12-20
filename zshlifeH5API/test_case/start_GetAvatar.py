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


class GetAvatarAPI(unittest.TestCase):
    '''我的头像获取接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=get_my_avatar"
        self.cookies=globalcookie.cookiestr

    def test_unlogin_getAvatar(self):
        u'''未登录状态获取默认头像'''
        r=requests.get(self.url)
        url_name=r.url.split('/')[-1].split('.')[0]
        self.assertEqual(200,r.status_code)
        self.assertEqual('00_avatar_small',url_name)

    def test_login_getAvatar(self):
        u'''登录状态获取用户帐号头像'''
        headers={'cookie':self.cookies}
        r=requests.get(url=self.url,headers=headers)
        url_name=r.url.split('/')[-1].split('.')[0]
        self.assertEqual(200,r.status_code)
        self.assertEqual('50_avatar_small',url_name)
        


    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()