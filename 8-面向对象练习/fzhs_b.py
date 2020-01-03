'''
请输入一个三位数与程序随机数比较大小
如果大于程序随机数，则分别输入这个三位数的个位、十位、百位
如果等于程序随机数，则提示中奖，记100分
如果小于程序随机数，则将120个字符输入到文本文件中（规则是每一条字符串的长度为12，
单独占一行，并且前四个是字母，后8个是数字）
'''
# ascii 码转数字
#print(ord("A"))
#print(ord("Z"))
# 数字转ascii码
#print(chr(97))

def Line():
    # 定义一个空字符串用于拼接字符
    str_num = ""
    # 循环前四个随机字符（用ascii对应的值来随机再转换为字母）
    for i in range(4):
        # 随机小写字符的ascii值
        num = random.randrange(97,123)
        # 将ascii值转换成对应的字母
        str_s = chr(num)
        # 将字符串拼接
        str_num = str_num + str_s
    for i in range(8):
        num = random.randrange(0,10)
        str_num = str_num +str(num)
    return str_num
source = 0
import random
num = input("请输入一个三位数,输入-1结束")
while 1:
    if num == "-1":
        break
    random_num = random.randrange(100,1000)
    print(random_num)
    if num.isdigit() and 100<=int(num)<=999:
        if int(num)>int(random_num):
            temp = str(num)
            a = temp[0]
            b = temp[1]
            c = temp[2]
            print("你输入的数比随机数大，程序随机数是{}".format(random_num))
            print("百:"+a)
            print("十:"+b)
            print("个:"+c)
        elif int(num) == int(random_num):
            source = source + 100
            print("恭喜你中奖了,目前分数为:",source)
        elif int(num) < int(random_num):
            print("你输入的数比随机数小")
            for i in range(10):
                Line()
                str_line = Line()
                with open("str_num.txt","a")as f:
                    f.write(str_line+"\n")
        else:
            print("请按规定输入")