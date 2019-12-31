import keyword

'''
# 输入
name = input()
# 输出
print("输出name = ",name)
'''

# 单行注释，程序中的关键字
# print(keyword.kwlist)

# 多行注释，也可以表示多行内容
'''
这个是三个单引号，或者是三个双引号
注释1
注释2
'''

# python使用缩进符表示代码块，缩进符的空格数是可变的，同一个代码块有相同的缩进符
'''
if True:
    print("true")
else:
    print("false")
'''

# 多行用反斜杠\来实现
'''
total = "12" + \
"3456"
print(total)
'''

# 在[],{}或者()中的多行语句，不需要使用反斜杠\
'''
total = ["12",
"3456"]
print(total)
'''

# 数字类型 int,bool,float,complex(复数：1+2j)
# print(1 + False + 1.23 + 1 + 2j)

# 字符串，单引号或者双引号，字符串截取的语法格式 变量变量[头下标:尾下标:步长]
'''
str = "jasonhua"
print(str,str[0],str[2:5],str[2:-1],str * 2,str + "测试")
'''

# 空行，函数之间或者类之间用空行分隔
# 同一行有多条语句用分号;隔开
# if,while,def,class这样的复合语句，首行以关键字开始，以冒号:结束
# 用import或者from ... import来导入相应的模块，
# 例如：
#   from somemodule import firstfunc, secondfunc, thirdfunc
#   import somemodule
#   from somemodule import firstfunc
# r'' 表示内部的字符串不转义
# and or not


