import pandas as pd

data = pd.read_excel("./20231001--20231010工管进出.xlsx")  #将文件放在同一个目录下然后修改文件名称即可使用

#按照姓名和时间排序，升序
print("正在转换数据格式，请稍后------")
data = data.sort_values(by=["人员姓名","事件时间"], ascending=True)
data['所属组织'] = data['所属组织'].str.extract('([^/]+$)', expand=True) #提取班级

names = data['人员姓名']
clas = data['所属组织']
xuehaos = data['工号'].str.replace("'","")   #用replace方法去除多余的 '' 符号
doors = data['门禁点'].str.slice(0,1)  #取出门禁的第一个字符，是东门还是西门
in_out = data['出/入']
str_times = data['事件时间']  #文本格式
date_times = pd.to_datetime(data['事件时间'])   #时间戳格式

x = 0
names_save = []
all_content = []
in_time = []
out_time = []
clas_name = []

print("正在筛选数据------")

while x<len(data)-1:  #行数判断
    if names[x] == names[x+1]:  #先判断姓名是否一致，不一致则跳过
        if doors[x] == doors[x+1]:
            x = x + 1
            continue
        else:
            if in_out[x] == in_out[x+1]:
                x = x + 1
                continue

            #判断时间
            time = (date_times[x] - date_times[x+1]).total_seconds()
            if abs(time) > 5 and abs(time) < 120:
                all_content.append(xuehaos[x])  #学号
                names_save.append(names[x])     #姓名
                out_time.append(date_times[x])  #出门时间
                in_time.append(date_times[x+1]) #进门时间
                clas_name.append(clas[x])       #班级

            x = x + 2
    else:
        x = x + 1

print("数据筛选完成，正在写入到新的数据表---")

# 将列表转换成DataFrame对象
df = pd.DataFrame({"姓名": names_save,"学号": all_content, "班级": clas_name, "出门时间": out_time, "入门时间": in_time})
# 将DataFrame对象写入到Excel文件中
df.to_excel("进出时间筛选.xlsx", sheet_name="data", index=False)
print("任务完成")
