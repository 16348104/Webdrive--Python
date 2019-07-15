# coding=utf-8
import os
import win32gui
import win32con

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random

# driver = webdriver.Chrome(executable_path='C:/Users/zb/Desktop/test/python/chromedriver.exe')  # modify
driver = webdriver.Chrome()


# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Firefox(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/geckodriver')  # mac firefox
# driver = webdriver.Chrome(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/chromedriver')  # mac  chrome
# driver = webdriver.Safari() #Mac os

def time_format():
    current_time = time.strftime("%y-%m-%d %H-%M-%S", time.localtime(time.time()))
    return current_time


# pywin32
def winUpLoadFile(file_path, title):
    # 一级顶层窗口，此处title为上传窗口名称，浏览器不一样上传窗口名称不一样
    dialog = win32gui.FindWindow("#32770", title)
    # 二级窗口
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    # 三级窗口
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
    # 四级窗口
    edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
    time.sleep(1)
    # 执行操作 输入文件路径
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
    # 点击打开上传文件
    time.sleep(1)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)


##################################################登录网络学堂###########################################################
print("======登录网络学堂=====")
print('测试浏览器:' + driver.name)
# driver.get('http://learn.tsinghua.edu.cn')
driver.get("http://wlxt160.thitc.cn")
driver.maximize_window()
driver.implicitly_wait(2)
print('登录后句柄:' + driver.current_window_handle)  # 登录网络学堂，【第一个窗口】
driver.find_element_by_name('i_user').clear()
driver.find_element_by_name('i_pass').clear()
# time.sleep(30)
driver.find_element_by_name('i_user').send_keys('')  # 键入用户名
driver.find_element_by_name('i_pass').send_keys('')  # 键入密码
driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
time.sleep(2)
print(driver.title, "【第一个窗口】")
# try:
#     driver.switch_to.alert.accept('日历服务漫游失败')
# except UnexpectedAlertPresentException as msg:
#     pass
driver.find_element_by_xpath("//a[contains(text(),'60240202-0')]").click()  # 开发60240202-0
# driver.find_element_by_xpath("//a[contains(text(),'20740084-998')]").click()  # 正式20740084-998
# 【切换到第二个窗口】
window_1 = driver.current_window_handle  # 当前窗口句柄
print('课程句柄:' + window_1)
windows = driver.window_handles  # 窗口总数
for current_window in windows:
    if current_window != window_1:
        driver.switch_to.window(current_window)
