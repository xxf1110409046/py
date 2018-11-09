import os
#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for number1 in range(1,5):
    for number2 in range(1,5):
        for number3 in  range(1,5):
            if number1 != number2 & number2 != number3 & number1 != number3:
                print(str(number1) + str(number2) + str(number3))

#企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# inputNumber = int(input("起始金额是："))
# rate = [0.1,0.075,0.05,0.03,0.15,0.01]
# money = [0,100000,200000,400000,600000,1000000]
# total = 0
# i = 1
# for i in range(1,6):
#     if inputNumber > money[i]:
#         gain = (money[i] - money[i - 1]) * rate[i - 1]
#         total = gain + total
#     else:
#         gain = (inputNumber - money[i-1]) * rate[i - 1]
#         total = gain + total
#         break
#     print(str(total))
# print(str(total))
#标准答案是依次递减的原则
# inputNumber = int(input("起始金额是："))
# money = [1000000,600000,400000,200000,100000,0]
# rate = [0.01,0.015,0.03,0.05,0.075,0.1]
# total = 0
# for i in range(0,6):
#     if inputNumber > money[i]:
#         gain = (inputNumber - money[i]) * rate[i]
#         total = total + gain
#         inputNumber = money[i]
# print(str(total))

#题目：将一个列表的数据复制到另一个表中
# list = [1,2,4,9,10]
# list1 = list[:]
# print(list1)

#输出乘法口诀表9*9
# for cell in range(1,10):
#     print()
#     for row in  range(1,cell + 1):
#         print ("%d*%d=%d" %(row,cell,row*cell))

# number1 = int(input("第一位数值："))
# number2 = int(input("第二位数值："))
# total = number1 + number2
# print("总数值是：" + str(total))


import json


























