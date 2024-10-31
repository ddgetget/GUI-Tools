# -*- encoding: utf-8 -*-
'''
@File    :   button_page.py
@Time    :   2024-10-31 18:32:41
@Author  :   simon
@Version :   1.0
@Contact :   yonglonggeng@163.com
@License :   (C)Copyright 1994-2024, Liugroup-NLPR-CASIA
@Desc    :   
@WeChat  :   Herbert·Simon
'''

# here put the import lib
import tkinter as tk
from tkinter import PhotoImage


def create_button_page(parent):
    frame = tk.Frame(parent, borderwidth=2, relief=tk.SUNKEN)

    # 加载两张图片
    image1 = PhotoImage(file="image1.png")
    image2 = PhotoImage(file="image2.png")

    # 创建一个变量来跟踪当前显示的图片
    current_image = image1

    # 定义按钮点击事件
    def on_button_click(event):
        nonlocal current_image  # 使用 nonlocal 关键字访问外部函数中的变量
        if current_image == image1:
            current_image = image2
        else:
            current_image = image1
        canvas.itemconfig(image_item, image=current_image)  # 更新 Canvas 上的图片

    # 创建一个 Canvas 来绘制圆角矩形和放置图片
    canvas = tk.Canvas(frame, width=image1.width(),
                       height=image1.height(), highlightthickness=0)
    canvas.pack(pady=20)

    # 在 Canvas 上绘制圆角矩形
    radius = 20  # 圆角半径
    x1, y1 = 0, 0
    x2, y2 = image1.width(), image1.height()
    canvas.create_rounded_rectangle(
        x1, y1, x2, y2, radius, fill="white", outline="gray")

    # 在 Canvas 上放置初始图片
    image_item = canvas.create_image(0, 0, anchor=tk.NW, image=current_image)

    # 绑定点击事件到 Canvas
    canvas.bind("<Button-1>", on_button_click)

    return frame

# 辅助函数：在 Canvas 上绘制圆角矩形


def _create_rounded_rectangle(self, x1, y1, x2, y2, r, **kwargs):
    points = [x1+r, y1,
              x1+r, y1,
              x2-r, y1,
              x2-r, y1,
              x2, y1,
              x2, y1+r,
              x2, y1+r,
              x2, y2-r,
              x2, y2-r,
              x2, y2,
              x2-r, y2,
              x2-r, y2,
              x1+r, y2,
              x1+r, y2,
              x1, y2,
              x1, y2-r,
              x1, y2-r,
              x1, y1+r,
              x1, y1+r,
              x1, y1]
    return self.create_polygon(points, **kwargs, smooth=True)


# 为 Canvas 添加创建圆角矩形的方法
tk.Canvas.create_rounded_rectangle = _create_rounded_rectangle
