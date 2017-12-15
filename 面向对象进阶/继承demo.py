class Cat(object):
    def __init__(self,name, color = 'blue'):
        self.name = name
        self.color = color

    def run(self):
        print('%s--runnign'%self.name)

# 定义一个子类,继承cat类
# 子类无init方法,但是父类有,默认继承了父类的init方法
# 子类继承的时候,写括号里的为父类的名字
# 父类的属性方法会继承给子类
# 私有的属性，不能通过对象直接访问，但是可以通过方法访问
# 私有的方法，不能通过对象直接访问
# 私有的属性、方法，不会被子类继承，也不能被访问
# 一般情况下，私有的属性、方法都是不对外公布的，
# 往往用来做内部的事情，起到安全的作用

class   Bosi(Cat):
    def setnewname(self,newname):
        self.name = newname

    def eat(self):
        print("%s--eat"%self.name)

bs = Bosi('印度猫')
print("bs颜色是:%s"%bs.name)
print("bs的名字是:%s"%bs.color)
bs.eat()
bs.setnewname("bosimao")
bs.run()
