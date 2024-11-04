# -*- coding: utf-8 -*-
# @Time:    2024-11-04 21:11
# @Author:  Herbert·Simon
# @Email:   yonglonggeng@163.com
# @WeChat:  ddgetget
# @File:    run.py
# @Project: GUI-Tools
# @Package: 
# @Ref:     just do it for yourself!
import os

import gradio as gr
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse, JSONResponse, FileResponse
from starlette.staticfiles import StaticFiles

from app.about import io
from app.chatbot.example.chatbot_examples.chatbot_examples import chatbot_examples
from app.demo import demo
from app.plot.bokeh_plot import bokeh_plot_app
from config import html_content

load_dotenv()
ico_path = os.environ.get("ico")

app = FastAPI()
# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 模拟数据
data = [
    {"id": 1, "app": "Alice", "des": "啥的健康", "link": "/gradio"},
    {"id": 2, "app": "demo", "des": "样例调试", "link": "/demo"},
    {"id": 3, "app": "chatbot_examples", "des": "sdad", "link": "/chatbot/examples"},
    {"id": 4, "app": "bokeh_plot_app", "des": "sdad", "link": "/bokeh/plot_app"},
    {"id": 3, "app": "agent_chatbot", "des": "sdad", "link": "/agent/chatbot"},
    {"id": 3, "app": "agent_chatbot", "des": "sdad", "link": "/agent/chatbot"},
    {"id": 3, "app": "agent_chatbot", "des": "sdad", "link": "/agent/chatbot"},
    {"id": 3, "app": "agent_chatbot", "des": "sdad", "link": "/agent/chatbot"},

]


@app.get("/data", response_class=JSONResponse)
async def get_data():
    return data


# 提供Favicon文件
@app.get('/avatar.png')
async def favicon():
    return FileResponse(ico_path)


# 提供Favicon文件
@app.get('/avatar.ico')
async def file_favicon():
    return FileResponse("static/avatar.png")


@app.get("/contents", response_class=HTMLResponse)
async def read_root(request: Request):
    return HTMLResponse(content=html_content, status_code=200)


app = gr.mount_gradio_app(app, io, path="/gradio")
app = gr.mount_gradio_app(app, demo, path="/demo")
app = gr.mount_gradio_app(app, chatbot_examples, path="/chatbot/examples")
app = gr.mount_gradio_app(app, bokeh_plot_app, path="/bokeh/plot_app")
