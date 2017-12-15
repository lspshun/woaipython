# 所谓重写，就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法

#coding=utf-8
class Cat(object):
    def sayHello(self):
        print("halou-----1")


class Bosi(Cat):

    def sayHello(self):
        print("halou-----2")

bosi = Bosi()

bosi.sayHello()
'''调用父类的方法

#coding=utf-8
class Cat(object):
    def __init__(self,name):
        self.name = name
        self.color = 'yellow'


class Bosi(Cat):

    def __init__(self,name):
        # 调用父类的__init__方法1(python2)
        #Cat.__init__(self,name)
        # 调用父类的__init__方法2
        #super(Bosi,self).__init__(name)
        # 调用父类的__init__方法3
        super().__init__(name)

    def getName(self):
        return self.name

bosi = Bosi('xiaohua')

print(bosi.name)
print(bosi.color)

'''