# -*- encoding: utf-8 -*-
'''
@File    :   tab_page.py
@Time    :   2024-10-31 18:32:07
@Author  :   simon
@Version :   1.0
@Contact :   yonglonggeng@163.com
@License :   (C)Copyright 1994-2024, Liugroup-NLPR-CASIA
@Desc    :   
@WeChat  :   Herbert·Simon
'''

# here put the import lib
import tkinter as tk
from tkinter import ttk


def create_tab_page(parent):
    frame = tk.Frame(parent, borderwidth=2, relief=tk.SUNKEN)

    # 创建 Notebook 用于管理多个标签页
    notebook = ttk.Notebook(frame)
    notebook.pack(fill='both', expand=True)

    # 公共参数
    shared_text = tk.StringVar(value="初始文本")
    shared_number = tk.IntVar(value=0)

    # 创建第一个标签页
    tab1 = ttk.Frame(notebook)
    label1 = tk.Label(tab1, text="播放列表:")
    entry1 = tk.Entry(tab1, textvariable=shared_text)
    spinbox1 = tk.Spinbox(tab1, from_=0, to=100, textvariable=shared_number)
    label1.pack(padx=10, pady=10)
    entry1.pack(padx=10, pady=10)
    spinbox1.pack(padx=10, pady=10)
    notebook.add(tab1, text="播放列表")

    # 创建第二个标签页
    tab2 = ttk.Frame(notebook)
    label2 = tk.Label(tab2, text="收藏夹:")
    entry2 = tk.Entry(tab2, textvariable=shared_text)
    spinbox2 = tk.Spinbox(tab2, from_=0, to=100, textvariable=shared_number)
    label2.pack(padx=10, pady=10)
    entry2.pack(padx=10, pady=10)
    spinbox2.pack(padx=10, pady=10)
    notebook.add(tab2, text="收藏夹")

    # 创建第三个标签页
    tab3 = ttk.Frame(notebook)
    label3 = tk.Label(tab3, text="最近播放:")
    entry3 = tk.Entry(tab3, textvariable=shared_text)
    spinbox3 = tk.Spinbox(tab3, from_=0, to=100, textvariable=shared_number)
    label3.pack(padx=10, pady=10)
    entry3.pack(padx=10, pady=10)
    spinbox3.pack(padx=10, pady=10)
    notebook.add(tab3, text="最近播放")

    return frame
