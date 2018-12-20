#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest,time
import requests
import ElementJudge
from selenium.webdriver.common.by import By


#登录模块函数
def login(un,pw,driver):
    u'''gdtmpd登录'''
    # driver=webdriver.Chrome()
    driver=driver
    startTime = time.time()
    print "页面加载start time is: %0.3f"%startTime
    driver.set_page_load_timeout(60)
    try:
        driver.get('https://gz.qqzsh.com/forum.php')#首页加载太慢，换成论坛页进行登录
    except:
        print 'time out after 60 seconds when loading page'
        driver.execute_script('window.stop()') #当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作

    nowhandle=driver.current_window_handle
    print "nowhandle:%s"%nowhandle
    # driver.implicitly_wait(30)
    # time.sleep(5)
    # driver.find_element_by_link_text(u'QQ').click()
    driver.find_element_by_class_name("self-info").find_element_by_link_text('QQ').click()
    #driver.find_element_by_css_selector("a[href='syncLogin.php?mod=login&login_type=qq&action=login']").click()
    time.sleep(3)
    driver.switch_to_frame("ptlogin_iframe") #frame里面写frame的id值
    time.sleep(5)
    driver.find_element_by_id("switcher_plogin").click()
    time.sleep(2)
    driver.find_element_by_id("u").clear()
    driver.find_element_by_id("u").send_keys(un)
    driver.find_element_by_id("p").clear()
    driver.find_element_by_id("p").send_keys(pw)
    time.sleep(3)
    driver.find_element_by_id("login_button").click()    
    time.sleep(5)
    usr=""
    try:
        usr=driver.find_element_by_id('username-top')
    except:
        startTime2 = time.time()
        print "页面加载start time is: %0.3f"%startTime
        driver.set_page_load_timeout(60)
        try:
            driver.get("https://gz.qqzsh.com/forum.php")
        except:
            print 'time out after 60 seconds when loading page'
            driver.execute_script('window.stop()') #当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作
        usr=driver.find_element_by_id('username-top')

    the_element=ElementJudge.is_element_visible_dr(driver,(By.ID,'username-top'))
        # print usr
    if the_element:
        print (u"登录成功,登录用户昵称是：%s" %usr.text)
        cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()] 
        # print cookie
        cookiestr = ';'.join(item for item in cookie)
        # cookiestr=driver.get_cookies()
        # print cookiestr
        return cookiestr
    else:
        print u"登录失败"
        driver.get_screenshot_as_file("../../screenshot/login_erro.png")
    time.sleep(3)
    # driver.quit()
    
