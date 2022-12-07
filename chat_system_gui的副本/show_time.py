import time
import datetime
import tkinter as tk
from time import strftime

while False:
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    current_second = now.strftime("%S")
    print(f"\033cClock: {current_time}\nSeconds: {current_second}")
    time.sleep(1)


def show_realtime_clock():
    # 创建一个窗口
    window = tk.Tk()

    # 设置窗口标题
    window.title("实时时间")

    # 创建一个标签，用于显示时间
    time_label = tk.Label(window, text="")
    time_label.pack()

    # 定义一个函数，用于更新时间
    def update_time():
        current_time = strftime("%H:%M:%S")
        time_label.configure(text=current_time)
        window.after(1000, update_time)

    # 每隔 1 秒更新一次时间
    update_time()

    # 运行主窗口
    window.mainloop()

#


class ClockWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text="")
        self.label.pack()

    def update_time(self):
        now = datetime.datetime.now()
        self.label.configure(text=now.strftime("%Y-%m-%d %H:%M:%S"))
        self.after(1000, self.update_time)

if __name__ == "__main__":
    window = ClockWindow()
    window.update_time()
    window.mainloop()

