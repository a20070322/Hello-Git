# 接收用户输入并打印
input_str = input("请输入:")
print('输入内:'+input_str)

# 接收输入，并验证为整数
# 提示字符串类型可以通过isdigit()方法判断是否为整数
num = input("请输入一个整数:")
if num.isdigit():
    print('输入的整数是:'+num)
else:
    print("error:输入的不是整数")


# 接收输入 并判断是否为指定符号
symbol = input("请输入符号 +、- 、*、/:")
if symbol == '+':
    print("+ 使用sum函数")
elif symbol == '-':
    print("- 使用sub函数")
elif symbol == '*':
    print("* 使用mul函数")
elif symbol == '/':
    print("/ 使用div函数")
else:
    print("error:输入的符号不正确")


# 实现一个计算器 输入两个数字，选择加减乘除，计算结果
num1 = input("请输入第一个数字:")
num2 = input("请输入第二个数字:")
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    symbol = input("请输入符号 +、- 、*、/:")
    if symbol == '+':
        print("加法运算结果："+str(num1+num2))
    elif symbol == '-':
        print("减法运算结果："+str(num1-num2))
    elif symbol == '*':
        print("乘法运算结果："+str(num1*num2))
    elif symbol == '/':
        print("除法运算结果："+str(num1/num2))
    else:
        print("error:输入的符号不正确")


# 思考如何让程序一直运行，直到用户输入exit
while True:
    input_str = input("请输入:")
    if input_str == 'exit':
        break
    print('输入内:'+input_str)

# 将计算器一直运行
while True:
    num1 = input("请输入第一个数字:")
    num2 = input("请输入第二个数字:")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        symbol = input("请输入符号 +、- 、*、/:")
        if symbol == '+':
            print("加法运算结果："+str(num1+num2))
        elif symbol == '-':
            print("减法运算结果："+str(num1-num2))
        elif symbol == '*':
            print("乘法运算结果："+str(num1*num2))
        elif symbol == '/':
            print("除法运算结果："+str(num1/num2))
        else:
            print("error:输入的符号不正确,请重试")
    else:
        print("error:输入的不是整数,请重试")
    print("============= finish ================")