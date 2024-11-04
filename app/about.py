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

import gradio as gr

from config import custom_css

io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox", title='打招呼', css=custom_css,
                  description="这是一个示例应用，用于演示如何在Gradio中设置本地Favicon。", )
