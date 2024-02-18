import requests
import json

num = 1 # 从第一页开始
url = "https://dingtalk.zjedu.gov.cn/oa2016/project/meetingmaterials/meetingMaterials/fileList?fileType=100&PageNumber={}&PageSize=10"

ATTACHPATH = []
ATTACHNAME = []

while True: # 无限循环
    a = requests.get(url=url.format(num)) # 发送请求，用 format 方法来替换 url 中的占位符
    data = json.loads(a.text) # 解析响应的文本为 json 对象

    FileList = data['FileList']
    for i in FileList:
        ATTACHPATH.append(i['ATTACHPATH'])
        ATTACHNAME.append(i['ATTACHNAME'])

    if len(FileList) == 0: # 如果数据的长度为零，说明没有更多数据了
        break # 跳出循环
    # print(data) # 打印数据
    num += 1 # 增加页数

print(ATTACHPATH,ATTACHNAME)
