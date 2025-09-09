#weight = input("请输入带有符号的重量")
if weight[-2:] in ["kg"]:
    poung = (eval(weight[0:-2])) * 2.2046
    print("对应的重量为：{:.3f}磅".format(poung))
elif weight[-2:] in ["pd"]:
    kg = (eval(weight[0:-2])) / 2.2046
    print("对应的重量为：{:.3f}千克".format(kg))
else:
    print("输入错误") 
