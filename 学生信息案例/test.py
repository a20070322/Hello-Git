# 定义 dict
people = {
    "name": 'zzy',
    "age": 26
}

# 打印字典
print(people)
# {'name': 'zzy', 'age': 26}

# 字典取值
print(people['name'])
# zzy

# 字典修改值
people['name'] = 'drd'
print(people['name'])
# drd


# 删除 name key
del people['name']

# 打印字典 name 已被删除
print(people)
# {'age': 26}
