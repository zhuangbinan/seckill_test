import requests
from selenium import webdriver

from selenium.webdriver.common.by import By
import time
import json

from selenium.webdriver.chrome.service import Service

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
}



class LotteryAssist:

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

    def openChromeToBilibili(self):
        # 使用开发者模式
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        # 禁用 Blink 运行时的某些功能
        options.add_argument(" --disable-blink-features=AutomationControlled")

        # 创建 driver 之后将 window.navigator.webdriver 改成 undefined
        # driver = webdriver.Chrome(options=options)

        s = Service(r'C:\Program Files\Google\Chrome\Application\chromedriver')
        driver = webdriver.Chrome(options=options, service=s)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        })

        # uid
        uid = None
        bilibiliUrl = 'https://www.bilibili.com'
        # 喵喵折APP 有个抽完的
        # 科技美学 有还没抽完的
        driver.get(bilibiliUrl)
        time.sleep(3)


        if LotteryAssist.iselementByClassName(driver, 'header-login-entry'):
            print('点击登录按钮', flush=True)
            driver.find_element(By.CLASS_NAME, 'header-login-entry').click()
            while (1 == 1):
                if LotteryAssist.iselementByClassName(driver, 'header-avatar-wrap'):
                    print("已经登录")
                    break
                else:
                    print("没登录")
                time.sleep(5)

            time.sleep(3)
            # print("假如登录了")

            if LotteryAssist.iselementByClassName(driver, 'nav-search-input'):
                print("找到搜索框")
                search_input = driver.find_element(By.CLASS_NAME, 'nav-search-input')
                search_input.send_keys('科技美学')
                if LotteryAssist.iselementByClassName(driver, 'nav-search-btn'):
                    print("点击搜索按钮")
                    search_btn = driver.find_element(By.CLASS_NAME, 'nav-search-btn')
                    search_btn.click()
                    types = driver.find_elements(By.CLASS_NAME, 'vui_tabs--nav-text')
                    print(types)
                    time.sleep(3)

                    print("准备XPATH")
                    # 应该要在新的窗口搜索
                    driver.switch_to.window(driver.window_handles[1])
                    if LotteryAssist.iselementByXpath(driver, '//*[@id="i_cecream"]/div/div[2]/div[1]/div[2]/div/nav/ul/li[8]/span/span[1]'):
                        type_user = driver.find_element(By.XPATH, '//*[@id="i_cecream"]/div/div[2]/div[1]/div[2]/div/nav/ul/li[8]/span/span[1]')
                        print('用户那一栏分类')
                        time.sleep(3)
                        print(type_user.text)
                        if type_user.text == '用户':
                            print('是用户的span')
                            print(driver.current_url)
                            # https://search.bilibili.com/all?keyword
                            # &order=fans

                            current_url = driver.current_url
                            pre_url = 'https://search.bilibili.com/upuser?keyword'
                            end_url = '&order=fans'
                            final_url = current_url.replace('https://search.bilibili.com/all?keyword', pre_url) + end_url

                            # type_user.click()
                            print(final_url)
                            driver.get(final_url)
                            time.sleep(5)
                            # 394.2万粉丝
                            # 1386粉丝
                            # //*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/p
                            if LotteryAssist.iselementByXpath(driver, '//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/p'):
                                print('查到了粉丝数')
                                fans_title = driver.find_element(By.XPATH, '//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/p')
                                print(fans_title.text)
                                fans_title_str = fans_title.text
                                split_array = fans_title_str.split('粉丝')
                                print(split_array[0])  # 394.2万
                                if split_array[0].find('万') != -1:
                                    fans_num = split_array[0].split('万')
                                    if float(fans_num[0]) > 1:
                                        # 大于1W的 可以看有没有抽奖的
                                        print('粉丝数大于1W的')
                                        # //*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/button  关注按钮
                                        time.sleep(3)
                                        # //*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/a 头像a标签
                                        avatarXpath = '//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/a'
                                        if LotteryAssist.iselementByXpath(driver, avatarXpath):
                                            a_tag = driver.find_element(By.XPATH, avatarXpath)
                                            print(a_tag.get_attribute('href')) # https://space.bilibili.com/3766866
                                            space_url = a_tag.get_attribute('href')
                                            space_url = 'https://space.bilibili.com/178690106'
                                            uid = space_url.split('com/')[1]
                                            uid = '178690106'
                                            print(uid) # uid
                                            a_tag.click()
                                            time.sleep(3)
                                            dyn = '/dynamic'
                                            dyn_url = space_url + dyn
                                            print(dyn_url)  # https://space.bilibili.com/3766866/dynamic
                                            driver.switch_to.window(driver.window_handles[2])
                                            driver.close()
                                            driver.switch_to.window(driver.window_handles[1])
                                            time.sleep(1)
                                            # driver.get(dyn_url)
                                            newWindowUrl = "window.open('" + dyn_url + "')"
                                            driver.execute_script(newWindowUrl)
                                            print('打开了动态页面')
                                            driver.switch_to.window(driver.window_handles[2])
                                            time.sleep(3)

                                            print('只找置顶是互动抽奖的')
                                            # 按uid(host_mid)获取dynamic_id(id_str)
                                            # https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset=&timezone_offset=-480&host_mid=7207905
                                            get_dynamic_id_url = 'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset=&timezone_offset=-480&host_mid=' + uid
                                            res = requests.get(get_dynamic_id_url)
                                            loaded = json.loads(res.text)
                                            dynamic_id = loaded.get('data').get('items')[0].get('id_str')
                                            hdcj_str = loaded.get('data').get('items')[0].get('modules').get('module_dynamic').get('desc').get('rich_text_nodes')[0].get('text')
                                            if hdcj_str.endswith('互动抽奖'):
                                                print('是互动抽奖')
                                                # 判断是否已开奖
                                                # https://api.vc.bilibili.com/lottery_svr/v1/lottery_svr/lottery_notice?dynamic_id=700543869440229449
                                                lottery_result_url = 'https://api.vc.bilibili.com/lottery_svr/v1/lottery_svr/lottery_notice?dynamic_id=' + dynamic_id
                                                response = requests.get(lottery_result_url)
                                                lottery_result_loaded = json.loads(response.text)
                                                if lottery_result_loaded.get('data').get('lottery_result') is None:
                                                    print('还没开奖')
                                                    # 给它关注,转发,评论套餐
                                                    # 关注是必须的
                                                    # 判断是否关注了
                                                    # className = h-f-icon
                                                    gz_btn_xpath = '//*[@id="app"]/div[1]/div[1]/div[2]/div[4]/span'
                                                    if LotteryAssist.iselementByXpath(driver, gz_btn_xpath):
                                                        print('没关注呢')
                                                        gz_btn = driver.find_element(By.XPATH, gz_btn_xpath)
                                                        gz_btn.click()
                                                        time.sleep(1)
                                                        # 关注完了要转发 //*[@id="page-dynamic"]/div[1]/div/div[1]/div[1]/div/div[2]/div[4]/div[1]/div
                                                        zf_xpath = '//*[@id="page-dynamic"]/div[1]/div/div[1]/div[1]/div/div[2]/div[4]/div[1]/div'
                                                        if LotteryAssist.iselementByXpath(driver, zf_xpath):
                                                            print('找到转发按钮')
                                                            zf_btn = driver.find_element(By.XPATH, zf_xpath)
                                                            zf_btn.click()
                                                            time.sleep(2)
                                                            zf_input_div_xpath = '//*[@id="page-dynamic"]/div[1]/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div'
                                                            if LotteryAssist.iselementByXpath(driver, zf_input_div_xpath):
                                                                print('找到转发时填入内容框')
                                                                zf_input_div = driver.find_element(By.XPATH, zf_input_div_xpath)
                                                                print('准备填入内容')
                                                                zf_input_div.send_keys('抽我抽我请抽我')
                                                                zf_submit_xpath = '//*[@id="page-dynamic"]/div[1]/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/div[2]/div[2]/button'
                                                                if LotteryAssist.iselementByXpath(driver, zf_submit_xpath):
                                                                    print('找到了转发按钮')
                                                                    zf_submit_btn = driver.find_element(By.XPATH, zf_submit_xpath)
                                                                    zf_submit_btn.click()
                                                                    print('点击了转发按钮')



                                        else:
                                            print(' no ')


                                        time.sleep(101)
                                time.sleep(10)
                            else:
                                print('没查到粉丝数')
                            time.sleep(10)
                        else:
                            print('不是用户的span')

                        time.sleep(10)

                    else:
                        print('没找到用户那一栏分类')
                        time.sleep(10)


                    time.sleep(10)
                else:
                    print("没找到搜索按钮")
                    time.sleep(10)
                time.sleep(100)
            else:
                print("没找到搜索框")

            time.sleep(100)
        else:
            print("没找到登录按钮")
            time.sleep(100)



a = LotteryAssist()
a.openChromeToBilibili()
