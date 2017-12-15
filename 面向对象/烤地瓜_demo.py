# 更好理解面向对象
'''cookedLevel : 这是数字；0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，
超过8表示已经烤成木炭了！我们的地瓜开始时时生的
cookedString : 这是字符串；描述地瓜的生熟程度
condiments : 这是地瓜的配料列表，比如番茄酱、芥末酱等
示例方法
cook() : 把地瓜烤一段时间
addCondiments() : 给地瓜添加配料
__init__() : 设置默认的属性
__str__() : 让print的结果看起来更好一些
'''

# 定义类,定义init方法
class kaodigua:
    # 定义初始化方法
    def __init__(self):
        self.cooklevel = 0
        self.cookedString = '生的'
        self.condiments = []
# 添加烤地瓜方法
def cook(self,time):
    self.cooklevel += time
    if self.cooklevel > 8:
        self.cookedString = '糊了'
    elif self.cooklevel > 5:
        self.cookedString = 'ok'
    elif self.cooklevel > 3:
        self.cookedString = 'not ok'
    else:
        self.cookedString = '生的'
# 用来进行测试
mykaodigua = kaodigua()
print(mykaodigua.cooklevel)
print(mykaodigua.cookedString)
print(mykaodigua.condiments)

# 测试cook方法是否OK
print('开始烤地瓜')
mykaodigua.condiments(4)
print(mykaodigua.cooklevel)
print(mykaodigua.cookedString)
