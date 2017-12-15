# break continue只能用于循环中,不能单独使用
# break continue 在嵌套循环中,只对最近的一层循环起作用
name = 'lishauipeng'
for i in name:
    print('----')
    if i == "i":
        continue
    print(i)