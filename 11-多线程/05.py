import time
# 导入多线程包并更名为thread
import threading
def loop1(in1):
    # ctime 得到当前时间
    print('Start loop 1 at :',time.ctime())
    # 把参数打印出来
    print('我是参数',in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop 1 at:',time.ctime())

def loop2(in2,in3):
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 把参数in1 和in2 打印出来  代表使用
    print('我是参数', in2, '和参数', in3)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 1 at:', time.ctime())

def main():
    print('Starting at:',time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1,args=('王老大',))
    t1.start()

    t2 = threading.Thread(target=loop2,args=('王大鹏','王晓鹏'))
    t2.start()

    t1.join()
    t2.join()

    print("All done at :",time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)