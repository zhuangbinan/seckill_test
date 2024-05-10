import datetime
import time
import pyautogui
import cv2
from paddleocr import PaddleOCR, draw_ocr
import openpyxl

print('请务必在1920×1080分辨率下打开鹅鸭杀游戏')
# 获取屏幕分辨率（宽高） Size(width=1920, height=1080)
screenWidth, screenHeight = pyautogui.size()
with open('logs/ggd_out.log', 'a') as f:
    print('Hello GGD!', '屏幕宽度：', screenWidth, '屏幕高度：', screenHeight, file=f)
    print('Hello GGD!', '屏幕宽度：', screenWidth, '屏幕高度：', screenHeight)

# 指定要截取的区域
left = 0
top = 0
width = 1920
height = 1080

# 截取指定区域的屏幕截图
# 设置截取范围
screenshot = pyautogui.screenshot(region=(left, top, width, height))

# 要判断是否在会议页面
meeting_flag = 1
while meeting_flag == 1:
    try:
        meeting_img = pyautogui.locateOnScreen('mtmp.png', confidence=0.9)
        with open('logs/ggd_out.log', 'a') as f:
            print('找到地图图标了，说明进会议了', file=f)
            print('找到地图图标了，说明进会议了')
        # 如果meeting_img没找到就会抛异常，找到了就往下截图
        screenshot.save('ggd_screenshot.png')
        # 截图后等待2秒，让图片保存好，2s应该够了
        time.sleep(2)
        # 退出循环flag
        meeting_flag = 2
    except pyautogui.ImageNotFoundException:
        with open('logs/ggd_out.log', 'a') as f:
            print('没进会议呢，还在找地图图标', file=f)
            print('没进会议呢，还在找地图图标')
        time.sleep(2)

imgGgd = cv2.imread('ggd_screenshot.png')


# 根据分辨率截图，截取昵称
# 第一行第一个
crop_row1_col1_nickname = imgGgd[198:231, 108:466]
# 第二行第一个
crop_row2_col1_nickname = imgGgd[231 + 128 + 20:231 + 128 + 20 + 33, 108:466]
# 第三行第一个
crop_row3_col1_nickname = imgGgd[231 + 128 + 20 + 33 + (128 + 20):231 + 128 + 20 + 33 + (128 + 20 + 33), 108:466]
# 第四行第一个
crop_row4_col1_nickname = imgGgd[
                          231 + 128 + 20 + 33 + (128 + 20 + 33) + (128 + 20):231 + 128 + 20 + 33 + (128 + 20 + 33) + (
                                      128 + 20) + 33, 108:466]

# 第一行第二个
crop_row1_col2_nickname = imgGgd[198:231, 473 + 20 + 8:473 + 366 + 20]
# 第一行第三个
crop_row1_col3_nickname = imgGgd[198:231, 473 + 366 + 20 + 20 + 8:473 + 366 + 20 + 366 + 20]
# 第一行第四个
crop_row1_col4_nickname = imgGgd[198:231, 473 + 366 + 20 + 366 + 20 + 20 + 8:473 + 366 + 20 + 366 + 20 + 366 + 20]

# 第二行第二个 y, x
crop_row2_col2_nickname = imgGgd[231 + 128 + 20:231 + 128 + 20 + 33, 473 + 20 + 8:473 + 366 + 20]
# 第二行第三个 y, x
crop_row2_col3_nickname = imgGgd[231 + 128 + 20:231 + 128 + 20 + 33, 473 + 366 + 20 + 20 + 8:473 + 366 + 20 + 366 + 20]
# 第二行第四个 y, x
crop_row2_col4_nickname = imgGgd[231 + 128 + 20:231 + 128 + 20 + 33,
                          473 + 366 + 20 + 366 + 20 + 20 + 8:473 + 366 + 20 + 366 + 20 + 366 + 20]

# 第三行第二个 y, x
crop_row3_col2_nickname = imgGgd[231 + 128 + 20 + 33 + (128 + 20):231 + 128 + 20 + 33 + (128 + 20 + 33),
                          473 + 20 + 8:473 + 366 + 20]
# 第三行第三个 y, x
crop_row3_col3_nickname = imgGgd[231 + 128 + 20 + 33 + (128 + 20):231 + 128 + 20 + 33 + (128 + 20 + 33),
                          473 + 366 + 20 + 20 + 8:473 + 366 + 20 + 366 + 20]
