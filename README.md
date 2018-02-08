# bilibili-index-icon
自动随机读取哔哩哔哩主页索引旁的动图。

**编辑时间**
2018年2月8日19:19:04 - 2018年2月8日20:32:11

---
# 思路
访问api页面，提取内容并保存至`icon.txt` 。
# api页面详情
**Url** https://api.bilibili.com/x/web-interface/index/icon
**请求方式** Get
**页面例子**
```json
{"code":0,"message":"0","ttl":1,"data":{"id":302,"title":"监狱兔","links":["http://search.bilibili.com/all?keyword=%E7%9B%91%E7%8B%B1%E5%85%94"],"icon":"//i0.hdslb.com/bfs/active/ba090ff3b9bccb7d0b2f383012a74217c0ff8c33.gif","weight":0}}
{
    "code":0,
    "message":"0",
    "ttl":1,
    "data":{
        "id":302,
        "title":"监狱兔",
        "links":[
            "http://search.bilibili.com/all?keyword=%E7%9B%91%E7%8B%B1%E5%85%94"
        ],
        "icon":"//i0.hdslb.com/bfs/active/ba090ff3b9bccb7d0b2f383012a74217c0ff8c33.gif",
        "weight":0
    }
}

{"code":0,"message":"0","ttl":1,"data":{"id":952,"title":"幽灵","links":["http://search.bilibili.com/all?keyword=%E5%B9%BD%E7%81%B5"],"icon":"//i0.hdslb.com/bfs/active/02b8b884e435959ec1714ca68168235bc9fe98f4.gif","weight":0}}
{
    "code":0,
    "message":"0",
    "ttl":1,
    "data":{
        "id":952,
        "title":"幽灵",
        "links":[
            "http://search.bilibili.com/all?keyword=%E5%B9%BD%E7%81%B5"
        ],
        "icon":"//i0.hdslb.com/bfs/active/02b8b884e435959ec1714ca68168235bc9fe98f4.gif",
        "weight":0
    }
}

{"code":0,"message":"0","ttl":1,"data":{"id":416,"title":"在下坂本，有何贵干？","links":["http://bangumi.bilibili.com/anime/3450"],"icon":"//i0.hdslb.com/bfs/active/9b625a77be6058aac7f952298da0078a0780cd09.gif","weight":0}}
{
    "code":0,
    "message":"0",
    "ttl":1,
    "data":{
        "id":416,
        "title":"在下坂本，有何贵干？",
        "links":[
            "http://bangumi.bilibili.com/anime/3450"
        ],
        "icon":"//i0.hdslb.com/bfs/active/9b625a77be6058aac7f952298da0078a0780cd09.gif",
        "weight":0
    }
}
```
| Key | 描述 |
| :-----: | :-----------------------: |
| code | 返回状态码 |
| message | 直译为`消息` ，用途未知 |
| ttl | 疑似为`Time To Live`的缩写，用途未知 |
| data | 数据 |
| id | 识别码 |
| title | 标题 |
| links | 点击图片后访问链接 |
| icon | 动态图片链接 |
| weight | 直译为`重量` ，用途未知 |

# Python代码

导入模块

```python
import requests
import json
from io import StringIO
import time
```
正式代码
```python
IG = requests.get('https://api.bilibili.com/x/web-interface/index/icon') # 定义访问链接(IconGet)
io = StringIO(IG.text)  # 提取文本，并转换为json格式
print('标题|',json.load(io)["data"]["title"],) # 提取标题
io = StringIO(IG.text)  # 提取文本，并转换为json格式(此处不知为何需要再次提取。)
print('图片Url|',json.load(io)["data"]["icon"]) # 提取图片Url
```
