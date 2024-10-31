# -*- encoding: utf-8 -*-
'''
@File    :   demo.py
@Time    :   2024-10-31 18:34:12
@Author  :   simon
@Version :   1.0
@Contact :   yonglonggeng@163.com
@License :   (C)Copyright 1994-2024, Liugroup-NLPR-CASIA
@Desc    :   
@WeChat  :   Herbert·Simon
'''

# here put the import lib
import tkinter as tk


def create_demo_page(parent):
    frame = tk.Frame(parent, borderwidth=2, relief=tk.SUNKEN)
    label = tk.Label(frame, text="这是主页页面")
    label.pack(padx=10, pady=10)
    return frame
