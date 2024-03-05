import requests
import time
# 打开txt文件
file = open("1.txt", "r", encoding="utf-8")

non_jpg = [line.split("/")[-1].strip("\n\t") for line in file]

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}

x = 0
for i in non_jpg:

    url = "http://cdn.sneducloud.com/file/upload/202402/26/002/"
    finall = url + i
    name = i[:-4]
    x = x+1
    # 定义保存 PDF 文件的路径
    save_path = 'C:\\Users\\23728\\Desktop\\pdf'

    response = requests.get(finall).content
    # 获取 jpg 文件的名称
    pdf_name = name
    # 保存 jpg 文件到本地
    with open(save_path + '\\' + pdf_name + ".jpg", 'wb') as f:
        f.write(response)
    print(f'文件 {pdf_name} 已下载成功！剩余{len(non_jpg)-x}个')