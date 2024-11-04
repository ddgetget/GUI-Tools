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
import gradio as gr

from config import custom_css

# 创建 Gradio Blocks
with gr.Blocks(css=custom_css, title='登陆') as demo:
    gr.Markdown("# 万叶表格示例")
    gr.Markdown("这是一个展示表格数据的示例。")
