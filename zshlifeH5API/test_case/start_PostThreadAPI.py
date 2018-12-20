#coding=utf-8
import requests
import unittest
from selenium.common.exceptions import NoSuchElementException
import json

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")
import globalcookie,Img_uploadAPI

class PostThreadAPI(unittest.TestCase):
    '''发帖接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=post"
        self.cookies=globalcookie.cookiestr
        self.subject="H5发帖接口测试发帖"


    def test_post_login(self):
        u'''已登录状态发帖'''
        #上传图片获取aid的值
        aid=""
        imgup_url='https://m.qqzsh.com/api/mobile/h5.php?mod=upload_image'
        picname='testpic.JPG'
        result=Img_uploadAPI.Img_upoad(imgup_url,picname,self.cookies)
        if result['status']==0:
            aid=result['data']['aid']
        else:
            print u"图片上传失败"
            print result
        payload={
        'message[0][type]':'text',
        'message[0][content]':self.subject+"帖子内容测试",
        'message[1][type]':'image',
        'message[1][content]':aid,
        'fid':65,
        'subject':self.subject,
        'phone':''
        }
        headers={
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json',
        'Cookie':self.cookies
        }
        r=requests.post(url=self.url,data=payload,headers=headers)
        self.result=r.json()
        # j=json.dumps(self.result)
        # dict2=j.decode("unicode-escape")
        # print dict2
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['msg'],'非常感谢，您的主题已发布')

    def test_post_unlogin(self):
        u'''未登录状态发帖'''
        #上传图片获取aid的值
        aid=""
        payload={
        'message[0][type]':'text',
        'message[0][content]':self.subject+"帖子内容测试",
        'message[1][type]':'image',
        'message[1][content]':aid,
        'fid':65,
        'subject':self.subject,
        'phone':''
        }
        headers={
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json',
        }
        r=requests.post(url=self.url,data=payload,headers=headers)
        self.result=r.json()
        # j=json.dumps(self.result)
        # dict2=j.decode("unicode-escape")
        # print dict2
        self.assertEqual(self.result['status'],10004)
        self.assertEqual(self.result['msg'],'请先登录')

    # def test_post_audit(self):
    #     u'''发帖待审核'''
    #     payload={
    #     'message[0][type]':'text',
    #     'message[0][content]':'test习近平啊',
    #     'fid':65,
    #     'subject':self.subject,
    #     'phone':''
    #     }
    #     headers={
    #     'Content-Type':'application/X-WWW-FORM-URLENCODED',
    #     'X-Requested-With':'XMLHttpRequest',
    #     'Accept-Language':'zh-cn',
    #     'Accept':'application/json',
    #     'Cookie':self.cookies
    #     }
    #     r=requests.post(url=self.url,data=payload,headers=headers)
    #     self.result=r.json()
    #     self.assertEqual(self.result['status'],0)
    #     self.assertEqual(self.result['msg'],'新主题需要审核，您的帖子通过审核后才能显示')

    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
