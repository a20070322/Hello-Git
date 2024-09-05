import json

fields = ["name", "age", "sex", "student_num", "hobby", "GPA"]
data_dict = {
    "name": {
        "title": "姓名",
    },
    "age": {
        "title": "年龄"
    },
    "sex": {
        "title": "性别"
    },
    "student_num": {
        "title": "学号"
    },
    "hobby": {
        "title": "爱好"
    },
    "GPA": {
        "title": "绩点"
    },
}


# 获取持久化存储数据
def get_json_data(file_path):
    try:
        # 尝试打开并读取JSON文件
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        # 默认数据
        data = {
            "list": []
        }
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)
    return data


# 数据同步持久化存储
def sync_json_data(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)


# 打印学生信息
def print_student(title, info):
    print("=========== " + title + " ==============")
    for field in fields:
        print(data_dict[field]['title'] + ":" + info[field]
              )
    print("=========== 学生信息结束 ==============")


# 添加学生信息
def student_add(data):
    info = {}
    for field in fields:
        answer = input("请输入" + data_dict[field]['title'] + "\n")
        info[field] = answer
    data['list'].append(info)
    print("log:student_add:=>>> 学生信息添加成功")
    print_student('学生信息添加', info)


# 查找指定元素在列表中出现的下标
def find_element(lst, val, key=False):
    for i in range(len(lst)):
        if key:
            if lst[i][key] == val:
                return i
        else:
            if lst[i] == val:
                return i
    return -1


# 编辑学生信息
def student_edit(data):
    answer = input("请输入要编辑学生信息的姓名\n")
    idx = find_element(data['list'], answer, "name")
    if idx < 0:
        print("未找到=== " + answer + "==此学生信息")
        return
    info = data['list'][idx]
    print_student('查询修改学生信息', info)
    print("请选择要修改的属性")
    for index, field in enumerate(fields):
        print(str((index + 1)) + '.编辑' + data_dict[field]['title'])
    index = input("请输入要修改的信息\n")
    try:
        key = fields[int(index) - 1]
    except IndexError:
        print('err:student_add:=>>> 请输入正确参数')
        return
    value = input("请输入" + data_dict[key]['title'] + "修改后的值\n")
    info[key] = value
    data['list'][idx] = info
    print("log:student_add:=>>> 学生信息修改成功")
    print_student('学生信息修改', info)


# 删除学生信息
def student_del(data):
    answer = input("请输入要删除学生信息的姓名\n")
    idx = find_element(data['list'], answer, "name")
    if idx < 0:
        print("未找到=== " + answer + "==此学生信息")
        return
    info = data['list'][idx]
    del data['list'][idx]
    print("log:student_del:=>>> 学生信息删除成功")
    print_student('学生信息删除', info)


def student_find(data):
    answer = input("请输入要查询学生信息的姓名\n")
    idx = find_element(data['list'], answer, "name")
    if idx < 0:
        print("未找到=== " + answer + "==此学生信息")
        return
    info = data['list'][idx]
    print("log:student_find:=>>> 学生信息查询成功")
    print_student('学生信息查询', info)


def student_list(data):
    print("请选择正确的排序类型")
    print("1. 默认排序(创建时间)")
    print("2. 年龄排序")
    print("3. 学号排序")
    print("4. 绩点排序")
    sort_choice = input("请选择：\n")
    if find_element(["1", "2", "3", "4"], sort_choice) < 0:
        print("log:student_list:=>>> 请选择正确的排序类型")
        return
    if sort_choice == "1":
        result = data['list']
    else:
        print("请选择排序规则")
        print("1. 正序")
        print("2. 倒序")
        sort_type = input("请选择：\n")
        if find_element(["1", "2"], sort_type) < 0:
            print("log:student_list:=>>> 请选择正确的排序规则")
            return
        # 正序倒序 true 倒序  反之 倒序
        if sort_type == "1":
            is_reverse = False
        else:
            is_reverse = True

        # 排序函数
        def sort_fn(sort_info):
            if sort_choice == '2':
                return sort_info['age'] * 1
            if sort_choice == '3':
                return sort_info['student_num'] * 1
            if sort_choice == '4':
                return sort_info['GPA'] * 1
            return 1

        result = sorted(data['list'], key=sort_fn, reverse=is_reverse)
    print("log:student_list:=>>> 学生信息列表")
    for info in result:
        info_str = ""
        for field in fields:
            info_str += data_dict[field]['title'] + ":" + info[field] + " "
        print(info_str)


def main():
    file_path = "./db.json"
    data = get_json_data(file_path)
    while True:
        print("\n========= 学生信息管理系统 ===========")
        print("1. 添加学生信息")
        print("2. 删除学生信息(根据姓名)")
        print("3. 修改学生信息(根据姓名)")
        print("4. 查看学生信息(根据姓名)")
        print("5. 查看学生信息列表")
        print("6. 退出")
        print("========= 学生信息管理系统 ===========")
        choice = input("请选择功能：\n")
        if choice == "1":
            student_add(data)
            sync_json_data(file_path, data)
        if choice == "2":
            student_del(data)
            sync_json_data(file_path, data)
        if choice == "3":
            student_edit(data)
            sync_json_data(file_path, data)
        if choice == "4":
            student_find(data)
        if choice == "5":
            student_list(data)
        if choice == "6":
            print("退出成功,感谢使用")
            break


if __name__ == "__main__":
    main()
