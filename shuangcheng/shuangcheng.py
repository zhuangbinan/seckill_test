import time

import pyautogui
import datetime
from paddleocr import PaddleOCR
import threading
import logging

# 控制识别组件日志频率
logging.basicConfig(level=logging.INFO)
# 假设ppocr使用的是名为'ppocr'的logger
logger_ppocr = logging.getLogger('ppocr')
logger_ppocr.setLevel(logging.INFO)


# 程序入口
def main():
    print('请关注您的分辨率，此程序需要配合thumbs_x_y.txt文件同时使用')
    print('简介：thumbs_x_y.txt文件')
    print('此文件为配置文件，内容一共7行')
    print('前5行为金铲铲内置助手大拇指在你电脑上的x坐标')
    print('第6行为y坐标，y坐标只有1个，因为5个大拇指都是在同一水平线上的')
    print('第7行为异常突变名称，填入您想要选择的异常突变名称，如：魔法训练')
    print('注意：此文件放在和.exe文件同级目录下，没有此文件，程序无法正常运行')
    # 获取屏幕分辨率（宽高） Size(width=1920, height=1080)
    screen_width, screen_height = pyautogui.size()
    welcome = 'Hello 双城之战!您当前屏幕像素宽度：' + str(screen_width) + '屏幕高度：' + str(screen_height)
    pyautogui.alert(welcome)

    time.sleep(1)
    # 获取雷电模拟器
    win = pyautogui.getWindowsWithTitle('雷电模拟器')

    if len(win) > 0:
        print('找到雷电模拟器窗口了')
    else:
        raise BaseException("没有找到雷电模拟器窗口")
    # 将游戏窗口最大化，使窗口处于最前面
    win[0].maximize()
    win[0].activate()
    # 用来遍历的
    list_7 = [1, 2, 3, 4, 5, 6, 7]
    # 初始化这几个参数
    x1 = -1
    x2 = -1
    x3 = -1
    x4 = -1
    x5 = -1
    y = -1
    yctb_name = ''
    # 打开文件并逐行读取
    with open('thumbs_x_y.txt', 'r') as file:
        for i, item in enumerate(list_7):
            line = file.readline()
            if i == 0:
                x1 = int(line)
            if i == 1:
                x2 = int(line)
            if i == 2:
                x3 = int(line)
            if i == 3:
                x4 = int(line)
            if i == 4:
                x5 = int(line)
            if i == 5:
                y = int(line)
            if i == 6:
                print('读取配置文件异常突变参数:', line)
                yctb_name = line

    get_cards_param = check_input_params(x1, x2, x3, x4, x5, y)
    # 创建线程对象
    thread1 = threading.Thread(target=get_cards, args=(get_cards_param,))
    thread2 = threading.Thread(target=get_yctb, args=(yctb_name,))
    # 启动线程
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


# 校验坐标要有值 定义一个校验函数
def is_valid_number(value):
    # 检查是否为数字类型（int 或 float）且不是 None
    return isinstance(value, (int, float)) and value is not None


# 检查入参
def check_input_params(x1, x2, x3, x4, x5, y):
    # 校验所有 x 坐标和 y 坐标
    if not all(is_valid_number(x) for x in [x1, x2, x3, x4, x5]):
        raise ValueError("所有 x 坐标都必须是数字且不能为空")

    if not is_valid_number(y):
        raise ValueError("y 坐标必须是数字且不能为空")
    # 5个大拇指坐标,x坐标不同,y坐标一样，都是一条水平线上的
    thumbs_x_y = (
        (x1, y),
        (x2, y),
        (x3, y),
        (x4, y),
        (x5, y)
    )
    return thumbs_x_y


# 拿卡
def get_cards(thumbs_x_y):
    # 记录打印日志时间，设置打印等待日志间隔
    now = datetime.datetime.now()
    init_sec = now.second
    while True:
        for index, thumb in enumerate(thumbs_x_y):
            thumb_color = pyautogui.pixel(thumb[0], thumb[1])
            # print(thumb_color[0] > 240, thumb_color[1] > 240, thumb_color[2] > 200)
            # RGB三色
            red = 240 < thumb_color[0]
            green = 240 < thumb_color[1]
            blue = 210 < thumb_color[2]

            # not_white_color 白色背景会影响程序判断，对白色的处理
            if thumb_color[0] == 255 and thumb_color[1] == 255 and thumb_color[2] == 255:
                print('当前屏幕显示背景在5个大拇指的位置有白色，请使用ALT+Tab组合键切出此窗口或关闭程序')
                time.sleep(3)
                continue
            if thumb_color[0] == 245 and thumb_color[1] == 245 and thumb_color[2] == 245:
                print('当前屏幕显示背景在5个大拇指的位置有杂色，请使用ALT+Tab组合键切出此窗口或关闭程序')
                time.sleep(3)
                continue

            if red and green and blue:
                print(index, "真的有true,即将点击", thumb[0], thumb[1])
                # pyautogui.click(thumb[0], thumb[1])
                # 改为模拟键盘按钮
                if index == 0:
                    print('按键1')
                    pyautogui.press('1')
                if index == 1:
                    print('按键2')
                    pyautogui.press('2')
                if index == 2:
                    print('按键3')
                    pyautogui.press('3')
                if index == 3:
                    print('按键4')
                    pyautogui.press('4')
                if index == 4:
                    print('按键5')
                    pyautogui.press('5')

        # 获取当前时间
        now = datetime.datetime.now()
        # 格式化时间为“时:分:秒”
        formatted_time = now.strftime("%H:%M:%S")
        if abs(now.second - init_sec) >= 10:
            # print("当前时间（时:分:秒）:", formatted_time)
            print("da等待大拇指出现...", formatted_time)
            init_sec = now.second


