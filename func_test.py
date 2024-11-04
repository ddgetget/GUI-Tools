# -*- coding: utf-8 -*-
# @Time:    2024-11-04 22:27
# @Author:  Herbert·Simon
# @Email:   yonglonggeng@163.com
# @WeChat:  ddgetget
# @File:    func_test.py
# @Project: GUI-Tools
# @Package: 
# @Ref:     just do it for yourself!
import gradio as gr

def greet(name):
    return f"Hello {name}!"

# 自定义HTML头信息
custom_css = """
<link rel="icon" href="https://example.com/path/to/favicon.ico" type="image/x-icon">
"""

custom_css = """
<link rel="icon" href="https://example.com/path/to/favicon.ico" type="image/x-icon">
"""

iface = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="Greeting App",
    description="这是一个示例应用，用于演示如何在Gradio中设置Favicon。",
    css=custom_css
)

iface.launch()