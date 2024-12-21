import threading
import tkinter as tk
from tkinter import ttk
import pyautogui
import time
import datetime
from paddleocr import PaddleOCR
import logging


max_screen_width, max_screen_height = pyautogui.size()
welcome = f'注意：请遵守一下规则：\n您当前屏幕像素宽度：{max_screen_width} 屏幕高度：{max_screen_height}\n' \
          f'因此，在填入x,y参数的时候\nx的值要在1到当前屏幕像素宽度 {max_screen_width} 之间\n' \
          f'y的值要在1到屏幕高度：{max_screen_height}之间'
pyautogui.alert(welcome)
# 定义全局变量大拇指的;异常突变的
x_coords = [720, 914, 1104, 1299, 1492]
y_coord = 968
param_yctb_name = ""

# 记录打印日志时间，设置打印等待日志间隔
global_now = datetime.datetime.now()
global_init_sec = global_now.second

thumbs_x_y = (
    (x_coords[0], y_coord),
    (x_coords[1], y_coord),
    (x_coords[2], y_coord),
    (x_coords[3], y_coord),
    (x_coords[4], y_coord)
)


class CoordinateApp:
    def __init__(self, root):
        self.root = root
        self.find_Ld_module()
        self.root.title("Coordinate App")
        self.thread = None
        # 创建全局停止事件
        global stop_event
        stop_event = threading.Event()
        # 创建标签和输入框
        print("CoordinateApp run")
        self.start_bt = None
        self.stop_bt = None
        self.create_widgets()
        # 设置窗口大小和位置 (宽x高+X偏移+Y偏移)
        self.root.geometry("550x350+100+100")
        # 绑定关闭事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        self.x_entries = []
        self.y_entry = None
        self.param_entry = None

        # 只允许输入数字的验证函数
        def only_numbers(char):
            return char.isdigit()

        validation = self.root.register(only_numbers)

        for i in range(5):
            # X 坐标标签和输入框
            x_label = ttk.Label(self.root, text=f"X 坐标 {i + 1}:")
            x_label.grid(column=0, row=i, padx=5, pady=5, sticky="W")

            x_entry = ttk.Entry(self.root, validate="key", validatecommand=(validation, '%S'))
            x_entry.grid(column=1, row=i, padx=5, pady=5, sticky="W")
            x_entry.insert(i, x_coords[i])  # 设置默认值
            self.x_entries.append(x_entry)

        # Y 坐标标签和输入框
        y_label = ttk.Label(self.root, text="Y 坐标:")
        y_label.grid(column=0, row=5, padx=5, pady=5, sticky="W")

        self.y_entry = ttk.Entry(self.root, validate="key", validatecommand=(validation, '%S'))
        self.y_entry.grid(column=1, row=5, padx=5, pady=5, sticky="W")
        self.y_entry.insert(0, y_coord)

        # 异常突变参数标签和输入框
        param_label = ttk.Label(self.root, text="异常突变:")
        param_label.grid(column=0, row=6, padx=5, pady=5, sticky="W")

        self.param_entry = ttk.Entry(self.root)
        self.param_entry.grid(column=1, row=6, padx=5, pady=5, sticky="W")

        self.param_entry = ttk.Combobox(self.root, values=["超高速", "狂战之怒", "力量训练", "防御型护盾", "即兴发挥", "双刀流", "壁垒", "终结者", "坚不可破", "荆棘满途", "恃强凌弱", "护甲山崩", "石头皮肤", "斥力发生器", "地下拳王", "魔法训练", "鹰眼", "奥术浩荡", "隐形", "友谊之力", "泰坦打击", "最后机会", "慢炖", "法师护甲", "恕瑞玛的传承", "千刀斩", "重量级打击手", "分享你的能量", "名片", "势不可挡", "真的会蟹", "史莱姆时间", "魔法专家", "翻盘故事", "防御专家", "物理专家", "冰霜触摸", "小我多多", "巨人体型", "根深蒂固", "连杀", "猎头者", "法强吸收", "攻击吸收", "火球", "贪财化身", "双狼佣兽", "剔除弱者", "深入敌阵", "迷失于未知", "龙魂", "绝不浪费", "镭射眼", "终极英雄", "震撼登场", "渴望能量", "星原之准"])
        self.param_entry.grid(column=1, row=6, padx=5, pady=5, sticky="W")
        self.param_entry.set('超高速')  # 设置默认值

        # 获取坐标按钮
        get_button = ttk.Button(self.root, text="获取坐标", command=self.get_coordinates)
        get_button.grid(column=0, row=7, padx=5, pady=5, sticky="W")
        self.start_bt = get_button

        # 显示坐标的标签
        self.coord_label = ttk.Label(self.root, text="当前坐标: ")
        self.coord_label.grid(column=0, row=8, columnspan=2, padx=5, pady=5)

        # 创建按钮2：停止线程
        stop_button = ttk.Button(self.root, text="停止", command=self.stop_thread_func)
        stop_button.grid(column=1, row=7, padx=10, pady=10)
        stop_button.config(state='disabled')  # 初始状态为禁用
        self.stop_bt = stop_button

    def get_coordinates(self):
        global x_coords, y_coord, param_yctb_name, thumbs_x_y
        x_coords = [int(entry.get()) for entry in self.x_entries]
        y_coord = int(self.y_entry.get())
        param_yctb_name = self.param_entry.get()
        self.coord_label.config(text=f"当前坐标: {[(x, y_coord) for x in x_coords]}, 异常突变参数: {param_yctb_name}")
        thumbs_x_y = (
            (x_coords[0], y_coord),
            (x_coords[1], y_coord),
            (x_coords[2], y_coord),
            (x_coords[3], y_coord),
            (x_coords[4], y_coord)
        )
        print(f"输入参数：{thumbs_x_y} 异常突变：{param_yctb_name}")
        if self.thread is None or not self.thread.is_alive():
            stop_event.clear()
            self.thread = threading.Thread(target=GetCard().get_cards_and_yctb)
            self.thread.start()
            self.start_bt.config(state='disabled')  # 禁用启动按钮
            self.stop_bt.config(state='normal')  # 启用停止按钮

    def stop_thread_func(self):
        print(f'stop_thread_func： self.thread={self.thread}')
        if self.thread is not None:
            stop_event.set()
            self.thread.join()
            self.thread = None
            self.start_bt.config(state='normal')  # 禁用启动按钮
            self.stop_bt.config(state='disabled')  # 启用停止按钮

    def on_closing(self):
        print('关闭窗口')
        self.stop_thread_func()
        self.root.destroy()

    # 找到雷电模拟器
    def find_Ld_module(self):
        try:
            # 获取雷电模拟器 将雷电模拟器窗口最大化，使窗口处于最前面
            win = pyautogui.getWindowsWithTitle('雷电模拟器')
            if len(win) > 0:
                print('找到雷电模拟器窗口了')
            win[0].maximize()
            win[0].activate()
        except BaseException as e:
            print('没找到雷电模拟器窗口')
            pyautogui.alert('没找到雷电模拟器窗口，请先打开雷电模拟器，再重新启动本程序，点击确认后程序就会关闭')
            exit(0)


