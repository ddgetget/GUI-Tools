# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2024-10-31 18:29:04
@Author  :   simon
@Version :   1.0
@Contact :   yonglonggeng@163.com
@License :   (C)Copyright 1994-2024, Liugroup-NLPR-CASIA
@Desc    :   
@WeChat  :   Herbert·Simon
'''

# here put the import lib
import tkinter as tk
# from home_page import create_home_page
# from discover_page import create_discover_page
# from library_page import create_library_page
# from profile_page import create_profile_page

from app.about import create_about_page
from app.button_page import create_button_page
from app.tab_page import create_tab_page
from app.demo import create_demo_page


def show_frame(frame, title):
    """ 显示指定的框架，并隐藏其他所有框架，同时更新窗口标题。"""
    for f in frames.values():
        if f == frame:
            f.pack(fill='both', expand=True)
        else:
            f.pack_forget()
    # 更新窗口标题
    root.title(f"网易云音乐 - {title}")


# 创建主窗口
root = tk.Tk()
root.title("网易云音乐")
root.geometry("800x600")  # 设置窗口大小

# 创建侧边菜单栏
menu_frame = tk.Frame(root, width=200, bg="lightgray")
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

# 创建按钮并添加到侧边菜单栏
side_buttons = ["主页", "发现", "我的音乐库", "个人资料"]
for btn_text in side_buttons:
    button = tk.Button(menu_frame, text=btn_text,
                       command=lambda b=btn_text: show_frame(frames[b], b))
    button.pack(fill=tk.X, pady=5)

# 创建顶部菜单栏
top_menu = tk.Menu(root)
root.config(menu=top_menu)

# 添加顶部菜单项
file_menu = tk.Menu(top_menu, tearoff=False)
top_menu.add_cascade(label="导航", menu=file_menu)
for btn_text in side_buttons:
    file_menu.add_command(
        label=btn_text, command=lambda b=btn_text: show_frame(frames[b], b))

# 定义各个页面
frames = {
    "主页": create_demo_page(root),
    "发现": create_about_page(root),
    "我的音乐库": create_button_page(root),
    "个人资料": create_tab_page(root)
}

# 默认显示第一个页面
show_frame(frames[side_buttons[0]], side_buttons[0])

# 运行主循环
root.mainloop()
