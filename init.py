# -*- coding: utf-8 -*-
# @Time:    2024-11-04 22:33
# @Author:  Herbert·Simon
# @Email:   yonglonggeng@163.com
# @WeChat:  ddgetget
# @File:    init.py
# @Project: GUI-Tools
# @Package: 
# @Ref:     just do it for yourself!
def writ_env():
    with open('.env', 'w') as file:
        # 写入指定内容
        file.write('ico = "static/10pbr-f4sot-001.ico"\n')
    print(".env 文件创建并写入成功。")


def load_env():
    from dotenv import load_dotenv
    import os

    # 加载 .env 文件中的环境变量
    load_dotenv()
    print(os.environ.get("ico"))


if __name__ == '__main__':
    writ_env()
    load_env()
