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

class ReplyAPI(unittest.TestCase):
    '''回帖接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=reply"
        self.cookies=globalcookie.cookiestr
        #获取帖子id
        self.tidurl="https://m.qqzsh.com/api/mobile/h5.php?mod=get_forum"
        self.data={
        'fid':65,
        'view':'all',
        'page':1
        }
        self.headers={
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json',
        'Cookie':self.cookies
        }
        self.r=requests.get(url=self.tidurl,params=self.data,headers=self.headers)
        self.resu=self.r.json()
        self.tid=self.resu['data']['thread'][0]['tid']





    def test_reply_login(self):
        u'''已登录状态回帖'''
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
        'message[0][content]':"自动化回帖测试内容",
        'message[1][type]':'image',
        'message[1][content]':aid,
        'tid':self.tid
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
        self.assertEqual(self.result['msg'],'非常感谢，回复发布成功')

    def test_reply_unlogin(self):
        u'''未登录状态回帖'''
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
        'message[0][content]':"自动化回帖测试内容",
        'tid':self.tid
        }
        headers={
        'Content-Type':'application/X-WWW-FORM-URLENCODED',
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Accept':'application/json'
        }
        r=requests.post(url=self.url,data=payload,headers=headers)
        self.result=r.json()
        self.assertEqual(self.result['status'],10004)
        self.assertEqual(self.result['msg'],'请先登录')


    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
