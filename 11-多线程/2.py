import random as r


class Turtle(object):
    def __init__(self):
        self.power = 100
        # 初始化乌龟的位置
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        new_x = r.choice([1, 2, -1, -2]) + self.x
        new_y = r.choice([1, 2, -1, -2]) + self.y

        # 判断 乌龟的移动是否超出了边界
        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

    def eat(self):
        self.power += 20
        if self.power >= 100:
            self.power = 100


class Fish(object):
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])

        if new_x > 10:
            self.x = 10 - (new_x - 10)
        elif new_x < 0:
            self.x = 0 - (new_x - 0)
        else:
            self.x = new_x

        if new_y > 10:
            self.y = 10 - (new_y - 10)
        elif new_y < 0:
            self.y = 0 - (new_y - 0)
        else:
            self.y = new_y

        return (self.x, self.y)


turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼吃完了，游戏结束了")
        break
    if not turtle.power:
        print("乌龟没有体力了，游戏结束")
        break

    pos = turtle.move()

    # 在迭代中做列表的删除元素是非常危险的，经常会出现一些意想不到的问题，因为迭代器是
    # 直接引用列表元素的数据做的操作，所以我们这里把列表拷贝一份传送给迭代器，然后再对
    # 列表做操作

    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼被吃掉了")