import configparser

# 第一步生成相应的ConfigParser的实例
cfg = configparser.ConfigParser()

# 生成实例后需要读入相应的配置文件
cfg.read("test_ini.ini",encoding='utf-8')  # ini_test.py 文件并不能用test_ini命名

sp_name = cfg.get('SmallPlane','name')
print(sp_name)

sp_width = cfg.getint('SmallPlane', 'width')
print(sp_width)