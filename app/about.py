# -*- encoding: utf-8 -*-
'''
@File    :   about.py
@Time    :   2024-10-31 18:31:32
@Author  :   simon
@Version :   1.0
@Contact :   yonglonggeng@163.com
@License :   (C)Copyright 1994-2024, Liugroup-NLPR-CASIA
@Desc    :   
@WeChat  :   Herbert·Simon
'''

# here put the import lib
import tkinter as tk


def create_about_page(parent):
    frame = tk.Frame(parent, borderwidth=2, relief=tk.SUNKEN)
    label = tk.Label(frame, text="这是个人资料页面")
    label.pack(padx=10, pady=10)
    return frame
