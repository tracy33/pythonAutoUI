#coding=utf-8
import requests
import unittest
from selenium.common.exceptions import NoSuchElementException
import json

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")
#import globalcookie


class GetCommentAPI(unittest.TestCase):
    '''获取点评详细页列表数据接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=get_comment"
        self.tid=2117097
        self.pid=25374952
        # self.cookies=globalcookie.cookiestr


    def test_loginGetComment(self):
        u'''获取点评'''
        payload={
        'tid':self.tid,
        'pid':self.pid,
        'page':1
        }

        headers={
        # 'cookie':self.cookies,
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json'
        }
        r=requests.post(url=self.url,data=payload,headers=headers)
        self.result=r.json()
        # j=json.dumps(self.result)
        # dict2=j.decode("unicode-escape")
        # print dict2
        self.assertEqual(self.result['status'],0)
        # print self.result['data']['replys']
        self.assertEqual(self.result['data']['replys'][0]['pid'],str(self.pid))
        print "点评长度：%s" %len(self.result['data']['replys'][0]['comments'])



    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
