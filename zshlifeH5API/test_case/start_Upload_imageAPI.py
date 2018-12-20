#coding=utf-8
import requests
import unittest,os
from selenium.common.exceptions import NoSuchElementException
import json

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sys.path.append(".\\public")
import globalcookie,Img_uploadAPI


class upload_imageAPI(unittest.TestCase):
    '''图片上传接口'''
    def setUp(self):
        self.verificationsErrors=[]
        self.accept_next_alert=True
        self.url="https://m.qqzsh.com/api/mobile/h5.php?mod=upload_image"
        self.cookies=globalcookie.cookiestr
        self.picname='testpic.JPG' #带上图片名称与后缀


    def test_imgupload_login(self):
        u'''已登录状态上传图片'''
        self.result=Img_uploadAPI.Img_upoad(self.url,self.picname,self.cookies)
        
        # j=json.dumps(self.result)
        # dict2=j.decode("unicode-escape")
        # print dict2
        self.assertEqual(self.result['status'],0)
        self.assertIn('gdtnio.com',self.result['data']['url'])


    def test_imgupload_unlogin(self):
        u'''未登录状态上传图片'''
        self.result=Img_uploadAPI.Img_upoad(self.url,self.picname,'')
        self.assertEqual(self.result['status'],10004)
        self.assertIn('请先登录',self.result['msg'])

    def test_imgupload_fail(self):
        u'''上传失败，文件不能为空'''
        self.result=Img_uploadAPI.Img_upoad(self.url,'',self.cookies)      
        self.assertEqual(self.result['status'],1)
        self.assertIn('文件不能为空',self.result['msg'])        

    def tearDown(self):
        self.assertEqual([],self.verificationsErrors)


if __name__ == '__main__':
    unittest.main()
