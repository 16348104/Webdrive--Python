# coding=utf-8
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(
#     executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/chromedriver')  # mac  chrome
# driver = webdriver.Firefox(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/geckodriver')# mac  firefox
print("======登录阿里云监控=====")
print('测试浏览器:' + driver.name)
driver.get('https://cloudmonitor.console.aliyun.com')
driver.maximize_window()
time.sleep(10)
driver.switch_to.frame('alibaba-login-box')  # 切入框架
driver.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()
# driver.find_element_by_xpath('//input[@id="fm-login-id"]').send_keys('')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('')
# driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').send_keys(
#     Keys.ENTER)
date = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/div[2]/p').text
print(date)
time.sleep(15)
driver.switch_to.default_content()
time.sleep(2)
# driver.find_element_by_css_selector(
#     'body > div.viewframeContainer > div.aliyun-console-help-guide > div.help-guide-step.help-guide-step-1 > div.help-guide-step-header > button > i').click()
time.sleep(2)
print('站点监控')
driver.get(
    'https://cloudmonitor.console.aliyun.com/?spm=5176.2020520111.aliyun_sidebar.aliyun_sidebar_cms.6ff9d103iaAGn8#/home/ecs')
time.sleep(4)
print('站点管理')
driver.get(
    'https://cloudmonitor.console.aliyun.com/?spm=5176.12818093.aliyun_sidebar.aliyun_sidebar_cms.488716d0VtQA3i#/newSite/list/')
time.sleep(7)
driver.find_element_by_xpath("//span[contains(text(),'网络学堂应用服务监控2')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@class='icon-collapse-left']").click()
time.sleep(13)
print('截图')
# driver.save_screenshot('/Users/xdx/Desktop/Monitor.png')  # mac
driver.save_screenshot('D:/Monitor.png')
time.sleep(3)
##发邮件
print('去发邮件!')
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# 发送邮件服务器
smtpsever = 'smtp.126.com'
# 用户名密码
# password = input("input:")
password = 'xdx2019'
user = 'xiaodaxing@126.com'
# 发件箱
sender = 'xiaodaxing@126.com'
# 收件箱
receiver = ['47283875@qq.com', 'wlxt@tsinghua.edu.cn']
# 邮件主题
subject = '阿里云监控截图'
# HTML类型邮件正文
msgRoot = MIMEText('<html><h3>Python Mail</h3></html>', 'html', 'utf-8')
# msgRoot = MIMEText('此为系统测试邮件，请勿直接回复！', 'plain', 'utf-8')
# mail_msg = 'Hello,Our task is done.'
sendfile = open('D:/Monitor.png', 'rb').read()
att = MIMEText(sendfile, 'png', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="Monitor.png"'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot['From'] = user
msgRoot.attach(att)
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(smtpsever, 25)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
print('Success,Email has send out!')
current_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time()))
print(current_time, '退出cloudmonitor')
# os.open('E:/WebDriver--Python/Example/Email/send_mail2.py')
driver.delete_all_cookies()
print('关闭浏览器，删除cookie')
time.sleep(1)
driver.quit()