time.sleep(3)
print(driver.title, "【第二个窗口】")
print('新窗口句柄:' + current_window)
print('=====登录成功=====')
# driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + 'dl-' + time_format() + ".png")  # modify截图
####################################################课程公告############################################################
# print("=====测试课程公告=====")
# driver.find_element_by_xpath("//a[@id='wlxt_kcgg_wlkc_ggb']").click()
# time.sleep(3)  # 休眠
# driver.find_element_by_xpath("//*[@id='table']/tbody/tr[1]/td[1]/a").click()
# time.sleep(2)
# ggfj = driver.find_element_by_xpath("//div[@id='ggfj']").is_displayed()
#
# print(ggfj)
# if ggfj:
#     print('预览公告附件!')
#     driver.find_element_by_xpath("//div[@id='ggfj']//a[@id='wjid']").click()  # 浏览公告附件
#     time.sleep(3)
#     # 切换【第3个窗口】
#     windows = driver.window_handles  # 窗口总数
#     driver.switch_to.window(windows[2])  # 切换到第3个窗口
#     window_2 = driver.current_window_handle
#     print('所有句柄:', windows)
#     print("当前窗口：", window_2)
#     time.sleep(3)
#     driver.switch_to.window(windows[1])  # 切换到第2个窗口
#     window_2 = driver.current_window_handle
#     print("当前窗口：", window_2)
# else:
#     print('无公告附件！')
#     driver.find_element_by_id('backBtn').click()
# print('=====公告测试完毕=====')
# time.sleep(2)
####################################################课程信息#############################################################
# print('测试课程信息')
# driver.find_element_by_css_selector('#wlxt_kc_v_kcxx_jskcxx').click()
# driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
# time.sleep(2)
# driver.execute_script("document.documentElement.scrollTop = 0;")  # 滚动条
# time.sleep(1)
# print('=======课程信息测试完毕=====')
####################################################课程文件#############################################################
# print("=====测试课程文件=====")
# driver.find_element_by_xpath("//a[@id='wlxt_kj_wlkc_kjxxb']").click()
# driver.find_element_by_xpath('//*[@id="tabbox"]/ul/li[1]/p').click()  # 电子教案类
# kjs = len(driver.find_elements_by_xpath("//i[contains(@class,'webicon-download downLoadFile')]"))
# li = driver.find_elements_by_xpath("//i[contains(@class,'webicon-download downLoadFile')]")
# print('课件总数', kjs)
# ran = random.randrange(15)  # 随机数,前[0-14)个文件
# print('随机数', ran)
# li.pop(ran).click()  # Download
# print('下载课件!')
# # element = driver.find_element_by_xpath("//div[@id='content']")
# # target = driver.find_element_by_xpath("//iframe[@id='playFrame']")
# # ActionChains(driver).drag_and_drop(element, target).perform()
# driver.find_element_by_xpath("//div[@class='playli']")
# js = "document.getElementsByClassName('playli')[0].scrollTop = 1000;"
# driver.execute_script(js)
# time.sleep(1)
# driver.switch_to.frame('playFrame')
# print('开始预览课件!')
# try:
#     Unable_preview = driver.find_element_by_xpath("//a[@class='downLoadFile']")
# except NoSuchElementException as msg:
#     print('此文件暂时无法预览', msg)
# else:
#     Unable_preview.click()
#     print('下载无法预览的文件')
#     time.sleep(3)
# try:
#     Video = driver.find_element_by_xpath("//button[@class='vjs-big-play-button']")
# except NoSuchElementException as msg:
#     print('暂无视频文件', msg)
# else:
#     Video.click()
#     print('预览视频文件')
#     time.sleep(5)
# try:
#     driver.find_element_by_css_selector("#mp3")
# except NoSuchElementException as msg:
#     print('暂无音频文件', msg)
# else:
#     js_audio = "var audio = document.getElementById('mp3');audio.play();"
#     driver.execute_script(js_audio)
#     print('预览音频文件')
#     time.sleep(2)
# try:
#     Word = driver.find_element_by_xpath("//body/a")
# except NoSuchElementException as msg:
#     print('暂无文本文件', msg)
# else:
#     Word.click()
#     js = "document.documentElement.scrollTop = 10000;"
#     driver.execute_script(js)
#     time.sleep(2)
#     print('预览文本文件')
# driver.switch_to.parent_frame()
# print('=====课件测试完毕=====')
# time.sleep(3)
####################################################课程作业############################################################
# print('=====测试课程作业=====')
# driver.find_element_by_xpath("//a[@id='wlxt_kczy_zy']").click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="wtj"]/tbody/tr[1]/td[2]/a').click()
# time.sleep(1)
# try:
#     driver.find_element_by_xpath('//input[@id="saveBtn"]')
# except NoSuchElementException:
#     print('作业过期不能提交了')
#     print(NoSuchElementException)
# else:
#     driver.find_element_by_xpath('//input[@id="saveBtn"]').click()
#     time.sleep(1)
#     print('去提交作业')
#     driver.find_element_by_xpath('//textarea[@id="s_documention"]')
#     js = "document.getElementById('s_documention').value= new Date().toLocaleDateString()"
#     driver.execute_script(js)
#     driver.find_element_by_id('fileupload').send_keys(r'D:/Homework.pdf')  # 上传文件modify
#     # driver.find_element_by_id('fileupload').send_keys(r'/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/readme.txt')  # Mac上传文件
#     driver.find_element_by_xpath("//input[@onclick='daijiao()']").click()
#     time.sleep(1)
#     try:
#         driver.find_element_by_css_selector(
#             "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
#     except NoSuchElementException as msg:
#         print('截图', msg)
#         driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'TJZY' + ".png")  # modify截图
#     else:
#         print('弹框结果:' + driver.find_element_by_css_selector(
#             "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
#
# print('=====作业测试完毕=====')
# time.sleep(4)

