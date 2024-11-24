import time

import pyautogui
import datetime

print('请在关注您的分辨率，打开金铲铲游戏模拟器最大化窗口进行游戏')
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


def start(thumbs_x_y):
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
                time.sleep(2)
                continue
            if thumb_color[0] == 245 and thumb_color[1] == 245 and thumb_color[2] == 245:
                print('当前屏幕显示背景在5个大拇指的位置有杂色，请使用ALT+Tab组合键切出此窗口或关闭程序')
                time.sleep(2)
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
            print("等待中", formatted_time)
            init_sec = now.second


# 用来遍历的
list_6 = [1, 2, 3, 4, 5, 6]
# x1 = 720
# x2 = 914
# x3 = 1107
# x4 = 1300
# x5 = 1493
# y坐标
# y = 970
x1 = -1
x2 = -1
x3 = -1
x4 = -1
x5 = -1
y = -1
# 打开文件并逐行读取
with open('thumbs_x_y.txt', 'r') as file:
    for i, item in enumerate(list_6):
        line = file.readline()
        # print(line, end='')  # `end=''`用于避免打印额外的换行符
        # print('序号：', i, '值:', item)
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

start(check_input_params(x1, x2, x3, x4, x5, y))
