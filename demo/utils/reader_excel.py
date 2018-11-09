# encoding:utf-8

import xlrd
from utils.log import LOG

#根据路径，找到接口文件，读取Excel文件内容，返回列表
def readerExcel(fileUrl):
    try:
       # print("总行数是：" + fileUrl)
        file = xlrd.open_workbook(fileUrl)
        listContent = []
        listUrl = []
        listResult = []
        #获取Excel的第几页数据
        msheet = file.sheets()[0]
        #获取总共是多少页
        nrows = msheet.nrows
        listUrl.append(msheet.cell(1,3).value)
        listContent.append(msheet.cell(1,2).value)
        listResult.append(msheet.cell(1,5).value)
        #print (listContent)
        return listContent,listUrl,listResult
    except Exception:
        #print("出现了错误")
        LOG.info('登录接口出现了错误')

