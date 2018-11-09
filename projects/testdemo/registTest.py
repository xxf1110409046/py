#coding=utf-8
import json
# class Regist():
#     def test001(self):
#         print('time001')
#     def test002(self):
#         print('time002')
#     def test003(self):
#         print("time003")



#要传入一个两个字段，一个数组
# name 'xiong' 'yang'
# age '16' '18'
# grand '90' '98'
# study 'English' 'china'
# list = ['wanderful','xiongdi',{'xiong','16','90','English'},{'yang','18','98','china'}]
# list = json.dumps(list)
# print(list)

# class primary_school():
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def displayCount(self):
#         print('Total Employee %d')
#     def displayEmployee(self):
#         print('go die')

class Result(object):
    def __init__(self, code, message, response=None):
        if response is None:
            response = []
        self.code = code
        self.message = message
        self.response = response


test_str = '{"code":200,"message":"发送成功","response":[{"code":0,"message":"xxxxxxxx","mobile":"xxxxxx","taskId":null},{"code":1,"message":"xiongxiaofeng","mobile":"13725894568","taskId":null}]}'

#字符串转化为json
test_str = json.loads(test_str)

# test_str = json.dumps(test_str)
print(test_str['response'])
name = test_str['response']
for i in name:
    print(str(i['code']))
    if 2 == i['code']:
        print('知道到：' + 'xiongxiaofeng')
        print('code是：' + str(i['code']))
    print('go')


# result = Result(**json.loads(test_str))
# list = result.response
# compare_message = 'xiongxiaofeng'
# # code_go = ''
# # message_go = ''
# # mobile_go = ''
# # taskId_go = ''
# for i in list:
#     # print(i)
#     message = i['message']
#     if compare_message in message:
#         print('找到你了:' + message)
#         code_go = i['code']
#         message_go = i['message']
#         mobile_go = i['mobile']
#         taskId_go = i['taskId']
#         print(str(code_go) + str(message_go) + str(mobile_go) + str(taskId_go))
        # print('当前索引是：' + )
    # print(i['code'])
    # print(i['message'])
    # print(i['mobile'])
    # print(i['taskId'])



# print(list)



