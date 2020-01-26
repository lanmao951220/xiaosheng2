import tkinter
import time
import random as rd
'''
蜜蜂从上向下运动
可以通过键盘左右控制
'''

step = 0# 计数器 小飞机走了多少步
direction = (1,1)
x = 0
y = 10
def set_right(e):
    global x
    x += 20

def set_left(e):
    global x
    x -= 20

root_window = tkinter.Tk()
root_window.title('赵lulu')

root_window.bind('<Key-Left>', set_left)
root_window.bind('<Key-Right>', set_right)
root_window.resizable(width=False, height=False)

# 创建画布
window_canvas = tkinter.Canvas(root_window,\
                               width=480,\
                               height=600)
window_canvas.pack()


def main():
    # 创建
    # 创建开始界面
    background_image_fullname = '../Images/background.gif'
    # background_image_fullname = '/home/augs/AirPlane/img/start.gif'
    # background_image_fullname = 'start.gif'
    start_img = tkinter.PhotoImage(file=background_image_fullname)
    window_canvas.create_image(480/2,\
                               600/2,\
                               anchor=tkinter.CENTER,\
                               image=start_img,\
                               tags='start')

    sp = '../Images/smallplane.gif'
    sp_img = tkinter.PhotoImage(file=sp)
    window_canvas.create_image(50,\
                               100/2,\
                               anchor=tkinter.CENTER,\
                               image=sp_img,\
                               tags='sp')
    ap_move()
    root_window.mainloop()
    # 让小蜜蜂动起来

def ap_move():
    global step
    global x
    global y
    y += 10
    print(x,y)
    window_canvas.move('sp', x, y)
    step += 1
    window_canvas.after(1000,ap_move)

if __name__=="__main__":
    main()