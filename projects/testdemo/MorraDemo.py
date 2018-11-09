#coding:utf-8
from enum import Enum
import requests
import json
import random

class Marro():

    shear = 0 #剪刀
    stone = 1 #石头
    cloth = 2 #布


#判断男孩女孩出拳
def Punsh(sex,result):
    # print(result)
    if(result == Marro.shear):
        print(sex + "出的拳是：剪刀" )
    if(result == Marro.stone):
        print(sex + "出的拳是：石头")
    if(result == Marro.cloth):
        print(sex + "出的拳是：布")



#boy出拳
list_boy = []
list_girl = []
no_win = []
boy_win = []
girl_win = []
def result():
    # boy = input('please input:')
    boy =  random.randint(0,2)
    Punsh("boy",boy)
    #girl出拳
    girl = random.randint(0,2)
    Punsh("girl",girl)
    #判断谁赢了1
    if(boy == girl):
        print("平手")
        no_win.append(1)
    else:
        if((boy == 0 and girl == 2) or (boy == 1 and girl == 0) or (boy == 2 and girl == 1) ):
            print('boy' + '赢')
            boy_win.append(1)
        else:
            print('girl' + "赢")
            girl_win.append(1)
    list_boy.append(boy)
    list_girl.append(girl)


for i in range( 0,1000):
    result()

# for i in list:
#     print(i)

#统计boy和girl出现0.1.2的频率
# def count(lists):
#     lists.
def marroResult(result):
    if result == 0:
        return "剪刀"
    if result == 1:
        return "石头"
    if result == 2:
        return "布"

stringBoy = ''
stringGirl = ''
stringMarro = ''
for i in range(0,3):
    count_boy = list_boy.count(i)
    count_girl = list_girl.count(i)
    stringResult = marroResult(i)
    print("男孩出现" + stringResult + "的次数是： " + str(count_boy))
    print("女孩出现"  + stringResult  + "的次数是： " + str(count_girl))
    stringMarro = stringMarro + "," +stringResult
    stringBoy = stringBoy + "," + str(count_boy)
    stringGirl = stringGirl + "," + str(count_girl)
    print("男孩出现" + stringMarro + "的次数分别是：" + stringBoy)
    print("男孩出现" + stringMarro + "的次数分别是：" + stringGirl)
    print(stringMarro)

#统计平，男孩赢，女孩赢的此时
def count():
    count = "平次数：" + str(no_win.count(1)) + ";" + "男孩赢次数：" + str(boy_win.count(1)) + ";" + "女孩赢次数:" + str(girl_win.count(1))

    return count

print(count())




#url
url = 'http://172.16.11.130:8080/nvsg_web/dvc/device/findDevicePagedByCriteria.do?name=&code='

#header
header = 'Content-Type:application/json;charset=UTF-8'

#请求
result = requests.get(url=url)
# result = json.loads(result)
print(result.text)
print(result.encoding)
result = result.json()
print(result['data'])
#将data数据转换成list or dect or
list = result['data']
print(list['pageSize'])
print(list['list'])

#试着打印下list
list_print = list['list']

# result = json.loads(result)

# print(result)
# print(str(result['errorCode']))

# if():
#     print('boy' + '赢')
# if():
#     print('boy' + '赢')

#测试：声明一个list，转换成JSon串，打印出来
# list_json = ['123',12,'xiaolaodi','风',30.66]
# print(list_json)
# list_json = json.dumps(list_json)
# print(list_json)
# list_json = json.loads(list_json)
# print(list_json)

#原始类型转换成JSon
#list_orgin = ['1',4,'xiong']

#我要获取一条名字叫做设备故障的数据





#像一个查询操作，可以验证的点 在不经过数据查询对比的情况下：
#1.




