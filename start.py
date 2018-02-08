# 编辑时间
# 2018年2月8日19:37:18 - 2018年2月8日20:01:03 基本框架完成，提取json部分提示 TypeError: string indices must be integers 错误。
# 2018年2月8日20:04:04 - 2018年2月8日20:32:19 修复提取错误的问题。
#---
import requests
import json
from io import StringIO
import time

IG = requests.get('https://api.bilibili.com/x/web-interface/index/icon') # 定义访问链接(IconGet)
io = StringIO(IG.text)  # 提取文本，并转换为json格式
print('标题|',json.load(io)["data"]["title"],) # 提取标题
io = StringIO(IG.text)  # 提取文本，并转换为json格式(此处不知为何需要再次提取。)
print('图片Url|',json.load(io)["data"]["icon"]) # 提取图片Url