import random
class GameNum():
    def Line(self):
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
    def num_game(self,total,source):
        while 1:
            num = input("请输入一个三位数,输入-1结束")
            if num == "-1":
                break
            random_num = random.randrange(100,1000)
            print(random_num)
            if num.isdigit() and 100<=int(num)<=999:
                # 计算有效输出了多少次
                total += 1
                print("输入%d次"%total)
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
                    print("你中奖的概率是{}".format(source/total))
                elif int(num) < int(random_num):
                    print("你输入的数比随机数小")
                    for i in range(10):
                        GameNum.Line(self)
                        str_line = GameNum.Line(self)
                        with open("str_num.txt","a")as f:
                            f.write(str_line+"\n")
                else:
                    print("请按规定输入")