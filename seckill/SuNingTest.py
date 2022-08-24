from selenium import webdriver
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import datetime
# import exceptions
# import numpy as np
import requests
import json
import time
import datetime
# import pandas as pd
# import os
from selenium.webdriver.chrome.service import Service


# suning_server_time = 'http://quan.suning.com/getSysTime.do'
suning_server_time = 'https://f.m.suning.com/api/ct.do'

# total_query_time_limit = 60000000
total_query_time_limit = 100
dataline_url = 'https://product.suning.com/0000000000/10115412380.html?f=t&src=ssdln_336521_recsszggmn_1-1_p_0000000000_10115412380_rec_2-1_0_A&safp=d488778a.46602.recGoodsBoxClearfix.1&safc=prd.1.rec_2-1_0_A&safpn=10006.336521'
paper_url = 'https://product.suning.com/0000000000/12184442094.html?safp=d488778a.40134.Jyd6.6&safc=prd.0.0&safpn=10009'
login_url = 'https://passport.suning.com/ids/login?method=GET&loginTheme=b2c'

class suning():

    def iselementByXpath(browser, xpaths):
        """
        基本实现判断元素是否存在
        :param browser: 浏览器对象
        :param xpaths: xpaths表达式
        :return: 是否存在
        """
        try:
            browser.find_element(By.XPATH, xpaths)
            return True
        except:
            return False

    def iselementById(browser, id):
        """
        基本实现判断元素是否存在
        :param browser: 浏览器对象
        :param xpaths: xpaths表达式
        :return: 是否存在
        """
        try:
            browser.find_element(By.ID, id)
            return True
        except:
            return False

    def openChromeToTaobao(self):
        s = Service(r'C:\Program Files\Google\Chrome\Application\chromedriver')
        driver = webdriver.Chrome(service=s)
        driver.get(login_url)
        print('请扫码登录')
        time.sleep(5)
        print('5s结束')
        while 1 == 1:
            print('进入循环,判断有没有搜索框来判断是否登录了')
            # isLogin = suning.iselement(driver, '/html/body/div[2]/div/div/div[2]/div/div[1]/form/div[3]/input')
            isLogin = suning.iselementById(driver, 'searchKeywords')

            if isLogin:
                print('已经登录了')
                driver.get(paper_url)
                # 判断购买时间

                if suning.iselementById(driver, 'buyNowAddCart'):
                    driver.find_element(By.ID, 'buyNowAddCart').click()
                    print("点了购买")
                    while 1 == 1:
                        print("进入提交订单页面")
                        if suning.iselementById(driver, 'submit-btn'):
                            print('点击提交订单按钮')
                            driver.find_element(By.ID, 'submit-btn').click()
                            print('已经点提交了')
                            time.sleep(3600)
                            if suning.iselementByXpath(driver, '/html/body/div[6]/div[1]/div[2]/div[1]/a[2]'):
                                print('break')
                                break
                            else:
                                print('return None')
                                return None
                        else:
                            continue

                    # time.sleep(0.5)

            if (total_query_time_limit - 1) == 1:
                print(total_query_time_limit)
                break


a = suning()
a.openChromeToTaobao()
# res = requests.get(url=suning_server_time)
# timestamp = json.loads(res.content)['currentTime']
# print(timestamp)
# total_query_time_limit = total_query_time_limit - 1
# time.sleep(0.1)
# //时间到了触发


# 先试试css选择器
#     if driver.find_element(By.ID, 'buyNowAddCart'):
#     print("is a ele")
#     buyNowAddCart = driver.find_element(By.ID, 'buyNowAddCart').click()
#     print("点了购买")

# while total_query_time_limit != 1:
#     res = requests.get(url=suning_server_time)
#     timestamp = json.loads(res.content)['currentTime']
#     print(timestamp)
#     total_query_time_limit = total_query_time_limit - 1
#     # time.sleep(0.1)
#     # //时间到了触发
#     s = Service(r'C:\Program Files\Google\Chrome\Application\chromedriver')
#     driver = webdriver.Chrome(service=s)
#     driver.get(dataline_url)
#     # print('请扫码登录')
#     # 先试试css选择器
#     if driver.find_element(By.ID, 'buyNowAddCart'):
#         print("is a ele")