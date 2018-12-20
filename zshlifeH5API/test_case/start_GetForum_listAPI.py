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

class GetForumList(unittest.TestCase):
    '''版块列表获取接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=get_forum_list"
        self.cookies=globalcookie.cookiestr


    def test_getForum_list_unlogin(self):
        u'''未登录状态获取板块列表'''
        r=requests.get(self.url)
        self.result=r.json()
        j=json.dumps(self.result)
        dict2=j.decode("unicode-escape")
        # print dict2
        self.assertEqual(self.result['status'],10004)
        self.assertEqual(self.result['msg'],'请先登录')

    def test_getForum_list_login(self):
        u'''已登录状态获取板块列表'''
        headers={'cookie':self.cookies}
        r=requests.get(self.url,headers=headers)
        self.result=r.json()
        # j=json.dumps(self.result)
        # dict2=j.decode("unicode-escape")
        # print dict2
        self.assertEqual(self.result['status'],0)
        print ("所有板块个数：%s" %len(self.result['data']['forumList']))
        for f in self.result['data']['forumList']:
            print ("【%s】下面的主题分类个数：%s" %(f['fname'],len(f['types'])))
        #判断收藏板块‘亲子乐园’
        print ("账户收藏板块个数：%s" %len(self.result['data']['followForum']))
        fo=json.dumps(self.result['data']['followForum'])
        fo2=fo.decode("unicode-escape")
        self.assertIn('亲子乐园',fo2)


    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
