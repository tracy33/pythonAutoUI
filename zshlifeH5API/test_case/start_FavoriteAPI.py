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


class FavoriteAPI(unittest.TestCase):
    '''收藏/取消 板块、帖子接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=favorite"
        self.favorite_forum='广州论坛'
        self.favorite_thread='深圳八大景之首—大鹏所城'
        self.favorite_id=130
        self.favorite_tid=2095430
        self.cookies=globalcookie.cookiestr


    def test_favoriteForum(self):
        u'''测试收藏、取消板块(重复请求则为取消)'''
        payload={
        'type':'forum',
        'id':self.favorite_id
        }
        headers={
        'cookie':self.cookies,
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json'
        }
        r=requests.get(url=self.url,params=payload,headers=headers)
        self.result=r.json()
        # j=json.dumps(self.result)
        # dict2=j.decode("unicode-escape")
        # print dict2
        self.assertEqual(self.result['status'],0)
        if self.result['data']['isFavorite']:
            self.assertIn(self.favorite_forum,json.dumps(self.result['data']['forumList'][0]).decode("unicode-escape"))
            print ("板块收藏成功")
        else:
            self.assertNotIn(self.favorite_forum,json.dumps(self.result['data']['forumList'][0]).decode("unicode-escape"))
            print ("板块取消收藏成功")

    def test_favoriteThread(self):
        u'''测试收藏、取消帖子(重复请求则为取消)'''
        payload={
        'type':'thread',
        'id':self.favorite_tid
        }
        headers={
        'cookie':self.cookies,
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json'
        }
        r=requests.get(url=self.url,params=payload,headers=headers,verify=False)
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        if self.result['data']['isFavorite']:
            print ("帖子收藏成功")
        else:
            print ("帖子取消收藏成功")


    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
