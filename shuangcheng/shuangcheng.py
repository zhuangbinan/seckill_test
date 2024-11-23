import time

import pyautogui
from pynput import keyboard
import datetime

# 获取当前时间
# now = datetime.datetime.now()

# 格式化时间为“时:分:秒”
# formatted_time = now.strftime("%H:%M:%S")

# 单独获取秒数
# seconds = now.second

# print("当前时间（时:分:秒）:", formatted_time)
# print("当前秒数:", seconds)

print('请在1920×1080分辨率下打开金铲铲游戏模拟器全屏进行游戏')
# 获取屏幕分辨率（宽高） Size(width=1920, height=1080)
screen_width, screen_height = pyautogui.size()
print('Hello 双城之战!', '屏幕宽度：', screen_width, '屏幕高度：', screen_height)

time.sleep(2)
# allTitles = pyautogui.getAllWindows()
# active_win = pyautogui.getActiveWindowTitle()
# print(active_win)
# print(type(allTitles))
#
# print(type(allTitles[0]))

# for t in allTitles:
#     print(t)

win = pyautogui.getWindowsWithTitle('雷电模拟器')

# game_window_list = pyautogui.getWindowsWithTitle('腾讯手游助手(64位)')

if len(win) > 0:
    print('找到游戏窗口了')
else:
    raise BaseException("没有找到游戏窗口")
win[0].maximize()
win[0].activate()


def start():
    # 框靠右边的时候的分辨率
    thumbs_x_y = (
        (842, 936),
        (1026, 936),
        (1210, 936),
        (1394, 936),
        (1578, 936)
    )
    # 1920*10805个大拇指的坐标 702,1005;910,1005; 1118,1005; 1326,1005; 1534,1005;
    thumbs_x_y = (
        (702, 1005),
        (910, 1005),
        (1118, 1005),
        (1320, 1005),
        (1534, 1005)
    )

    thumbs_x_y = (
        (720, 970),
        (914, 970),
        (1107, 970),
        (1300, 970),
        (1493, 970)
    )
    # 记录打印日志时间，设置打印等待日志间隔
    now = datetime.datetime.now()
    init_sec = now.second
    while True:
        for index, thumb in enumerate(thumbs_x_y):
            thumb_color = pyautogui.pixel(thumb[0], thumb[1])
            # print(thumb_color[0] > 240, thumb_color[1] > 240, thumb_color[2] > 200)
            red = 240 < thumb_color[0]
            green = 240 < thumb_color[1]
            blue = 210 < thumb_color[2]

            # not_white_color
            if thumb_color[0] == 255 and thumb_color[1] == 255 and thumb_color[2] == 255:
                continue
            if thumb_color[0] == 245 and thumb_color[1] == 245 and thumb_color[2] == 245:
                continue
            if thumb_color[0] == thumb_color[2]:
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
        if now.second - init_sec >= 10:
            # print("当前时间（时:分:秒）:", formatted_time)
            print("等待中", formatted_time)
            init_sec = now.second

start()