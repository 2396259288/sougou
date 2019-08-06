from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.chrome.options import Options
import random

# username = '2396259288'
# password = 'kaito-536260'
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')


driver = webdriver.Chrome()
driver.minimize_window()
driver.get('https://wenwen.sogou.com/')
print('进入网站')
s_login = driver.find_element_by_id('s_login')
print('点击登录')
s_login.click()
sleep(2)
# img_url = driver.get_screenshot_as_file('D:\\yzm.png')
print('获取二维码')
# driver2 = webdriver.Chrome()
# driver2.get('D:\\yzm.png')
print('扫描二维码')
#点击我要提问
sleep(15)
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/h2/a').click()


index_handle = driver.current_window_handle
for item in driver.window_handles:
    if item != index_handle:
        hd_handle = item

# List = ['有哪些温暖可爱的句子?', '大家问什么喜欢DC?', '有哪些小众的自由职业?']
# for item in List:
#定位到问题页面
sleep(1)
driver.switch_to.window(hd_handle)

kws = ['机械', '运动', '手机', '电脑']
huidas = ['创建一个Python项目', '我其实并不会这个问题', '给你提供一些思路', '双翘板很酷']
#搜索框
for k in kws:
    kw = driver.find_element_by_xpath('//*[@id="questionList"]/form/input[2]')
    kw.clear()
    kw.send_keys(k)
    sleep(1)
    # ask_title.clear()
    #点击搜索按钮
    driver.find_element_by_xpath('//*[@id="questionList"]/form/input[3]').click()
    sleep(1)
    #问题列表
    wenti_list = driver.find_elements_by_xpath('//*[@id="questionList"]/ul/li/a')
    print(wenti_list)
    for item in wenti_list:
        print(driver.window_handles)
        #点击问题
        item.click()
        for item in driver.window_handles:
            if item != index_handle and item != hd_handle:
                wenti_handle = item
        print(wenti_handle)
        #定位到回答页面
        sleep(1)
        driver.switch_to.window(wenti_handle)
        #回答框内输入回答内容
        

        try:
            hd_kuang = driver.find_element_by_id('myAnswerContent')
            hd_kuang.send_keys(random.choice(huidas))
            sleep(1)
            #选择匿名
            driver.find_element_by_id('set_anonymous').click()
            sleep(1)
            #提交
            driver.find_element_by_id('submit_answer').click()
            sleep(3)
            driver.close()
            sleep(3)
            driver.switch_to.window(hd_handle)
        except Exception as e:
            driver.close()
            sleep(3)
            driver.switch_to.window(hd_handle)


# ask_title.send_keys(item)
# sleep(1)
# driver.find_element_by_xpath('//*[@id="edit"]').click()
# sleep(1)
# driver.find_element_by_xpath('//*[@id="ask_anonymous"]').click()
# sleep(1)
# driver.find_element_by_id('submit_question').click()
# sleep(2)
# driver.back()
# print('提问成功')
# sleep(30)


