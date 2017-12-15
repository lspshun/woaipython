# 初始化函数,用来完成一些默认的设定
# 定义汽车类
class Car:

    def __init__(self):
        self.wheelnum = 4
        self.color = 'blue'

    def move (self):
        print('车在跑,目标东京')


# 创建对象
BMW = Car()
print('color is:%s'%BMW.color)
print('number is: %s'%BMW.wheelnum)
# 创建car对象后,没有调用init方法前提下,bmw就有默认的两个属性wheelnum和color,
# 原因是init方法在创建对象后,就立刻北默认调用



