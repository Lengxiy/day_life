import requests
import urllib
import os
import re
# 打开txt文件
file = open("source_code.txt", "r")

# 创建两个空列表，用于存储ATTACHNAME和ATTACHPATH的内容
attachname_list = []
attachpath_list = []

# 逐行读取文件中的数据
for line in file:
    # 获取前10个字符
    first_10_chars = line[1:11]
    # 如果前10个字符是"ATTACHNAME"，则把冒号后面的内容去掉引号后添加到attachname_list中
    if first_10_chars == "ATTACHNAME":
        attachname = line.split(":")[1].strip().strip('"')
        attachname_list.append(attachname)
    # 如果前10个字符是"ATTACHPATH"，则把冒号后面的内容去掉引号后添加到attachpath_list中
    elif first_10_chars == "ATTACHPATH":
        attachpath = line.split(":")[1].strip().strip('"')
        attachpath_list.append(attachpath)

# 关闭文件
file.close()

# # 打印结果
# print("attachname_list:", attachname_list)
# print("attachpath_list:", attachpath_list)
# print(len(attachpath_list))

new_list = [x.strip('"') for x in attachpath_list]
new_list1 = []
for x in attachname_list:
    new_list1.append(x[:-2])

x = 0
for i in new_list:

    url = "https://dingtalk.zjedu.gov.cn/"
    finall = url + i
    chang = len(finall)
    if chang == 82:
        finall = finall[:75] + "_docx.pdf"
    if chang == 81:
        finall = finall[:75] + "_doc.pdf"

    name = new_list1[x]
    x = x+1
    # 定义保存 PDF 文件的路径
    save_path = 'C:\\Users\\23728\\Desktop\\pdf'
    
    response = requests.get(finall).content
    # 获取 PDF 文件的名称
    pdf_name = name
    # 保存 PDF 文件到本地
    with open(save_path + '\\' + pdf_name + ".pdf", 'wb') as f:
        f.write(response)
    print(f'文件 {pdf_name} 已下载成功！')
