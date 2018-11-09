import requests
import json
import test_case.class_demo

'''
from utils.log import LOG
listView = ['1','2','3','4']
#listView.count()
length = len(listView)
listView.append('9')
print(listView)
LOG.info('222')

number = 0
while (number < 10):
    number = number + 1
    if number == 5:
        print('我可以')
        break
    else:
        print('不可以')


#循环打印一个python
#声明一个数组，存储数据
py = []
for study in 'python':
    print('study:' + study)
    py.append(study)
print(py)

#语句不一样，in range 可以从头到尾，不需要声明变量
for lists in range(len(py)):
    print('list:' + py[lists])

length = len(py)
print('length=' + str(length))


#随便打印一堆*
for reslut in range(10):
    print (' * ')
    
#声明一个数组
list = []
#给数组赋值
for i in range(10,20):
    list.append(i)
    i = i + 1

for k in range(0,20):
    list.append(k)
    k = k + 1
#循环遍历数组，打印出来

for s in range(len(list)):
    print("打印 + " + str(list[s]))
    s = s + 1

#冒泡排序数组，逻辑是 第一个数和其他数比较，较大的排在第一位，依次类推
for d in range(len(list)):
    for f in range(len(list)):
        if list[d] < list[f]:
            #声明一个数，做数据交换
            g = list[d]
            list[d] = list[f]
            list[f] = g
            f = f + 1
    d = d + 1

#循环遍历数组，打印出来
for j in range(len(list)):
    print("打印 + " + str(list[j]))
    j = j + 1 
'''

header = {'Content-type':'application/json;UTF-8'}

def function(response):
    response = response.json()
    response['d']
    if response['d']:
        print("我已经成功调用了")
    else:
        print("你这个小混蛋，小要拿我的数据，没门")

#登录验证，返回值为boolaen
url = "http://gps.szwearable.com/OpenAPI/MobileService.asmx/Login"
paramsData = {"LoginName":"13728792621","Password":"123456","AppKey":"FCB94EB3-F83A-4103-9F6F-E8D0FD614696"}
response = requests.post(url=url,data=json.dumps(paramsData),headers = header)
print(response.text)
cookie = response.cookies
function(response)

#根据登录名，获取用户信息
userUrl = "http://gps.szwearable.com/OpenAPI/MobileService.asmx/GetDeviceListByLoginName"
userParams = {"LoginName":"13728792621"}
userResponse = requests.post(url = userUrl,data=json.dumps(userParams),headers = header,cookies = cookie)
print(userResponse.text)
function(userResponse)

#获取当前APP语种
languageURL = "http://gps.szwearable.com//OpenAPI/MobileService.asmx/SaveToken"
languageParams = {"LoginName":"13728792621","Lang":"zh","AppKey":"FCB94EB3-F83A-4103-9F6F-E8D0FD614696","IMEI":"862224034230618","CType":1}
languageResponse = requests.post(url = languageURL,data=json.dumps(languageParams),headers = header,cookies = cookie)
print(languageResponse.text)
function(languageResponse)

#设置极光推送注册id
pushURL = "http://gps.szwearable.com//OpenAPI/MobileService.asmx/SettingJPushRegistrationId"
pushParams = {"RegistrationId":"190e35f7e0429431ab9"}
pushResponse = requests.post(url=pushURL,data=json.dumps(pushParams),headers = header,cookies = cookie)
print(pushResponse.text)
function(pushResponse)

#开始测试
students = test_case.class_demo.student("搞怪","成功")
students.printData()

waleURL = "https://api.post.wale.wawazhuawawa.com/api/v2/post/list"
waleParams = {"offset":0,"limit":1,"channel":10}
waleReponse = requests.post(url=waleURL,data=json.dumps(waleParams),headers = header)
print(waleReponse.text)



baiduURL = "http://www.baidu.com"
baiduReponse = requests.get(baiduURL,headers=header)
print("百度的请求" + baiduReponse.text)
#1.请求头部符合W3c协议规范，转换格式，2.传入的参数不是json格式，默认是python的字典，转换为json格式，请求后得到响应；值为true

















