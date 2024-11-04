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

# 创建Gradio Blocks布局
with gr.Blocks(css=custom_css) as demo:
    with gr.Row():
        with gr.Column():
            gr.Markdown("## App 1")
            input_text1 = gr.Textbox(label="Input Text")
            output_text1 = gr.Textbox(label="Output Text")
            btn1 = gr.Button("Submit")


        with gr.Column():
            gr.Markdown("## App 2")
            input_text2 = gr.Textbox(label="Input Text")
            output_text2 = gr.Textbox(label="Output Text")
            btn2 = gr.Button("Submit")


    # 加载本地图片
    with gr.Row():
        gr.Markdown("## Local Image")
        image = gr.Image(value="local_image.jpg", label="Local Image")
