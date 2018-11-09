#目前的理解是，建立post，get，delete请求方法，供接口测试使用
import requests
import json
urls = 'http://172.16.10.10:8080/nvsg_web/fnd/'
def post_requests(url,data,header): #post方法
    # url = urls + url
    post_request_response = requests.post(url=url,data=data,headers=header)
    post_request_response = post_request_response.json()
    return post_request_response

def get_requests(url,data,header):  #get方法
    # url = urls + url
    get_request_response = requests.get(url=url,data=data,headers=header)
    get_request_response = get_request_response.json()
    return get_request_response

def delete_requests(url,data,header):  #delete方法
    # url = urls + url
    delete_request_response = requests.delete(url=url,data=data,headers=header)
    delete_request_response = delete_request_response.json()
    return delete_request_response
