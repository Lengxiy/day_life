import pandas as pd

data = pd.read_excel("./整理后结果_获奖结果.xlsx", sheet_name="Sheet2", na_values=['', 0])
#需要被查询的列
stu_names = data["参赛学生姓名"].tolist()
tea_names = data["指导教师"].tolist()
# print(tea_names)

#学生
search_data_stu = pd.read_excel("./原素材/data.xlsx", sheet_name="SJCJ_JW_XSJBXXB-1", na_values=['', 0])
search_stu_name = search_data_stu["姓名"].tolist()#姓名
search_stu_score = search_data_stu["学号"].tolist()#学号

#老师
search_data_tea = pd.read_excel("./原素材/data.xlsx", sheet_name="SJCJ_RS_JSJBXX-1", na_values=['', 0])
search_tea_name = search_data_tea["姓名"].tolist()
search_tea_scor = search_data_tea["工号"].tolist()

#查询对应的教师/学生的工号/学号位置
def find_position(search_string, my_list):
    try:
        position = my_list.index(search_string)
        return position
    except ValueError:
        #数据匹配不到的都设置成：无
        return f"无"

#对教师工号进行补位操作
def buwei(s_int):
    l = len(s_int)
    if l<7:
        while l<7:
            s_int = "0"+s_int
            l = l +1
        return s_int
    return s_int

name_hebing = []#姓名用逗号合并
score_hebing = []#学号用逗号合并

tea_g = "" #教师工号
tea_n = "" #教师姓名
for tea in tea_names:
    # print(tea)
    if pd.notna(tea):
        c = len(tea)
        x = 0   
        y = 0  #前一个字符
        s = ""
        if c == 0:
            continue
        while x<=c:

            if x == c:
                tea_n = tea_n + tea[y:x]
                s = tea[y:x]
                position = find_position(s,search_tea_name)
                if position == "无":
                    tea_g = tea_g + position
                    # n = n + position
                    x = x + 1
                    continue

                tea_g = tea_g + buwei(str(search_tea_scor[position]))

            elif tea[x] == "、":
                s = tea[y:x]
                tea_n = tea_n + tea[y:x]+","
                y = x + 1
                position = find_position(s,search_tea_name)
                if position == "无":
                    tea_g = tea_g + position + ","
                    # n = n + position + ","
                    x = x + 1
                    continue
                tea_g = tea_g + buwei(str(search_tea_scor[position])) + ","

            elif tea[x] == "，":
                s = tea[y:x]
                tea_n = tea_n + tea[y:x]+","
                y = x + 1
                position = find_position(s,search_tea_name)
                if position == "无":
                    tea_g = tea_g + position + ","
                    # n = n + position + ","
                    x = x + 1
                    continue
                tea_g = tea_g + buwei(str(search_tea_scor[position])) + ","

            elif tea[x] == ",":
                s = tea[y:x]
                tea_n = tea_n + tea[y:x]+","
                y = x + 1
                position = find_position(s,search_tea_name)
                if position == "无":
                    tea_g = tea_g + position + ","
                    # n = n + position + ","
                    x = x + 1
                    continue
                tea_g = tea_g + buwei(str(search_tea_scor[position])) + ","

            elif tea[x] == " ":
                pass
            
            s = ""
            x = x+1

        name_hebing.append(tea_n)
        score_hebing.append(tea_g)

        tea_n = ""
        tea_g = ""
    else:
        name_hebing.append("无")
        score_hebing.append("无")

s_name_hebing = []
s_score_hebing = []
stu_g = "" #学生学号
stu_n = "" #学生姓名
for stu in stu_names:
    # print(tea)
    if pd.notna(stu):
        c = len(stu)
        x = 0   
        y = 0  #前一个字符
        s = ""
        if c == 0:
            continue
        while x<=c:

            if x == c:
                stu_n = stu_n + stu[y:x]
                s = stu[y:x]
                position = find_position(s,search_stu_name)
                if position == "无":
                    stu_g = stu_g + position
                    # n = n + position
                    x = x + 1
                    continue

                stu_g = stu_g + buwei(str(search_stu_score[position]))

            elif stu[x] == "、":
                s = stu[y:x]
                stu_n = stu_n + stu[y:x]+","
                y = x + 1
                position = find_position(s,search_stu_name)
                if position == "无":
                    stu_g = stu_g + position + ","
                    # n = n + position + ","
                    x = x + 1
                    continue
                stu_g = stu_g + buwei(str(search_stu_score[position])) + ","

            elif stu[x] == "，":
                s = stu[y:x]
                stu_n = stu_n + stu[y:x]+","
                y = x + 1
                position = find_position(s,search_stu_name)
                if position == "无":
                    stu_g = stu_g + position + ","
                    # n = n + position + ","
                    x = x + 1
                    continue
                stu_g = stu_g + buwei(str(search_stu_score[position])) + ","

            elif stu[x] == ",":
                s = stu[y:x]
                stu_n = stu_n + stu[y:x]+","
                y = x + 1
                position = find_position(s,search_stu_name)
                if position == "无":
                    stu_g = stu_g + position + ","
                    # n = n + position + ","
                    x = x + 1
                    continue
                stu_g = stu_g + buwei(str(search_stu_score[position])) + ","

            s = ""
            x = x+1

        s_name_hebing.append(stu_n)
        s_score_hebing.append(stu_g)

        stu_n = ""
        stu_g = ""
    else:
        s_name_hebing.append("无")
        s_score_hebing.append("无")

result_df = pd.DataFrame({
    '教师姓名': name_hebing,
    '教师工号': score_hebing,
    '学生姓名': s_name_hebing,
    '学生学号': s_score_hebing
})

# 将数据框写入新的Excel文件
print("完成")
result_df.to_excel('output_result.xlsx', index=False)


    