# 第三行第四个 y, x
crop_row3_col4_nickname = imgGgd[231 + 128 + 20 + 33 + (128 + 20):231 + 128 + 20 + 33 + (128 + 20 + 33),
                          473 + 366 + 20 + 366 + 20 + 20 + 8:473 + 366 + 20 + 366 + 20 + 366 + 20]

# 第四行第二个
crop_row4_col2_nickname = imgGgd[
                          231 + 128 + 20 + 33 + (128 + 20 + 33) + (128 + 20):231 + 128 + 20 + 33 + (128 + 20 + 33) + (
                                      128 + 20) + 33, 473 + 20 + 8:473 + 366 + 20]
# 第四行第三个
crop_row4_col3_nickname = imgGgd[
                          231 + 128 + 20 + 33 + (128 + 20 + 33) + (128 + 20):231 + 128 + 20 + 33 + (128 + 20 + 33) + (
                                      128 + 20) + 33, 473 + 366 + 20 + 20 + 8:473 + 366 + 20 + 366 + 20]
# 第四行第四个
crop_row4_col4_nickname = imgGgd[
                          231 + 128 + 20 + 33 + (128 + 20 + 33) + (128 + 20):231 + 128 + 20 + 33 + (128 + 20 + 33) + (
                                      128 + 20) + 33,
                          473 + 366 + 20 + 366 + 20 + 20 + 8:473 + 366 + 20 + 366 + 20 + 366 + 20]

# 输出截图
cv2.imwrite('crop_row1_col1_nickname.png', crop_row1_col1_nickname)
cv2.imwrite('crop_row2_col1_nickname.png', crop_row2_col1_nickname)
cv2.imwrite('crop_row3_col1_nickname.png', crop_row3_col1_nickname)
cv2.imwrite('crop_row4_col1_nickname.png', crop_row4_col1_nickname)

cv2.imwrite('crop_row1_col2_nickname.png', crop_row1_col2_nickname)
cv2.imwrite('crop_row1_col3_nickname.png', crop_row1_col3_nickname)
cv2.imwrite('crop_row1_col4_nickname.png', crop_row1_col4_nickname)

cv2.imwrite('crop_row2_col2_nickname.png', crop_row2_col2_nickname)
cv2.imwrite('crop_row2_col3_nickname.png', crop_row2_col3_nickname)
cv2.imwrite('crop_row2_col4_nickname.png', crop_row2_col4_nickname)

cv2.imwrite('crop_row3_col2_nickname.png', crop_row3_col2_nickname)
cv2.imwrite('crop_row3_col3_nickname.png', crop_row3_col3_nickname)
cv2.imwrite('crop_row3_col4_nickname.png', crop_row3_col4_nickname)

cv2.imwrite('crop_row4_col2_nickname.png', crop_row4_col2_nickname)
cv2.imwrite('crop_row4_col3_nickname.png', crop_row4_col3_nickname)
cv2.imwrite('crop_row4_col4_nickname.png', crop_row4_col4_nickname)

willReadPictureList = ['crop_row1_col1_nickname.png', 'crop_row1_col2_nickname.png', 'crop_row1_col3_nickname.png',
                       'crop_row1_col4_nickname.png',
                       'crop_row2_col1_nickname.png', 'crop_row2_col2_nickname.png', 'crop_row2_col3_nickname.png',
                       'crop_row2_col4_nickname.png',
                       'crop_row3_col1_nickname.png', 'crop_row3_col2_nickname.png', 'crop_row3_col3_nickname.png',
                       'crop_row3_col4_nickname.png',
                       'crop_row4_col1_nickname.png', 'crop_row4_col2_nickname.png', 'crop_row4_col3_nickname.png',
                       'crop_row4_col4_nickname.png']
print('willReadPictureList.size=', len(willReadPictureList))
img_path = '',
nick_name_list = []
blank_nick_name_count_num = 0

