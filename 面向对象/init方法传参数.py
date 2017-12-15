# 定义汽车类
# 创建玩对象后init方法已经被默认执行,传递参数
# init 中默认一个参数self
# 如果创建对象传递两个实参,那么init中self作为第一个形参外还需要两个形参
# init中的self参数不需开发者传递,Python解释器会自动将当前的对象引用传递进去

class Car:
    def __init__(self,newwheelnum,newcolor):
        self.wheelnum = newwheelnum
        self.color = newcolor

    def move(self):
        print('车在跑,目标东京')
# 创建对象
BMW = Car(4,'blue')

print("color is :%s"%BMW.color)
print('cheelnum is: %s'%BMW.wheelnum)

