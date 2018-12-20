#coding=utf-8
import requests
import unittest
from selenium.common.exceptions import NoSuchElementException
import json
import types 

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")


class ThreadDetailAPI(unittest.TestCase):
    '''帖子详情页接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=get_thread"



    def test_NormalThread(self):
        u'''常规帖子详情第一页'''
        payload={
        'tid':2095430,
        'page':None,
        'onlyAuthor':None,
        'assign':None,
        'activityList':None
        }
        r=requests.get(url=self.url,params=payload)
        # print json.dumps(r.json()).decode("unicode-escape")
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        #每日热帖推荐
        self.assertTrue(len(self.result['data']['hotRecommend'])>1)
        print ("每日热帖推荐数：%s" %len(self.result['data']['hotRecommend'])) 
        #广告位
        self.assertEqual(requests.get(self.result['data']['adv']['url']).status_code,200)
        #导航验证
        len_n=len(self.result['data']['navigation'])
        self.assertTrue(len_n>=1)
        navi_url='';
        for index,n in enumerate(self.result['data']['navigation']):
            if index<len_n-1:
                navi_url=navi_url+n['name']+">"
            else:
                navi_url=navi_url+n['name']
        print ("面包屑导航路径：%s" %navi_url)
        #帖子详情与图片
        Thread_content=self.result['data']['thread']['message'][0]['content']
        # print Thread_content
        self.assertTrue(len(Thread_content)>=1)
        imgurls=[]
        imgurls_thumb=[]
        for c in Thread_content:
            # print type(c)
            if type(c)==unicode:
                print ("纯字符串的不提取图片地址")
            else:
                if c['type']=='image':
                    imgurls.append(c['content'])
                    imgurls_thumb.append(c['thumb'])
        print ("帖子详情页面图片总数：%s" %len(imgurls_thumb))
        #检验缩略图
        for img_t in imgurls_thumb:
            self.assertEqual(requests.get(img_t).status_code,200)
        #检验原图
        for img in imgurls:
            self.assertEqual(requests.get(img).status_code,200)
        #验证回复数与头像
        print ("回复列表总数：%s" %len(self.result['data']['replys']))
        for r in self.result['data']['replys']:
            self.assertEqual(requests.get(r['avatar']).status_code,200)
        #验证帖子详情页楼主自己的头像
        self.assertEqual(requests.get(self.result['data']['thread']['avatar']).status_code,200)

    def test_ThreadOnlyAuthor(self):
        u'''帖子详情只看楼主'''
        payload={
        'tid':2086823,
        'page':None,
        'onlyAuthor':'1',
        'assign':None,
        'activityList':None
        }
        r=requests.get(url=self.url,params=payload)
        # print json.dumps(r.json()).decode("unicode-escape")
        self.result=r.json()
        self.assertEqual(self.result['status'],0)
        author=self.result['data']['thread']['author']
        authorid=self.result['data']['thread']['authorid']
        for r in self.result['data']['replys']:
            self.assertEqual(r['author'],author)
            self.assertEqual(r['authorid'],authorid)



    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()