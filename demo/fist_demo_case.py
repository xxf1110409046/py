# coding: utf-8

#导入能操作Excel的包
import xlrd
import requests
import os
import json
from utils.log import LOG
from utils.reader_excel import readerExcel
from request.request import *


#获取当前excel文件路径
filePath = os.getcwd() + "\\test_excel_data\\data.xlsx"
LOG.info("excel文件路径 " + filePath)
#利用文件路径读取Excel文件，生成数组
list,listUrls,listResult = readerExcel(filePath)
#声明header
header = {'Content-type':'application/json;UTF-8'}
#获取请求参数
postData = list[0]
postUrl = listUrls[0]
#print(postData + "shuju" + postUrl)
#向服务器请求，获得句柄，即响应数据
print("postData=====" + postData)
response = requests.post(url=postUrl,data=postData,headers=header)
#print(response.text)
#结果集转JSON
resultJsonFomat = response.json()
#获取“message”串
resultJsonFomat['message']
#data = response.getJson()
#datas = data['errorCode']
LOG.info("请求响应结果是：" + resultJsonFomat['message'])
#设置断言，查看结果是否一致
if resultJsonFomat['message'] == listResult[0]:
    LOG.info('登录===断言正常')

#验证登录接口返回状态码是否正常
paramsData = []
paramsData.append("loginName")
paramsData.append("password")
paramsData.append("clientAppCode")
paramsData.append("clientIP")
paramsData.append("hostName")
paramsData.append("clientMAC")
paramsData.append("serverIP")
postData = json.loads(postData)

#字符过长限制以及必填项验证
def check_errorcode(stringLength,errorCode,logParams):
    for data in range(len(paramsData)):
        params = paramsData[data]
        if postData[params] in str(postData):
            newPostData = str(postData).replace(postData[params], stringLength)
            newPostData = eval(newPostData)
            loginResponse = post_requests(postUrl,json.dumps(newPostData),header)
            # 获取‘errorCode’，判断是否响应准确，标准状态码是102002
            errorCodeData = loginResponse['errorCode']
            LOG.info(errorCodeData)
            if errorCodeData == errorCode:
                LOG.info("参数" + params + logParams + "验证成功，结果是：" + loginResponse['message'])
            else:
                LOG.info("参数" + params + logParams + "验证失败，结果是：" + loginResponse['message'])
        else:
            print("无该字符串")

# 必填项验证
check_errorcode("","102002","必填项")

#字符过长验证
toolong = "123456789123456789987456123123456789"
check_errorcode(toolong,"102002","字符长度限制")

#用户名或密码错误


#json.dumps(postData)
#print(postData['hostName'])keep









'''
getUrl = 'http://172.16.10.10:8080/nvsg_web/fnd/dictionarytable/getDictionaryTableById.do'
getParam = {
    'id':'1'
}
#get提交方式
getResponse = requests.get(url=getUrl,params=getParam,headers = header)

d = getResponse.json()
e = getResponse['token']
print('这就是token：' + e)

print(getResponse.text)
print(getResponse.url)
'''

#获取公司信息
companyurl = 'http://172.16.10.10:8080/nvsg_web/fnd/company/findCompanyDropDown.do'
companyRe = requests.get(url=companyurl,headers=header)
print('公司信息是：' + companyRe.text)




        


      


