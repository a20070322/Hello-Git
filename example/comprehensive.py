# 学生信息案例需求拆分
"""
学生信息管理系统
1. 增加学生信息
2. 删除学生信息
3. 修改学生信息
4. 查询学生信息
5. 退出系统
"""
# 数据结构分析
"""
学生信息：姓名，年龄，性别，学号，爱好，绩效
学生信息列表: [学生信息1,学生信息2,学生信息3]
"""
student_list = [
    {
        "name": "张三",
        "age": 18,
        "sex": "男",
        "id": 1001,
        "hobby": "足球",
        "score": 90
    },
    {
        "name": "李四",
        "age": 19,
        "sex": "男",
        "id": 1002,
        "hobby": "篮球",
        "score": 80
    }
]


# 实现列表打印，以下为打印示例
# ========= 用户信息列表 ==========
# 姓名：张三
# 年龄：18
# 性别：18
# 学号：1001
# 爱好：足球
# 绩效：90
# =================================
# 姓名：李四
# 年龄：19
# 性别：19
# 学号：1002
# 爱好：篮球
# 绩效：80
# =================================
def get_student_list(data):
    print('========= 用户信息列表 ==========')
    for item in data:
        print('姓名：'+item.get("name"))
        print('年龄：'+str(item.get("age")))
        print('性别：'+str(item.get("age")))
        print('学号：'+str(item.get("id")))
        print('爱好：'+str(item.get("hobby")))
        print('绩效：'+str(item.get("score")))
        print('=================================')


# get_student_list(student_list)


# 实现通过姓名查询学生信息
# find_student_by_name(student_list, '张三')
def find_student_by_name(data, name):
    for i in range(len(data)):
        if data[i].get("name") == name:
            return {
                "info": data[i],
                "index": i
            }
    return {
        "info": None,
        "index": -1
    }


# result = find_student_by_name(student_list, '李四')
# print(result)


# 实现添加学生信息
def add_student(data):
    info = {}
    info['name'] = input("请输入学生姓名：")
    info['age'] = int(input("请输入学生年龄："))
    info['sex'] = input("请输入学生性别：")
    info['id'] = int(input("请输入学生学号："))
    info['hobby'] = input("请输入学生爱好：")
    info['score'] = int(input("请输入学生成绩："))
    data.append(info)
    print("添加成功")


# add_student(student_list)
# get_student_list(student_list)


# 实现根据学生姓名删除学生信息
def delete_student(data, name):
    result = find_student_by_name(data, name)
    if result.get("info") is None:
        print("未找到该学生")
    else:
        data.pop(result.get("index"))
        print("删除成功")


# delete_student(student_list, '李四')
# get_student_list(student_list)


def update_student(data, name):
    result = find_student_by_name(data, name)
    if result.get("info") is None:
        print("未找到该学生")
        return
    info = result.get("info")
    print("如果字段无需修改 可直接回车")
    name = input("学生姓名：")
    if name != "":
        info['name'] = name

    age = input("学生年龄：")
    if age != "":
        info['age'] = int(age)
    sex = input("学生性别：")
    if sex != "":
        info['sex'] = sex
    student_id = input("学生学号：")
    if student_id != "":
        info['id'] = int(student_id)
    hobby = input("学生爱好：")
    if hobby != "":
        info['hobby'] = hobby
    score = input("学生成绩：")
    if score != "":
        info['score'] = int(score)
    # 可以简写为以下代码
    # info['name'] = input("学生姓名：") or info['name']
    data[result.get("index")] = info


# update_student(student_list, '李四')
# get_student_list(student_list)


# 通过循环 实现学生信息管理系统
while True:
    print("=========学生信息管理系统=========")
    print("1. 增加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 退出系统")
    choice = int(input("请输入您的选择："))
    if choice == 1:
        add_student(student_list)
    elif choice == 2:
        name = input("请输入要删除的学生姓名：")
        delete_student(student_list, name)
    elif choice == 3:
        name = input("请输入要修改的学生姓名：")
        update_student(student_list, name)
    elif choice == 4:
        get_student_list(student_list)
    elif choice == 5:
        print("欢迎再次使用")
        break
    else:
        print("输入有误，请重新输入")
    print("")
    print("")