#coding=utf-8
import requests
import unittest,os
from selenium.common.exceptions import NoSuchElementException
import json

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


def Img_upoad(url,picname,cookies):
    url=url
    picname=picname
    cookies=cookies
    headers={
        #'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryCl3tslK1Le3fzjbX',#去掉这句就成功了，不然老提示文件不能为空
        'X-Requested-With':'XMLHttpRequest',
        'Accept-Language':'zh-cn',
        'Cookie':cookies
        }
    if picname=='':
        file=''
    else:
        #当前文件的路径
        pwd=os.getcwd()
        #picdir=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"."+os.path.sep+"data") #被调用的话不需要两个..
        #有all_tests统一执行就不需要父路径了，如下
        picdir=os.path.abspath(pwd+os.path.sep+"data")
        picpath=os.path.join(picdir,picname)
        file={'file':(picname,open(picpath,'rb'),'image/jpeg')}
        # print file
        
    r=requests.post(url=url,files=file,headers=headers)
    result=r.json()
    print result
    return result
