from selenium import webdriver
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import datetime
# import exceptions
# import numpy as np
import requests

# import pandas as pd
# import os
from selenium.webdriver.chrome.service import Service

# 获取淘宝服务器时间
taobaoTime_url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
}
# 获取今天预备抢购的日期
now_time = datetime.datetime.now().strftime('%Y-%m-%d')
# times=now_time+' 19:59:59.000000'
# times=now_time+' 13:50:00.000000'
# time_stamp = 1660651200000
# 2022-08-23 19:59:57 时间戳如下
sale_time_stamp = 1661255997000

class taobao():

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

    def iselement(browser, xpaths):
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

    def openChromeToTaobao(self):
        # driver = webdriver.Chrome(executable_path='/Users/lvdouxianbaozi/Downloads/chromeDownload/chromedriver')
        s = Service(r'C:\Program Files\Google\Chrome\Application\chromedriver')
        # s = Service(r'C:\Program Files (x86)\Google\Chrome\Application')
        # driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver')
        driver = webdriver.Chrome(service=s)
        taobaoUrl = 'https://login.taobao.com/member/login.jhtml?f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F%3Fspm%3Da1z0d.6639537%2Ftb.1581860521.1.24317484mFBzxx'
        driver.get(taobaoUrl)
        # 在输入框输入内容
        # 但是淘宝整了个滑动解锁的操作,所以不输入账号密码登陆了,改为扫码登录
        # driver.find_element_by_id('fm-login-id').send_keys("17614866848")
        # driver.find_element_by_id('fm-login-password').send_keys("*****")
        # time.sleep(2)  # giving time to json get in the data
        print('请扫码登录')
        print('Clicking to extend table...')
        driver.find_element(By.XPATH, '//i[@class="iconfont icon-qrcode"]').click()
        # 给我5s扫码登录的时间
        # Getting HTML
        print('这里扫码开始等待点击')
        time.sleep(6)
        while 1==1:
            isLogin = taobao.iselement(driver, '/html/body/div[2]/div/div/div[2]/div/div[1]/form/div[3]/input')
            if isLogin:
                driver.get('https://cart.taobao.com/cart.htm?')
                # 勾选
                # 这里的参数需要修改,勾选的商品!
                # time.sleep(200000)
                driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div').click()
                print('正在等待秒杀时间')
                while 1==1:
                    # 本地时间
                    # now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    # 淘宝服务器时间
                    taobaoTime = requests.get(url=taobaoTime_url, headers=headers).json()['data']['t']
                    # tTime= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(taobaoTime) / 1000))
                    # 结算  现在按照淘宝时间看了
                    # if tTime >times:
                    # print(int(taobaoTime))
                    # print(sale_time_stamp)
                    if int(taobaoTime) >= sale_time_stamp:
                        if taobao.iselementById(driver,'J_Go'):
                            # 点击结算按钮
                            # driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div[4]/div[2]/div[3]/div[5]').click()
                            driver.find_element(By.ID,'J_Go').click()
                            print("点击结算")
                            while 1==1:
                                ss = taobao.iselement(driver, '//*[@id="submitOrderPC_1"]/div/a[2]')
                                if ss:
                                    # 点击提交按钮
                                    driver.find_element(By.XPATH, '//*[@id="submitOrderPC_1"]/div/a[2]').click()
                                    print('点击提交: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                                    return None
                    else:
                        time.sleep(0.05)
        time.sleep(1000000000)



a = taobao()
a.openChromeToTaobao()