# 获取异常突变，需要在配置文件填异常突变名称
def get_yctb(param_yctb_name):
    if param_yctb_name is not None and param_yctb_name != '':
        print('异常突变函数被调用')
        # 4-6阶段有异常突变，记录4-6出现的位置
        # 702
        left4_6 = 686
        top4_6 = 42
        width4_6 = 60
        height4_6 = 25

        # 异常突变 名称 出现的位置 一个字 宽38
        left_yctb = 574
        top_yctb = 870
        width_yctb = 128
        height_yctb = 36

        # 4-6得算作英文来识别
        ocr_en = PaddleOCR(use_angle_cls=True, lang="en")
        ocr = PaddleOCR(use_angle_cls=True, lang="ch")
        stage_flag = False
        # 记录打印日志时间，设置打印等待日志间隔
        now = datetime.datetime.now()
        init_sec1 = now.second
        init_sec2 = now.second
        # 判断回合数 阶段数
        while True:
            time.sleep(0.1)
            screen4_6 = pyautogui.screenshot(region=(left4_6, top4_6, width4_6, height4_6))
            screen4_6.save(f"stage_screenshot4_6.png")

            screen4_6 = pyautogui.screenshot(region=(left_yctb, top_yctb, width_yctb, height_yctb))
            screen4_6.save(f"yctb_screenshot.png")

            ocr_en_result_list = ocr_en.ocr('stage_screenshot4_6.png', cls=True)
            ocr_en_result = ocr_en_result_list[0]
            if ocr_en_result is not None:
                stage_num = ocr_en_result[0][1][0]

                if stage_num is not None and str(stage_num).startswith('2'):
                    print('ocr二阶段,睡眠20s,开始时间：', datetime.datetime.now().strftime("%H:%M:%S"))
                    time.sleep(20)
                    print('ocr二阶段,睡眠20s,结束时间：', datetime.datetime.now().strftime("%H:%M:%S"))
                if stage_num is not None and str(stage_num).startswith('3'):
                    print('ocr三阶段,睡眠20s,开始时间：', datetime.datetime.now().strftime("%H:%M:%S"))
                    time.sleep(20)
                    print('ocr三阶段,睡眠20s,结束时间：', datetime.datetime.now().strftime("%H:%M:%S"))
                # 4-6
                if '4-6' == stage_num:
                    print('ocr到4-6阶段')
                    stage_flag = True
                    # 判断 异常突变 名称
                    while stage_flag:
                        ocr_result_list = ocr.ocr('yctb_screenshot.png', cls=True)
                        ocr_result = ocr_result_list[0]
                        if ocr_result is not None:
                            # 异常突变名6称str
                            print('异常突变名称:', ocr_result[0][1][0])
                            if param_yctb_name == ocr_result[0][1][0]:
                                print('====名称对上了，准备按钮6===')
                                pyautogui.press('6')
                                stage_flag = False
                                print('****按了6，异常突变进程结束！****')
                else:
                    # 获取当前时间
                    now = datetime.datetime.now()
                    # 格式化时间为“时:分:秒”
                    formatted_time = now.strftime("%H:%M:%S")
                    if abs(now.second - init_sec2) >= 10:
                        print('ocr截取回合数：', stage_num, "等待匹配到正确的回合数", formatted_time)
                        init_sec2 = now.second
            else:
                # 获取当前时间
                now = datetime.datetime.now()
                # 格式化时间为“时:分:秒”
                formatted_time = now.strftime("%H:%M:%S")
                if abs(now.second - init_sec1) >= 10:
                    # print("当前时间（时:分:秒）:", formatted_time)
                    print("ocr等待指定回合数位置有识别的字符", formatted_time)
                    init_sec1 = now.second

    if param_yctb_name is None:
        print('异常突变 参数有误 None')
    if param_yctb_name == '':
        print("异常突变 参数没填")


if __name__ == '__main__':
    main()

