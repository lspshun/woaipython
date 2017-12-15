# 删除对象时,默认调用__del__(  )
# 当有一个变量保存了对象的引用,此对象的引用次数会加一
# del 删除变量指向的对象时,如果对象的引用计数不会1，
# 比如3，那么此时只会让这个引用计数减1，即变为2，
# 当再次调用del时，变为1，如果再调用1次del，
# 此时会真的把对象进行删除
import time
class Animal(object):

    # 初始化方法
    # 创建完成对象后会自动被调用
    def __init__(self, name):
        print('__init__方法被调用了')
        self.__name = name

    # 析构方法
    # 当对象被删除时，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..."%self.__name)

# 创建对象
dog = Animal("哈皮狗")

# 删除对象
del dog


cat = Animal("波斯猫")
cat2 = cat
cat3 = cat

print("---马上 删除cat对象")
del cat
print("---马上 删除cat2对象")
del cat2
print("---马上 删除cat3对象")
del cat3

print("程序2秒钟后结束")
time.sleep(2)