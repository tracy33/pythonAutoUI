#coding=utf-8
import requests
import unittest
from selenium.common.exceptions import NoSuchElementException
import json

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")

class GetForum(unittest.TestCase):
    '''板块帖子获取接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=get_forum"
        self.fid='201'
        self.fidname='广州美食'

    def test_summaryThread(self):
        u'''默认获取全部的帖子（即h5端tab'最新')和板块列表'''
        r=requests.get(self.url)
        self.result=r.json()
        # print self.result
        self.assertEqual(self.result['status'],0)
        print ("默认最新-帖子列表个数：%s" %len(self.result['data']['thread']))
        #self.assertTrue(len(self.result['data']['forumList'])==8)
        print ("板块分类个数：%s" %len(self.result['data']['forumList']))
        # j=json.dumps(self.result)
        # dict2=j.decode("unicode-escape")
        # print dict2
        for f in self.result['data']['forumList']:
            print("板块分类 '%s' 下面的板块数 %s" %(f["sname"],len(f["sub"])))

    def test_summaryThread_Digest(self):
        u'''获取聚合推荐列表的精华帖子''' #相当于h5端的“精华”
        payload={'view':'digest'}
        r=requests.post(url=self.url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        print ("默认精华-帖子列表个数：%s" %len(self.result['data']['thread']))
        for t in self.result['data']['thread']:
            self.assertTrue(t["digest"])

    def test_summaryThread_Hot(self):
        u'''获取聚合推荐列表的最热帖子'''  #相当于h5端的“全部”
        payload={'view':'hot'}
        r=requests.post(url=self.url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        print ("默认全部-帖子列表个数：%s" %len(self.result['data']['thread']))
        # j=json.dumps(self.result)
        # dict2=j.decode("unicode-escape")
        # print dict2
        # for t in self.result['data']['thread']:
        #     self.assertTrue(t["heats"])

    def test_fidThread_Digest(self):
        u'''广州美食版精华帖子'''
        payload={'fid':self.fid,'view':'digest'}
        r=requests.post(url=self.url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        print ("'%s'精华-帖子列表个数：%s" %(self.fidname,len(self.result['data']['thread'])))
        for t in self.result['data']['thread']:
            self.assertTrue(t["digest"])
            self.assertEqual(t["fid"],self.fid)

    def test_fidThread_Newthread(self):
        u'''广州美食版最新帖子'''
        payload={'fid':self.fid,'view':'newthread'}
        r=requests.post(url=self.url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        print ("'%s'最新-帖子列表个数：%s" %(self.fidname,len(self.result['data']['thread'])))
        for index,t in enumerate(self.result['data']['thread']):
            self.assertEqual(t["fid"],self.fid)
            # self.assertGreater(self.result['data']['thread'][index+1]['dateline'],t['dateline'])

    def test_fidThread_Hot(self):
        u'''广州美食版热帖'''
        payload={'fid':self.fid,'view':'hot'}
        r=requests.post(url=self.url,data=payload)
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        print ("'%s'全部-帖子列表个数：%s" %(self.fidname,len(self.result['data']['thread'])))
        # j=json.dumps(self.result)
        # dict2=j.decode("unicode-escape")
        # print dict2
        for t in self.result['data']['thread']:
            # self.assertTrue(t["heats"])
            self.assertEqual(t["fid"],self.fid)


    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
