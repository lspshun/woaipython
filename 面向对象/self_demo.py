# 所谓的self可以理解为自己
# 可以把self当做c++中类里面的this指针一样,就是对象自身的意思
# 当某个对象被调用其方法时,python解释器会把这个对象作为第一个参数传递给sele
# 所以开发者只需传递后边的参数即可
class Animal:
    # 方法
    def __init__(self,name):
        self.name = name
    def printName(self):
        print('name is:%s '%self.name)

# 定义一个函数
def myPrint(animal):
    animal.printName()

dog1 = Animal('xixi')
myPrint(dog1)
dog2 = Animal('haha')
myPrint(dog2)
