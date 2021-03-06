# 多态的概念是应用于Java和C#这一类强类型语言中，而Python崇尚“鸭子类型”。
# 所谓多态：定义时的类型和运行时的类型不一样，此时就成为多态pyPthon伪代码实现Java或C#的多态
'''class F1(object):
    def show(self):
        print ('F1.show')
class S1(F1):
    def show(self):
        print('S1.show')
class S2(F1):
    def show(self):
        print ('S2.show')
# 由于在Java或C#中定义函数参数时，必须指定参数的类型
# 为了让Func函数既可以执行S1对象的show方法，又可以执行S2对象的show方法，所以，定义了一个S1和S2类的父类
# 而实际传入的参数是：S1对象和S2对象
def Func(F1 obj):
    """Func函数需要接收一个F1类型或者F1子类的类型"""
    print obj.show()

s1_obj = S1()
Func(s1_obj) # 在Func函数中传入S1类的对象 s1_obj，执行 S1 的show方法，结果：S1.show
s2_obj = S2()
Func(s2_obj) # 在Func函数中传入Ss类的对象 ss_obj，执行 Ss 的show方法，结果：S2.show
# Python “鸭子类型”
class F1(object):
    def show(self):
        print 'F1.show'

class S1(F1):

    def show(self):
        print 'S1.show'

class S2(F1):

    def show(self):
        print 'S2.show'

def Func(obj):
    print obj.show()

s1_obj = S1()
Func(s1_obj)

s2_obj = S2()
Func(s2_obj)
'''