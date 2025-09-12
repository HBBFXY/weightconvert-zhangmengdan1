weight = input()
if weight[-2:] in ["kg"]:
    poung = (eval(weight[0:-2])) * 2.2046
    print("对应的英制重量为：{:.3f}磅".format(poung))
elif weight[-2:] in ["pd"]:
    kg = (eval(weight[0:-2])) * 0.4535
    print("对应的公制重量为：{:.3f}公斤".format(kg))
else:
    print("输入错误") 
