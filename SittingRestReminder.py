
import time
import base64
import schedule
import datetime
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
from img_2_py import exercise_img_png, sitting_img_png

def base64img(img_base64):
    """
    为了避免调用外部图片，这里将所需图片提前编码存放至PY文件中，主程序运行时通过本函数直接调用
    将编码后的图片解码为图片格式
    :param img_base64: 编码后的图片
    :return:
    """
    img_data = base64.b64decode(img_base64)
    image = Image.open(BytesIO(img_data))
    # image.show()
    return image


def sitting_remind():
    """
    每sitting_remind_time分钟提醒一下坐姿
    """
    print('sitting_remind执行时间：{0}'.format(datetime.datetime.now()))
    main_gui = tk.Tk()
    main_gui.title('坐姿提醒')
    main_gui.resizable(1, 1)
    windows_w = 700
    windows_h = 400
    # 在屏幕中心显示窗口
    screen_w = main_gui.winfo_screenwidth()
    screen_h = main_gui.winfo_screenheight()
    x, y = int((screen_w -windows_w)/2), int((screen_h -windows_h)/2)
    main_gui.geometry('{0}x{1}+{2}+{3}'.format(windows_w, windows_h, x, y))
    # 直接打开图片
    # img = tk.PhotoImage(file='sitting_img.png')
    # 采用将图片转成base64的方式 再打开图片
    img = ImageTk.PhotoImage(base64img(sitting_img_png))
    label = tk.Label(main_gui, image=img, text='请注意调整你的坐姿！\n 极端挺直情况下减少10%是良好的坐姿！\n 窗口10s后自动退出',
                     compound='bottom', font=("微软雅黑", 20, 'bold'))
    label.pack()
    main_gui.attributes('-toolwindow', True,
                    '-alpha', 1,
                    '-fullscreen', True,
                    '-topmost', True)
    main_gui.overrideredirect(True)
    # 5S后自动退出
    main_gui.after(10*1000, main_gui.destroy)
    main_gui.mainloop()


def rest_remind():
    """
    每rest_remind_time分钟提醒一下休息
    """
    print('rest_remind执行时间：{0}'.format(datetime.datetime.now()))
    main_gui = tk.Tk()
    main_gui.title('休息提醒')
    main_gui.resizable(1, 1)
    # 最大化窗口
    # screen_w = main_gui.winfo_screenwidth()
    # screen_h = main_gui.winfo_screenheight()
    # main_gui.geometry('{0}x{1}'.format(screen_w, screen_h))
    # img = tk.PhotoImage(file='exercise_img.png'),
    img = ImageTk.PhotoImage(base64img(exercise_img_png))
    label_1 = tk.Label(main_gui, image=img, text='1. 麦肯基背部训练(10次)',
                       compound='bottom', font=("微软雅黑", 20, 'bold'))
    label_2 = tk.Label(main_gui, text='1)两腿分开站直，双手放在后腰部，四指靠在脊椎两侧。\n 2)躯干尽量向后弯曲，使用双手做为支撑点。\n'
                                     '3)重复进行10次。',
                       font=("微软雅黑", 16, 'bold'))
    label_3 = tk.Label(main_gui, text='2. 走动一下，去喝喝水', font=("微软雅黑", 20, 'bold'))
    label_4 = tk.Label(main_gui, text='3. 倒计时结束，窗口自动关闭', font=("微软雅黑", 20, 'bold'))
    label_var = tk.StringVar()
    label_5 = tk.Label(main_gui, textvariable=label_var, fg='red', font=("微软雅黑", 25, 'bold'))
    label_1.pack()
    label_2.pack()
    label_3.pack()
    label_4.pack()
    label_5.pack()
    # 设置
    main_gui.attributes('-toolwindow', True,  # True 只有退出按钮，也没有图标；False 正常的窗体样式
                    '-alpha', 1,
                    '-fullscreen', True,  # True 全屏；False 正常显示
                    '-topmost', True)  # True 所有窗口中处于最顶层
    # True 没有工具栏按钮；False 正常显示
    main_gui.overrideredirect(True)
    # 5分钟后自动退出
    counter = 5 * 60
    while counter:
        counter -= 1
        label_var.set(str(counter))
        label_5.update()
        time.sleep(1)

    main_gui.after(1000, main_gui.destroy)
    main_gui.mainloop()


if __name__ == '__main__':
    # 主函数采用定时执行
    sitting_remind_time = 10
    rest_remind_time = 40
    schedule.every(sitting_remind_time).minutes.do(sitting_remind)
    schedule.every(rest_remind_time).minutes.do(rest_remind)
    print('主程序运行：{0}'.format(datetime.datetime.now()))
    while True:
        # 运行所有可以运行的任务
        schedule.run_pending()
        time.sleep(1)
