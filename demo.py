import fzl_b  # 导入fzl_a 也可以
import zimu_a
game = input("请选择游戏\n1.数字游戏\n2.字母游戏")
if game == "1":
    game_num = fzl_b.GameNum()
    game_num.num_game(0,0)
elif game == "2":
    game_zimu = zimu_a.GameZiMu()
    game_zimu.a()
else:
    print("输入错误")
