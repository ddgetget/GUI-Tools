# -*- coding: utf-8 -*-
# @Time:    2024-11-04 21:11
# @Author:  Herbert·Simon
# @Email:   yonglonggeng@163.com
# @WeChat:  ddgetget
# @File:    main.py
# @Project: GUI-Tools
# @Package: 
# @Ref:     just do it for yourself!
import uvicorn
from run import app

if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=8000, reload=True, workers=1)
    # uvicorn.run('run:app', host='0.0.0.0', port=8000, reload=False, workers=1)
