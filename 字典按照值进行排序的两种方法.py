#方法一：sorted函数+匿名（自定义）函数lambda
dic1 = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(dic1)
lst = sorted(dic1.items(), key = lambda x: x[1], reverse = False)
#第一个参数表示排序的对象是字典中的键值对
#第二个参数key用匿名函数表示排序的标准是字典的值
#第三个参数reverse=False表示默认顺序排列，True表示倒序排列
print(lst)#用sorted函数排序后得到一个由原来的键值对转换成的二元元组构成的list
dic2 = dict(lst)#将该list转换为字典
print(dic2)
#这一方法使用匿名函数直接确定sorted函数排序的标准，免去了方法二中两次使用列表推导式将键值对来回对调的步骤

#方法二:list comprehension列表推导式
dic1 = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(dic1)
tup1 = [(x[1],x[0]) for x in dic1.items()]
#用列表推导式将原来字典中的每一对键值交换位置后转换为二元元组，并将这些元组进而组成一个list
print(tup1)
tup2 = sorted(tup1)#对前面的list中的元组进行排序，实际是按照原来字典中的值进行排序
print(tup2)
tup3 = [(x[1],x[0]) for x in tup2]
#再次使用列表推导式将排完序的list中的元组的两个元素再次调换位置，实际又得到原来字典中键值对的布局
print(tup3)
dic2 = dict(tup3)#将最新得到由二元元组构成的list转换为字典
print(dic2)