try:
    # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
    # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    for index, tempPic in enumerate(willReadPictureList):
        # 0 - 15
        print("循环遍历index:", index)
        img_path = tempPic
        # 识别昵称图片
        result = ocr.ocr(img_path, cls=True)
        # 0 , 一个昵称，识别以后可能识别出2个结果，只拿第一个
        res = result[0]
        # 如果识别结果不是空的
        if res is not None:
            # 就把图片识别的昵称保存到nick_name_list，并初始值costTimeCount=0
            for line in res:
                print(line)
                nick_name_list.append(dict([('nick_name', line[-1][0]), ('costTimeCount', 0)]))
        # else 处理空白名字
        else:
            nick_name_list.append(dict([('nick_name', '第{}位空白名'.format(index+1)), ('costTimeCount', 0)]))
            blank_nick_name_count_num = blank_nick_name_count_num + 1
            with open('logs/ggd_out.log', 'a') as f:
                print('有空白名字,序号为：', index, file=f)
                print('有空白名字,序号为：', index)

    with open('logs/ggd_out.log', 'a') as f:
        print('初步截{}张图，获取昵称，结束'.format(len(willReadPictureList)), file=f)
        print('初步截{}张图，获取昵称，结束'.format(len(willReadPictureList)))
        print('识别的昵称图片有{}张是空白昵称'.format(blank_nick_name_count_num), file=f)
        print('识别的昵称图片有{}张是空白昵称'.format(blank_nick_name_count_num))

    # 显示结果
    from PIL import Image

    time.sleep(2)

    # 创建Excel
    workbook = openpyxl.Workbook()
    # 选择活动的工作表
    worksheet = workbook.active

    # 设置表头
    headers = ['昵称', '发言耗时权重（数值越高说明发言时间越久）']
    worksheet.append(headers)

    # 3600s
    i = 3600
    while True:
        # if i == 3600: break
        print("获取当前鼠标位置", pyautogui.position())
        with open('logs/ggd_out.log', 'a') as f:
            print('获取当前鼠标位置', pyautogui.position(), file=f)

        # 参数：横坐标、竖坐标，从屏幕左上角开始
        color = pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)
        print("当前鼠标位置RGB颜色参数", color)  # (248, 248, 248) 正确发言框颜色(255, 195, 0) => #FFC300
        with open('logs/ggd_out.log', 'a') as f:
            print('当前鼠标位置RGB颜色参数', color, file=f)
        # x：要检查像素颜色的横坐标。
        # y：要检查像素颜色的纵坐标。
        # expectedColor：一个三元组，表示期望的像素颜色值，以RGB格式表示。例如，(255, 0, 0)表示红色。
        # tolerance（可选）：容忍度，表示颜色匹配的容忍程度。默认值为0，表示完全匹配。
        # 返回值： 返回布尔值，表示指定位置的像素颜色是否与给定颜色匹配。
        # pyautogui.pixelMatchesColor(x, y, expectedColor, tolerance=0)
        # row1_col1 (285, 190)
        row1_col1_point = pyautogui.pixelMatchesColor(285, 190, (255, 195, 0), 0)
        if row1_col1_point:
            nick_name_list[0]['costTimeCount'] = nick_name_list[0].get('costTimeCount') + 1
        # row1_col2 (675, 191)
        row1_col2_point = pyautogui.pixelMatchesColor(675, 190, (255, 195, 0), 0)
        if row1_col2_point:
            nick_name_list[1]['costTimeCount'] = nick_name_list[1].get('costTimeCount') + 1
        # row1_col3 (1090, 192)
        row1_col3_point = pyautogui.pixelMatchesColor(1090, 190, (255, 195, 0), 0)
        if row1_col3_point:
            nick_name_list[2]['costTimeCount'] = nick_name_list[2].get('costTimeCount') + 1
        # row1_col4 (1440, 190)
        row1_col4_point = pyautogui.pixelMatchesColor(1440, 190, (255, 195, 0), 0)
        if row1_col4_point:
            nick_name_list[3]['costTimeCount'] = nick_name_list[3].get('costTimeCount') + 1

        print('第一行：***', row1_col1_point, '***', row1_col2_point, '***', row1_col3_point, '***', row1_col4_point)
        with open('logs/ggd_out.log', 'a') as f:
            print('第一行：***', row1_col1_point, '***', row1_col2_point, '***', row1_col3_point, '***', row1_col4_point,
                  file=f)

        # row2_col1 285, 372
        row2_col1_point = pyautogui.pixelMatchesColor(285, 372, (255, 195, 0), 0)
        if row2_col1_point:
            nick_name_list[4]['costTimeCount'] = nick_name_list[4].get('costTimeCount') + 1
        # row2_col2 675, 372
        row2_col2_point = pyautogui.pixelMatchesColor(675, 372, (255, 195, 0), 0)
        if row2_col2_point:
            nick_name_list[5]['costTimeCount'] = nick_name_list[5].get('costTimeCount') + 1
        # row2_col3 1090, 372
        row2_col3_point = pyautogui.pixelMatchesColor(1090, 372, (255, 195, 0), 0)
        if row2_col3_point:
            nick_name_list[6]['costTimeCount'] = nick_name_list[6].get('costTimeCount') + 1
        # row2_col4 1440, 372
        row2_col4_point = pyautogui.pixelMatchesColor(1440, 372, (255, 195, 0), 0)
        if row2_col4_point:
            nick_name_list[7]['costTimeCount'] = nick_name_list[7].get('costTimeCount') + 1

        print('第二行：***', row2_col1_point, '***', row2_col2_point, '***', row2_col3_point, '***', row2_col4_point)
        with open('logs/ggd_out.log', 'a') as f:
            print('第二行：***', row2_col1_point, '***', row2_col2_point, '***', row2_col3_point, '***', row2_col4_point,
                  file=f)

        # row3_clo1 (285, 553)
        row3_col1_point = pyautogui.pixelMatchesColor(285, 553, (255, 195, 0), 0)
        if row3_col1_point:
            nick_name_list[8]['costTimeCount'] = nick_name_list[8].get('costTimeCount') + 1
        # row3_clo2 (675, 553)
        row3_col2_point = pyautogui.pixelMatchesColor(675, 553, (255, 195, 0), 0)
        if row3_col2_point:
            nick_name_list[9]['costTimeCount'] = nick_name_list[9].get('costTimeCount') + 1
        # row3_col3 (1090, 553)
        row3_col3_point = pyautogui.pixelMatchesColor(1090, 553, (255, 195, 0), 0)
        if row3_col3_point:
            nick_name_list[10]['costTimeCount'] = nick_name_list[10].get('costTimeCount') + 1
        # row3_col4 (1440, 553)
        row3_col4_point = pyautogui.pixelMatchesColor(1440, 553, (255, 195, 0), 0)
        if row3_col4_point:
            nick_name_list[11]['costTimeCount'] = nick_name_list[11].get('costTimeCount') + 1
        print('第三行：***', row3_col1_point, '***', row3_col2_point, '***', row3_col3_point, '***', row3_col4_point)
        with open('logs/ggd_out.log', 'a') as f:
            print('第三行：***', row3_col1_point, '***', row3_col2_point, '***', row3_col3_point, '***', row3_col4_point,
                  file=f)

        # row4_clo1 (285, 735)
        row4_col1_point = pyautogui.pixelMatchesColor(285, 735, (255, 195, 0), 0)
        if row4_col1_point:
            nick_name_list[12]['costTimeCount'] = nick_name_list[12].get('costTimeCount') + 1
        # row4_clo2 (675, 735)
        row4_col2_point = pyautogui.pixelMatchesColor(675, 735, (255, 195, 0), 0)
        if row4_col2_point:
            nick_name_list[13]['costTimeCount'] = nick_name_list[13].get('costTimeCount') + 1
        # row4_col3 (1090, 735)
        row4_col3_point = pyautogui.pixelMatchesColor(1090, 735, (255, 195, 0), 0)
        if row4_col3_point:
            nick_name_list[14]['costTimeCount'] = nick_name_list[14].get('costTimeCount') + 1
        # row4_col4 (1440, 735)
        row4_col4_point = pyautogui.pixelMatchesColor(1440, 735, (255, 195, 0), 0)
        if row4_col4_point:
            nick_name_list[15]['costTimeCount'] = nick_name_list[15].get('costTimeCount') + 1
        print('第四行：***', row4_col1_point, '***', row4_col2_point, '***', row4_col3_point, '***', row4_col4_point)
        with open('logs/ggd_out.log', 'a') as f:
            print('第四行：***', row4_col1_point, '***', row4_col2_point, '***', row4_col3_point, '***', row4_col4_point,
                  file=f)

        i = i - 1
        print(nick_name_list)
        with open('logs/ggd_out.log', 'a') as f:
            print(nick_name_list, file=f)
        # sleep 1 second
        time.sleep(1)
        if i == 0:
            break
except Exception as e:
    # 当其他类型的异常被引发时
    print(f"发生了一个未知异常: {e}")
finally:
    # 遍历数据列表并写入到工作表中
    for row_data in nick_name_list:
        worksheet.append([row_data['nick_name'], row_data['costTimeCount']])
    # 保存工作簿
    # excel_name
    excel_name = 'excel/ggd_example' + str(int(datetime.datetime.now().timestamp())) + '.xlsx'
    workbook.save(excel_name)
