# 打印 0 ~ 9 的数字
# for num in range(10):
#     print(num)


# 打印 1 ~ 9 的数字
# for num in range(1, 10):
#     print(num)


# 输出
# *
# **
# ***
# ****
# *****
# ******
# for i in range(6):
#     tmpStr = ''
#     for j in range(i+1):
#         tmpStr += '*'
#     print(tmpStr)


# 输出
#      *
#     **
#    ***
#   ****
#  *****
# ******
# 实际输出 1 ~ 6
# for i in range(1, 7):
#     tmpStr = ''
#     for j in range(6-i):
#         tmpStr += ' '
#     for j in range(i):
#         tmpStr += '*'
#     print(tmpStr)

# 输出
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

# 实际输出 1 ~ 6
# for i in range(1, 7):
#     tmpStr = ''
#     for j in range(6-i):
#         tmpStr += ' '
#     for j in range(2*i-1):
#         tmpStr += '*'
#     print(tmpStr)
