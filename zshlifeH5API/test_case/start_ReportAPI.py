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



class ReportAPI(unittest.TestCase):
    '''举报接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=report"
        self.forum_id=65
        self.thread_id=2113116
        self.post_id=25235969
        self.uid=10325961
        self.pic=5430248
        self.cookies=globalcookie.cookiestr


    def test_ReportThread(self):
        u'''举报帖子'''
        payload={
        'report_select':'广告垃圾',
        'rtype':'thread',
        'rid':self.thread_id,
        'fid':self.forum_id
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
        self.assertIn('举报成功',self.result['msg'])
        print('举报帖子成功')

    def test_unloginReportThread(self):
        u'''未登录进行举报'''
        payload={
        'report_select':'违规内容',
        'rtype':'thread',
        'rid':2113116,
        'fid':65
        }
        headers={
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json'
        }
        r=requests.get(url=self.url,params=payload,headers=headers)
        self.result=r.json()
        self.assertEqual(self.result['status'],10004)
        self.assertEqual(self.result['msg'],'请先登录')

    def test_ReportPost(self):
        u'''举报回帖'''
        payload={
        'report_select':'广告垃圾',
        'rtype':'post',
        'rid':self.post_id,
        'fid':self.forum_id
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
        self.assertEqual(self.result['status'],0)
        self.assertIn('举报成功',self.result['msg'])
        print('举报回帖成功')

    def test_ReportUser(self):
        u'''举报用户'''
        payload={
        'report_select':'恶意灌水',
        'rtype':'user',
        'rid':self.uid,
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
        self.assertEqual(self.result['status'],0)
        self.assertIn('举报成功',self.result['msg'])
        print('举报用户成功')

    def test_ReportPic(self):
        u'''举报图片'''
        payload={
        'report_select':'其他',
        'message':'外图',
        'rtype':'pic',
        'rid':self.pic,
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
        self.assertEqual(self.result['status'],0)
        self.assertIn('举报成功',self.result['msg'])
        print('举报图片成功')



    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
