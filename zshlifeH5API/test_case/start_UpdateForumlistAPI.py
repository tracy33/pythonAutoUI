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


class UpdateForumlistOrder(unittest.TestCase):
    '''更新关注版块排序接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=set_forum_list_order"
        self.cookies=globalcookie.cookiestr


    def test_updatelist_unlogin(self):
        u'''未登录状态更新关注版块排序'''
        payload={
        'forumList[0][fid]':68,
        'forumList[1][fid]':74,
        'forumList[2][fid]':65
        }
        headers={
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
        self.assertEqual(self.result['status'],10004)
        self.assertEqual(self.result['msg'],'请先登录')

    def test_updatelist_login(self):
        u'''已登录状态更新关注版块排序'''
        #先获取已收藏的板块
        headers={'cookie':self.cookies,
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json'        
        }
        payload={}
        r0=requests.get(url='https://m.qqzsh.com/api/mobile/h5.php?mod=get_forum_list',headers=headers)
        re0=r0.json()
        for index,fol in enumerate(re0['data']['followForum']):
            key='forumList['+str(index)+'][fid]'
            value=fol['fid']
            payload.setdefault(key,value)
        # sorted(payload.iteritems(),key=lambda asd:asd[0],reverse=False) #等于字典进行升序排序，按照key升序
        # payload={'forumList[0][fid]':68,'forumList[1][fid]':74} #这样传参后 74排在68前面
        print re0['data']['followForum']
        r=requests.post(url=self.url,headers=headers,data=payload)
        print json.dumps(r.json()).decode("unicode-escape")
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['msg'],'更新成功')

    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
