import json


# 打开JSON文件，并且打印
with open('./example/data.json', 'r') as data:
    file_str = data.read()
    print(file_str)
    print(type(file_str))


# 打开JSON文件、并解析为json数据(list dict)
with open('./example/data.json', 'r') as data:
    res = json.load(data)
    print(res)
    print(type(res))

# 获取json数据
# 添加数据({"name": "test" + str(len(json_data))})
# 并且保存list 到文件

file_path = './example/data.json'
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)
    json_data.append({
        "name": "test" + str(len(json_data)),
    })
    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file)






# # 获取持久化存储数据
# def get_json_data(file_path):
#     try:
#         # 尝试打开并读取JSON文件
#         with open(file_path, 'r') as json_file:
#             data = json.load(json_file)
#     except FileNotFoundError:
#         # 默认数据
#         data = {
#             "list": []
#         }
#         with open(file_path, 'w') as json_file:
#             json.dump(data, json_file)
#     return data


# # 数据同步持久化存储
# def sync_json_data(file_path, data):
#     with open(file_path, 'w') as json_file:
#         json.dump(data, json_file)