class GetCard:
    def __init__(self):
        # 控制识别组件日志频率
        logging.basicConfig(level=logging.INFO)
        # 假设ppocr使用的是名为'ppocr'的logger
        logger_ppocr = logging.getLogger('ppocr')
        logger_ppocr.setLevel(logging.INFO)

    def get_cards_new(self):
        global global_init_sec, thumbs_x_y
        for index, thumb in enumerate(thumbs_x_y):
            thumb_color = pyautogui.pixel(thumb[0], thumb[1])
            # print(index, f'x={thumb[0]},y={thumb[1]}', thumb_color[0], thumb_color[1], thumb_color[2])
            # RGB三色
            red = 240 < thumb_color[0]
            green = 240 < thumb_color[1]
            blue = 200 < thumb_color[2]

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
                print(index + 1, "真的有true,即将点击", thumb[0], thumb[1],datetime.datetime.now())
                # pyautogui.click(thumb[0], thumb[1])
                # 改为模拟键盘按钮
                pyautogui.press(str(index + 1))
        # 获取当前时间
        now = datetime.datetime.now()
        # 格式化时间为“时:分:秒”
        formatted_time = now.strftime("%H:%M:%S")
        if abs(now.second - global_init_sec) >= 10:
            # print("当前时间（时:分:秒）:", formatted_time)
            print("da等待大拇指出现...", formatted_time)
            global_init_sec = now.second

    def get_cards_and_yctb(self):
        global param_yctb_name, thumbs_x_y
        print(f'get_cards_and_yctb：{thumbs_x_y},{param_yctb_name}')
        # 4-6阶段有异常突变，记录4-6出现的位置
        left4_6 = 686
        top4_6 = 42
        width4_6 = 60
        height4_6 = 25

        # 异常突变 名称 出现的位置 一个字 宽38
        left_yctb = 574
        top_yctb = 870
        width_yctb = 118
        height_yctb = 36
        # 4-6得算作英文来识别
        ocr_en = PaddleOCR(use_angle_cls=True, lang="en")
        ocr = PaddleOCR(use_angle_cls=True, lang="ch")
        stage_flag = False
        # 记录打印日志时间，设置打印等待日志间隔
        init_sec2 = datetime.datetime.now().second
        yctb_stage = '4-6'
        yctb_stage_recycle = '4-6'
        # 和启动停止按钮线程联动
        while not stop_event.is_set():
            time.sleep(0.06)
            screen4_6 = pyautogui.screenshot(region=(left4_6, top4_6, width4_6, height4_6))
            screen4_6.save(f"stage_screenshot4_6.png")

            screen4_6 = pyautogui.screenshot(region=(left_yctb, top_yctb, width_yctb, height_yctb))
            screen4_6.save(f"yctb_screenshot.png")

            ocr_en_result_list = ocr_en.ocr('stage_screenshot4_6.png', cls=True)
            ocr_en_result = ocr_en_result_list[0]
            if ocr_en_result is not None:
                # 捕获到字符了
                stage_num = ocr_en_result[0][1][0]
                # 4-6
                if yctb_stage == stage_num:
                    print('ocr到4-6阶段')
                    stage_flag = True
                    # 记录开始时间的时间戳
                    start_time = time.time()
                    # 判断 异常突变 名称
                    while stage_flag:
                        screen4_6 = pyautogui.screenshot(region=(left_yctb, top_yctb, width_yctb, height_yctb))
                        screen4_6.save(f"yctb_screenshot.png")
                        ocr_result_list = ocr.ocr('yctb_screenshot.png', cls=True)
                        ocr_result = ocr_result_list[0]
                        if ocr_result is not None:
                            # 获取当前时间的时间戳
                            current_time = time.time()
                            # 计算时间差
                            time_difference = current_time - start_time
                            # 判断时间差是否达到或超过60秒 # 退出循环
                            if time_difference >= 60:
                                print('4-6选择异常突变超时')
                                stage_flag = False
                                yctb_stage = ''
                            # 异常突变名6称str
                            print('异常突变名称:', ocr_result[0][1][0])
                            # 最长5个字的，最短2个字的； 2个字的会俩字（
                            # 先对上2个字 3个字的又2个魔法训练，魔法专家
                            if len(str(ocr_result[0][1][0])) == 3:
                                if param_yctb_name[:3] == ocr_result[0][1][0]:
                                    print('====名称对上了，准备按钮6===')
                                    pyautogui.press('6')
                                    stage_flag = False
                                    yctb_stage = ''
                                    print('****按了6，异常突变暂时结束！****')
                            if len(str(ocr_result[0][1][0])) > 3:
                                if param_yctb_name[:2] == str(ocr_result[0][1][0])[:2]:
                                    print('====名称对上了，准备按钮6===')
                                    pyautogui.press('6')
                                    stage_flag = False
                                    yctb_stage = ''
                                    print('****按了6，异常突变暂时结束！****')
                else:
                    # 不是4-6，但是是2和3阶段
                    if stage_num is not None and str(stage_num).startswith('2-'):
                        print('ocr二阶段,时间：', datetime.datetime.now().strftime("%H:%M:%S"))
                        yctb_stage = yctb_stage_recycle
                    if stage_num is not None and str(stage_num).startswith('3-'):
                        print('ocr三阶段,时间：', datetime.datetime.now().strftime("%H:%M:%S"))
                        yctb_stage = yctb_stage_recycle
                    # 获取当前时间
                    now = datetime.datetime.now()
                    # 格式化时间为“时:分:秒”
                    formatted_time = now.strftime("%H:%M:%S")
                    if abs(now.second - init_sec2) >= 10:
                        print('ocr截取回合数：', stage_num, "等待匹配到正确的回合数", formatted_time)
                        init_sec2 = now.second
                    # 没有捕获4-6阶段的字符,执行拿卡操作
                    self.get_cards_new()
            else:
                self.get_cards_new()


if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateApp(root)
    root.mainloop()