########################################################我的分组#########################################################
# print('测试我的分组')
# driver.find_element_by_css_selector('#wlxt_qz_v_wlkc_qzcyb').click()
# print('=====我的分组测试完毕=====')
# time.sleep(3)
######################################################课程答疑###########################################################
print('=====测试课程答疑=====')
driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
time.sleep(2)
# print('=====提问=====')
# driver.find_element_by_xpath('//*[@id="content"]//span[2]/a').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="addFormId"]//div[2]/input[1]').send_keys(time_format() + '测试课程答疑')
# driver.execute_script("document.documentElement.scrollTop = 10000;")
# # 富文本音频win32gui
# driver.find_element_by_xpath('//*[@id="cke_41"]').click()
# time.sleep(1)
# try:
#     winUpLoadFile("D:\Artists.mp3", "打开")
# except UnexpectedAlertPresentException as msg:
#     print(driver.switch_to.alert.text)
#     driver.switch_to.alert.accept()
# # AutoIt v3
# # os.system("D:/Audio.exe")
# time.sleep(5)
# # 富文本视频win32gui
# driver.find_element_by_xpath('//*[@id="cke_41"]').click()
# time.sleep(1)
# try:
#     winUpLoadFile("D:\mov.mp4", "打开")  # 往输入框输入绝对地址D:\modify
# except UnexpectedAlertPresentException as msg:
#     print(driver.switch_to.alert.text)
#     driver.switch_to.alert.accept()
# # AutoIt v3
# # os.system("D:/Video.exe")
# time.sleep(10)
# driver.find_element_by_xpath('//*[@id="saveBtn"]').click()
# time.sleep(1)
# try:
#     driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
# except NoSuchElementException as msg:
#     print('截图', msg)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'TWDY' + ".png")  # modify截图
# else:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(3)
# print('=====编辑未答问题=====')
# driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//tr[1]//td[4]//a[1]').click()
# time.sleep(1)
# driver.find_element_by_xpath("//a[@class='ml-10 show-textar']").click()
# time.sleep(1)
# # CKeditor数学公式
# driver.find_element_by_xpath("//a[@id='cke_39']").click()
# js = "document.getElementsByClassName('cke_dialog_background_cover')[0].style.display = 'none'"
# driver.execute_script(js)
# driver.find_element_by_xpath("//a[contains(@class,'ok')]").click()  # 动态id
# time.sleep(2)
# # 上传答疑文件
# driver.find_element_by_id('fileupload').send_keys(r'D:/Homework.pdf')  # modify
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="saveTltBtn"]').click()
# time.sleep(1)
# print('弹框结果:' + driver.find_element_by_css_selector(
#     "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(5)
print('=====查看已回答问题=====')
# driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
# time.sleep(2)
driver.find_element_by_xpath('//*[@id="tabbox"]/ul/li[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]//td[6]//a[1]').click()
time.sleep(2)
driver.execute_script("document.documentElement.scrollTop = 10000;")
time.sleep(1)
# Play Audio
try:
    driver.find_element_by_xpath("//audio")
except NoSuchElementException as msg_MP3:
    print('无音频文件', msg_MP3)
else:
    print('预览音频文件')
    js_audio = "var audio = document.getElementsByTagName('audio')[0];audio.play();"
    driver.execute_script(js_audio)
    time.sleep(5)
# Play Video
try:
    driver.find_element_by_xpath("//video")
except NoSuchElementException as msg_MP4:
    print('无视频文件', msg_MP4)
else:
    print('预览视频文件')
    js_video = "var video = document.getElementsByTagName('video')[0];video.play();"
    driver.execute_script(js_video)
    time.sleep(5)
# 下载全部答疑附件
print('下载全部已回复的答疑文件')
try:
    driver.find_element_by_xpath('//*[@id="hfjg"]//a[@id="removeFile"]')  # 全部教师的答疑文件
except NoSuchElementException as msg:
    print('无答疑附件', msg)
else:
    Downloads = driver.find_elements_by_xpath('//*[@id="hfjg"]//a[@id="removeFile"]')
    print(Downloads)
    for i in Downloads:
        i.click()
        time.sleep(1)
driver.execute_script("document.documentElement.scrollTop = 10000;")
# print('=====继续提问=====')
# driver.find_element_by_xpath('//a[@class="ml-10 show-textar"]').click()
# # CKeditor上传图片
# driver.find_element_by_xpath("//a[@id='cke_40']").click()
# os.system("D:/image.exe")
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="saveBtn"]').click()
# time.sleep(2)
# try:
#     driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
# except NoSuchElementException as msg:
#     print('截图', msg)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'KCDY' + ".png")  # modify截图
# else:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(3)
print('=====查看问题集锦=====')
driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
# driver.back()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="tabbox"]/ul/li[3]').click()
time.sleep(2)
driver.find_element_by_xpath('//tr[1]//td[2]/a').click()
time.sleep(3)
driver.execute_script("document.documentElement.scrollTop = 10000;")
time.sleep(1)
# Play Audio
try:
    driver.find_element_by_xpath("//p[@id='wtnr']//p//audio")
