# 打印id()
# 定义_str_()方法
# 在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
# 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

class Car:
    def __init__(self, newwheel,newcolor):
        self.wheelnum = newwheel
        self.color = newcolor
    def __str__(self):
        msg = "我的颜色是" +self.color+'我有'+str(self.wheelnum)+"轮胎个数"
        return msg
    def move(self):
        print('车在跑,目标东京')
# 创建对象
BMW = Car(4,'白色')
print(BMW)
