# 多继承,就是子类有多个父类,并且具有特们的特征
# python 可以多继承
# 定义一个父类
class S:
    def printS(self):
        print('s')
class B:
    def printB(self):
        print("b")

# 定义子类.继承来自A,B
class C(S,B):
    def printC(self):
        print('-c-')

obj_c = C()
obj_c.printS()
obj_c.printB()