except NoSuchElementException as msg_MP3:
    print('无音频文件', msg_MP3)
else:
    print('预览音频文件')
    js_audio = "var audio = document.getElementsByTagName('audio')[0];audio.play();"
    driver.execute_script(js_audio)
    time.sleep(5)
# Play Video
try:
    driver.find_element_by_xpath("//p[@id='wtnr']//p//video")
except NoSuchElementException as msg_MP4:
    print('无视频文件', msg_MP4)
else:
    print('预览视频文件')
    js_video = "var video = document.getElementsByTagName('video')[0];video.play();"
    driver.execute_script(js_video)
    time.sleep(5)
# 随机下载答疑附件
print('随机下载问题集锦文件')
try:
    driver.find_element_by_xpath('//a[@id="removeFile"]')
except NoSuchElementException as msg:
    print('无答疑附件', msg)
else:
    key = len(driver.find_elements_by_xpath('//a[@id="removeFile"]'))
    print("答疑附件个数", key)
    ran = random.randrange(key)
    print('随机数', ran)
    driver.find_elements_by_xpath('//a[@id="removeFile"]').pop(ran).click()
print('=====答疑测试完毕=====')
time.sleep(1)
####################################################课程邮件#############################################################
# print('=====测试课程邮件=====')
# driver.find_element_by_xpath("//a[@id='wlxt_mail_yj_yjxxb']").click()
# time.sleep(2)
# driver.find_element_by_xpath('//span[@class="rt right"]/child::a').click()  # 去发邮件
# addresses = driver.find_elements_by_xpath("//span[contains(@class,'text-icon')]")
# for i in addresses:
#     # if i.get_attribute('text') != '肖大兴':
#     i.click()
#     time.sleep(1)
# driver.find_element_by_xpath('//ul[@id="myTags"]//li//input').send_keys('wlxt@tsinghua.edu.cn')
# driver.find_element_by_xpath('//ul[@id="myTags"]//li//input').send_keys(Keys.ENTER)
# time.sleep(1)
# # driver.find_element_by_xpath('//ul[@id="myTags"]//li[2]/input').send_keys('谢素萍')
# # driver.find_element_by_xpath('//ul[@id="myTags"]//li[2]//input').send_keys(Keys.ENTER)
# # time.sleep(1)
# # driver.find_element_by_xpath('//ul[@id="myTags"]//li[3]/input').send_keys('杜娟')
# # driver.find_element_by_xpath('//ul[@id="myTags"]//li[3]//input').send_keys(Keys.ENTER)
# # time.sleep(1)
# js = "document.getElementById('bt').value = new Date().toLocaleString();"
# val = driver.execute_script(js)
# driver.find_element_by_xpath('//input[@id="bt"]').send_keys('网络学堂自动化测试结果—学生端功能正常')
# iframe = driver.find_element_by_xpath("//iframe[contains(@title,'nrStr')]")  # 定位iframe
# driver.switch_to.frame(iframe)  # 切入iframe
# driver.find_element_by_xpath("//body[starts-with(@class,'cke')]").send_keys('学生端功能正常')
# driver.switch_to.default_content()  # 跳出iframe
# # driver.find_element_by_id('fileupload').send_keys(r'/Users/xiaodaxing/Desktop/Race.pdf')  # Mac上传文件
# driver.find_element_by_id('fileupload').send_keys(r'C:/Users/zb/Desktop/test/python/review.docx')  # modify
# time.sleep(1)
# driver.find_element_by_xpath('//input[@id="submitButton"]').click()
# time.sleep(1)
# print('弹框结果:' + driver.find_element_by_css_selector(
#     "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(4)
# print('浏览邮件')
# driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]/a').click()  # 浏览邮件
# driver.find_element_by_id('returnButton').click()
# print('=====邮件测试完毕=====')
# time.sleep(5)
##################################################退出网络学堂############################################################
driver.find_element_by_xpath("//i[@class='webicon-out']").click()
time.sleep(2)
driver.find_element_by_xpath("//div[contains(@class,'zeromodal-footer')]//button[contains(text(),'确定')]").send_keys(
    Keys.ENTER)
print('=====退出网络学堂=====')
# js = "alert('12345')"
# driver.execute_script(js)
# driver.switch_to_alert().accept()
# driver.switch_to.alert.accept()
# cookie = driver.get_cookies()
# print(cookie)
driver.delete_all_cookies()
time.sleep(1)
driver.quit()
print('关闭浏览器，删除cookie')
