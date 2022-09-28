import requests
from selenium import webdriver

from selenium.webdriver.common.by import By
import time
import datetime
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

    def getRandomZfStr(browser, i):
        list = ['抽我抽我抽我', '抽我,抽我,抽我', '抽我请抽我抽我', '请抽我抽我抽我', '抽我抽我请抽我', '抽我,抽我,请抽我', '请抽我,不要客气', '让我看看是哪个luckyDog被抽中了', '分母集合', '偶尔也当一个分子啊']
        return list[i]

    # 按顺序关闭窗口 closeWindowWithOrder
    def closeWindowWithOrder(browser):
        browser.switch_to.window(browser.window_handles[2])
        browser.close()
        browser.switch_to.window(browser.window_handles[1])
        browser.close()
        browser.switch_to.window(browser.window_handles[0])  # 然后continue
        print('已有序关闭窗口')

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
        bilibili_url = 'https://www.bilibili.com'
        # 喵喵折APP 有个抽完的
        # 科技美学 有还没抽完的
        driver.get(bilibili_url)
        time.sleep(3)

        if LotteryAssist.iselementByClassName(driver, 'header-login-entry'):
            # print('点击登录按钮', flush=True)
            # driver.find_element(By.CLASS_NAME, 'header-login-entry').click()
            # while 1 == 1:
            #     if LotteryAssist.iselementByClassName(driver, 'header-avatar-wrap'):
            #         print("已经登录")
            #         break
            #     else:
            #         print("没登录")
            #     time.sleep(5)

            time.sleep(3)
            # print("假如登录了")

            if LotteryAssist.iselementByClassName(driver, 'nav-search-input'):
                print("找到搜索框")
                search_input = driver.find_element(By.CLASS_NAME, 'nav-search-input')
                search_input.send_keys('科技美学')  # 应该要退到这一步来重新搜索
                if LotteryAssist.iselementByClassName(driver, 'nav-search-btn'):
                    print("点击搜索按钮")
                    search_btn = driver.find_element(By.CLASS_NAME, 'nav-search-btn')
                    search_btn.click()
                    print("点击了搜索按钮")
                    time.sleep(3)

                    driver.switch_to.window(driver.window_handles[1])  # 切换到新的窗口
                    print('当前窗口url')
                    print(driver.current_url)

                    current_url = driver.current_url
                    pre_url = 'https://search.bilibili.com/upuser?keyword'
                    end_url = '&order=fans'
                    final_url = current_url.replace('https://search.bilibili.com/all?keyword', pre_url) + end_url

                    print(final_url)
                    driver.get(final_url)
                    time.sleep(5)
                    if LotteryAssist.iselementByXpath(driver, '//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/p'):
                        print('查到了粉丝数')
                        fans_title = driver.find_element(By.XPATH, '//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/p')
                        print(fans_title.text)
                        fans_title_str = fans_title.text
                        split_array = fans_title_str.split('粉丝')
                        print(split_array[0])  # 394.2万
                        if split_array[0].find('万') != -1:
                            # 大于1W fans的 才看有没有抽奖的
                            print('粉丝数大于1W的')
                            time.sleep(3)
                            avatarXpath = '//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/a'
                            if LotteryAssist.iselementByXpath(driver, avatarXpath):
                                print('进一步查看搜索结果的第0个详情')
                                a_tag = driver.find_element(By.XPATH, avatarXpath)
                                print(a_tag.get_attribute('href'))  # https://space.bilibili.com/3766866
                                space_url = a_tag.get_attribute('href')
                                uid = space_url.split('com/')[1]
                                print('当前UID:', uid)  # uid
                                a_tag.click()  # 点了一下a标签, 即头像那个地方 https://space.bilibili.com/3766866 , 会跳转到这个a标签地址去
                                time.sleep(3)
                                dyn = '/dynamic'
                                dyn_url = space_url + dyn
                                print(dyn_url)  # https://space.bilibili.com/3766866/dynamic
                                driver.switch_to.window(driver.window_handles[2])
                                driver.close()  # 关闭 https://space.bilibili.com/3766866
                                driver.switch_to.window(driver.window_handles[1])  # 搜索的结果页
                                time.sleep(1)
                                new_window_url = "window.open('" + dyn_url + "')"
                                driver.execute_script(new_window_url)    # 打开 https://space.bilibili.com/3766866/dynamic
                                print('打开动态页面')
                                time.sleep(3)
                                driver.switch_to.window(driver.window_handles[2])    # 切到 https://space.bilibili.com/3766866/dynamic
                                print('打开了动态页面')
                                print('只找置顶是互动抽奖的')
                                # 按uid(host_mid)获取dynamic_id(id_str)
                                # https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset=&timezone_offset=-480&host_mid=7207905
                                get_dynamic_id_url = 'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset=&timezone_offset=-480&host_mid=' + uid
                                res = requests.get(get_dynamic_id_url)
                                loaded = json.loads(res.text)
                                dynamic_id = loaded.get('data').get('items')[0].get('id_str')
                                print('获取到动态id', dynamic_id)
                                hdcj_str = ''    # 互动抽奖的预设
                                hdcj_flag = False

                                try:
                                    hdcj_str = loaded.get('data').get('items')[0].get('modules').get('module_dynamic').get('desc').get('rich_text_nodes')[0].get('text')
                                    if hdcj_str.endswith('互动抽奖'):
                                        hdcj_flag = True
                                except:
                                    print('不是互动抽奖,且异常')
                                    LotteryAssist.closeWindowWithOrder(driver)
                                    print('遇到异常,需要continue')
                                if hdcj_flag:
                                    print('是互动抽奖')
                                    # 判断是否已开奖
                                    # https://api.vc.bilibili.com/lottery_svr/v1/lottery_svr/lottery_notice?dynamic_id=700543869440229449
                                    lottery_result_url = 'https://api.vc.bilibili.com/lottery_svr/v1/lottery_svr/lottery_notice?dynamic_id=' + dynamic_id
                                    response = requests.get(lottery_result_url)
                                    lottery_result_loaded = json.loads(response.text)
                                    print('判断是否已开奖')
                                    if lottery_result_loaded.get('data').get('lottery_result') is None:
                                        print('还没开奖')
                                        # 判断是否关注了
                                        gz_btn_xpath_if_not_gz = '//*[@id="app"]/div[1]/div[1]/div[2]/div[4]/span'
                                        gz_btn_xpath_if_gz = '//*[@id="app"]/div[1]/div[1]/div[2]/div[4]/div[1]/div'
                                        # 已关注的XPATH  //*[@id="app"]/div[1]/div[1]/div[2]/div[4]/div[1]/div
                                        # 没关注的XPATH  //*[@id="app"]/div[1]/div[1]/div[2]/div[4]/span
                                        if LotteryAssist.iselementByXpath(driver, gz_btn_xpath_if_not_gz):
                                            print('没关注呢,需要先关注')
                                            gz_btn = driver.find_element(By.XPATH, gz_btn_xpath_if_not_gz)
                                            print('点击关注按钮')
                                            gz_btn.click()
                                            time.sleep(1)
                                            print('点了关注按钮')
                                            time.sleep(1)
                                            gz_btn = driver.find_element(By.XPATH, gz_btn_xpath_if_gz)
                                            if gz_btn.text.endswith('已关注'):
                                                print('已关注')
                                                # 关注完了要转发 //*[@id="page-dynamic"]/div[1]/div/div[1]/div[1]/div/div[2]/div[4]/div[1]/div
                                                zf_xpath = '//*[@id="page-dynamic"]/div[1]/div/div[1]/div[1]/div/div[2]/div[4]/div[1]/div'
                                                if LotteryAssist.iselementByXpath(driver, zf_xpath):
                                                    print('找到转发按钮')
                                                    zf_btn = driver.find_element(By.XPATH, zf_xpath)
                                                    print('点击转发按钮')
                                                    zf_btn.click()
                                                    time.sleep(2)
                                                    zf_input_div_xpath = '//*[@id="page-dynamic"]/div[1]/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div'
                                                    if LotteryAssist.iselementByXpath(driver, zf_input_div_xpath):
                                                        print('找到转发时填入文字的内容框')
                                                        zf_input_div = driver.find_element(By.XPATH, zf_input_div_xpath)
                                                        print('准备填入内容')
                                                        zf_content = LotteryAssist.getRandomZfStr(driver, int(datetime.datetime.now().strftime('%S')[1:2]))
                                                        zf_input_div.send_keys(zf_content)  # 可以做个随机的
                                                        print('已填入转发时文字内容')
                                                        zf_submit_xpath = '//*[@id="page-dynamic"]/div[1]/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/div[2]/div[2]/button'
                                                        if LotteryAssist.iselementByXpath(driver, zf_submit_xpath):
                                                            print('找到了转发提交按钮')
                                                            zf_submit_btn = driver.find_element(By.XPATH, zf_submit_xpath)
                                                            zf_submit_btn.click()
                                                            print('点击了转发提交按钮,完成1次抽奖任务')
                                            else:
                                                print('点了关注按钮,但是没有关注成功')
                                                LotteryAssist.closeWindowWithOrder(driver)
                                        else:
                                            print('只想关注没关注的up的抽奖活动')
                                            LotteryAssist.closeWindowWithOrder(driver)
                                    else:
                                        print('已经开奖了')
                                        LotteryAssist.closeWindowWithOrder(driver)
                                else:
                                    print('不是互动抽奖,可以结束当前窗口了')
                                    LotteryAssist.closeWindowWithOrder(driver)
                            #  这里开始有0,1,2共3个窗口,1-b站主页,2-搜索结果页,3-动态页
                            else:
                                print('没获取到第0个详情')
                        else:
                            print('粉丝数没大于1W,需要continue')
                    else:
                        print('没查到粉丝数,大概率是没有搜索结果,需要continue')
                else:
                    print("没找到搜索按钮")
            else:
                print("没找到搜索框")

            print('程序结束')
            time.sleep(100)
        else:
            print("没找到登录按钮")
            time.sleep(100)


a = LotteryAssist()
a.openChromeToBilibili()
