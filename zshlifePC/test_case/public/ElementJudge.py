#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

#判断元素是否存在

# def ElementExist(self,element,bywhat):
#     u'''判断元素是否存在'''
#     flag=True
#     driver=self.driver
#     try:
#         if bywhat=='by_name':
#             driver.find_element_by_name(element)
#         elif bywhat=='by_class'
#             driver.find_element_by_class_name(element)
#         elif bywhat=='by_css':
#             driver.find_element_by_css_selector(element)
#         elif bywhat=='by_xpath':
#             driver.find_element_by_xpath(element)
#         elif bywhat=='by_link':
#             driver.find_element_by_link_text(element)
#         else:
#             driver.find_element_by_id(element)
#     except:
#         flag=False
#     return flag


def is_element_visible(self, element):
    u'''判断元素是否可见'''
    driver=self.driver
    try:
        the_element = EC.visibility_of_element_located(element)
        assert the_element(driver)
        flag = True

    except:
        flag=False
    return flag

def is_element_visible_dr(driver, element):
    u'''判断元素是否可见'''
    driver=driver
    try:
        the_element = EC.visibility_of_element_located(element)
        assert the_element(driver)
        flag = True

    except:
        flag=False
    return flag
