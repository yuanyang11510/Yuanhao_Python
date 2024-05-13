#0读取txt文件得到string
with open("路径","r",encoding = "UTF-8") as file:
    text = file.read()
    print("text =",text)
#1将string转换为list1   
lst1 = list(text)
print("lst1 =",lst1)
print("length1=",len(lst1))
#2创建另一个空list2，过滤标点符号和换行符，得到一个只含有汉字的list2
#（这一步在text文件中可以直接用正则表达式解决，但为了保证源文件的完整性，建议通过代码进行）
lst2 = []
for x in lst1:
    if x == "，" or x == "。" or x == "？" or x == "！" or x == "：" or x == "\n" or x ==" ":
        pass
    else:
        lst2.append(x)
print("lst2 =",lst2)
print("length2=",len(lst2))
#3创建第三个空list3，将list2中的重复项合并，然后加入list3，得到一个含有所有list2中不重复汉字的list3
lst3 = []
for x in lst2:
    if x not in lst3:
        lst3.append(x)
print("lst3 =",lst3)
print("length3=",len(lst3))
#4计算list2中汉字的字频并写入文件
with open("路径","w",encoding = "UTF-8") as file:
    for x in lst3:
        frequency = lst1.count(x)
        sentence = x+"出现了"+str(frequency)+"次"#注意数字要转换为字符串后才能写入
        file.write(sentence+"\n")
#5将字频降序排列并写入文件，见"字典排序的两种方法"
dic = {}
for x in lst3:
    dic[x] = lst2.count(x)
print("dic =",dic)
sorted_dic_lst = sorted(dic.items(),key = lambda x: x[1],reverse = True)
print("sorted_dic_lst =",sorted_dic)
with open("路径","w",encoding="utf-8") as f:
    for character,frequency in sorted_dic_lst:#注意这里的list是由二元元组组成的，所以for循环需要引用两个变量
        sentence = character+"出现了"+str(frequency)+"次"
        f.write(sentence+"\n")
                   

