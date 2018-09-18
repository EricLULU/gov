from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 


url = "http://www.gsxt.gov.cn/index.html"
browser = webdriver.Firefox()  #声明浏览器
wait = WebDriverWait(browser, 60)   #指定延时时间
browser.get(url)

def spider(name):
    #寻找搜索框和搜索按钮
    in_put = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#keyword')))
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btn_query')))

    #输入企业名称
    in_put.clear()     #清空输入信息， 每次都要
    in_put.send_keys(name)  #输入信息
    submit.click()     #点击提交按钮
    
    #然后人工确认极验验证码

    #等待网页跳转后，搜索提取公司名称
    title = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'h1')))
    for title in browser.find_elements_by_css_selector('h1'):
        print(title.text)

def main():
    name = input("输入企业名称:")
    spider(name)

if __name__ == '__main__':
    main()