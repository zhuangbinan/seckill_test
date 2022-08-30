from selenium import webdriver
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import datetime
# import exceptions
# import numpy as np
import requests
import json

# import pandas as pd
# import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 导入 ActionChains 类
from selenium.webdriver import ActionChains
# 导入 Select 类
from selenium.webdriver.support.ui import Select

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

# 获取淘宝服务器时间
taobaoTime_url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
}

Note = open('1920Index.txt', mode='a', encoding='utf-8')

class MgrbJw():

    def iselementById(browser, id):
        """
        基本实现判断元素是否存在
        :param browser: 浏览器对象
        :param id: id
        :return: 是否存在
        """
        try:
            browser.find_element(By.ID, id)
            return True
        except:
            return False

    def iselementByXpath(browser, xpaths):
        """
        基本实现判断元素是否存在
        :param browser: 浏览器对象
        :param xpaths: xpaths表达式
        :return: 是否存在
        """
        try:
            browser.find_element(By.XPATH, xpaths)
            print('is a ele')
            return True
        except:
            print('not a ele')
            return False

    def iselementByClassName(browser, class_name):
        """
        基本实现判断元素是否存在
        :param browser: 浏览器对象
        :param class_name: class_name
        :return: 是否存在
        """
        try:
            browser.find_element(By.CLASS_NAME, class_name)
            return True
        except:
            return False

    def openChromeToTaobao(self):
        # 使用开发者模式
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        # 禁用 Blink 运行时的某些功能
        options.add_argument(" --disable-blink-features=AutomationControlled")

        # 创建 driver 之后将 window.navigator.webdriver 改成 undefined
        # driver = webdriver.Chrome(options=options)

        s = Service(r'C:\Program Files\Google\Chrome\Application\chromedriver')
        # s = Service(r'C:\Program Files (x86)\Google\Chrome\Application')
        # driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver')
        driver = webdriver.Chrome(options=options, service=s)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        })
        # 这个是各个年份的那个URL
        mgrb_jw_url = 'https://www.cnbksy.com/literature/literature/6b0c95bc3774bc22c9901ebedd276483'
        mgrb_jw_url2 = 'https://www.cnbksy.com/literature/literaturesearch/6b0c95bc3774bc22c9901ebedd276483'

        mgrb_jw_url3 = 'https://www.cnbksy.com/literature/entitysearch/a5ff87f95cb578859ffd2c4e218801ab'
        mgrb_jw_url4 = 'https://www.cnbksy.com/literature/entitysearch/ca08a32b2407a5ef95e7560d9b838381'

        driver.get(mgrb_jw_url3)
        time.sleep(5)
        if MgrbJw.iselementByClassName(driver, 'resultRow'):
            resultRow = driver.find_elements(By.CLASS_NAME, 'resultRow')
            print("开始了")
            for index, value in enumerate(resultRow):
                s = resultRow[index].text.replace('\n', '    ')
                spl = s.split("    ")
                # print('标题', spl[0])
                # print('作者', spl[1])
                # print('刊名', spl[2])
                line1 = '{}|{}|{}|{}'.format(spl[0], spl[1], spl[2], s[s.find("[") + 1:-1].strip())
                # print(line1)
                # print(Note.write(line1+'\n'))
            # print(s[-1])
        # 执行退出按钮JS 模拟在控制台 执行
        # 在js中，通过window.open打开新窗口
        # driver.execute_script("bksy.formPost('/logout')")

        fp = open("1920totalUrl.txt", 'r', encoding='utf-8')
        i = 0
        for line in fp:
            i = i + 1
            if i == 1:
                continue
            print(i, line)
            url_line = line.replace("\n", "")
            # 打开这个页面,准备解析HTML
            newWindowUrl = "window.open('" + url_line + "')"
            print(newWindowUrl)
            driver.execute_script(newWindowUrl)
            print(driver.window_handles)
            time.sleep(1)  # 打开新网页以后会停留在新页面上
            # 打开所有页面后再进行操作
        time.sleep(2)
        # 开始处理
        # 0 到 最大值 , 递进1
        for num in range(0, 6, 1):
            driver.switch_to.window(driver.window_handles[num])
            time.sleep(2)
            if MgrbJw.iselementByClassName(driver, 'resultRow'):
                resultRow = driver.find_elements(By.CLASS_NAME, 'resultRow')
                for index, value in enumerate(resultRow):
                    s = resultRow[index].text.replace('\n', '    ')
                    spl = s.split("    ")
                    line = '{}|{}|{}|{}'.format(spl[0], spl[1], spl[2], s[s.find("[") + 1:-1].strip())
                    print(line)
                    Note.write(line+"\n")
        time.sleep(5)
        # Note.flush()
        Note.close()
        return None


a = MgrbJw()
a.openChromeToTaobao()
