from selenium import webdriver  #导入webdriver
import time

driver = webdriver.Chrome()   #获取Chrome浏览器对象
# driver = webdriver.Firefox()
driver.get("http://www.baidu.com")   #进入百度页面
print(driver.title)   #打印title
driver.maximize_window()   #窗口最大化
driver.find_element_by_id("kw").send_keys("1")  #输入框中输入“selenium”
# driver.find_element_by_id("su").click()   #点击按钮
# driver.find_element_by_tag_name("_blank").click()
#driver.find_element_by_link_text("功能自动化测试工具--Selenium篇")
try:
    # driver.find_element_by_link_text("官网").click()  #根据link找到“知道”，点击进入知道页面
    #driver.find_element_by_link_text("-专业IT技术社区").click()
    #driver.find_element_by_partial_link_text("-专业IT技术社区").click()
    #driver.find_element_by_class_name("favurl").click()
    # driver.find_element_by_xpath("//*/div[@id='2']/a[text()='功能自动化测试工具--Selenium篇']")
    # driver.find_element_by_class_name("result c-container ")
    # driver.find_element_by_partial_link_text("功能自动化测试工具")
    # driver.find_element_by_id("2")
    #driver.find_element_by_class_name("官网").click()
    driver.find_element_by_xpath("//input[@id='su']").click()
    # driver.find_element_by_class_name("t").click()
    driver.find_element_by_link_text("图片").click()
    driver.back()
    # driver.find_element_by_xpath("//a[contains(text(),'正义网')]").click()
    # driver.switch_to_window(driver.window_handles[0])
    # driver.switch_to_frame()
    # driver.find_element_by_xpath("//*[contains(text(),'正义网')]").click()
    # driver.find_element_by_link_text("正义网").click()
    # for i in range(1,5000):
    driver.find_element_by_link_text("贴吧").click()
    time.sleep(3)
    driver.back()
except Exception as e:
    print("格式错误：",format(e))
# time.sleep(3)
# driver.refresh()
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("小熊")
# driver.find_element_by_id("su").click()
# time.sleep(20)
# driver.close()

# ieDriver = webdriver.Ie()百度一下，你就知道
#
# Process finished with exit code 0
# ieDriver.get("http://www.baidu.com")
# ieDriver.maximize_window()
# ieDriver.find_element_by_id("kw").send_keys("小熊")
# ieDriver.find_element_by_id("su").click()
# print("IE使用结束")


