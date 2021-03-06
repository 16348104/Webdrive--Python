# coding=utf-8
import os
import re
import win32gui
import win32con
import win32api
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, \
    ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random

# 配置Firefox文件下载
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('browser.download.folderList', 0)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                       'application/zip,application/xhtml+xml,application/xml,application/x-msdownload,application/octet/octet-stream,application/exe,txt/csv,application/pdf,application/x-msexcl,application/x-excel,application/excel,image/png,image/jpeg,text/html,text/plain,text/x-c')
# driver = webdriver.Firefox(firefox_profile=profile)
driver = webdriver.Chrome()
# driver = webdriver.Ie()
driver.delete_all_cookies()
time.sleep(1)


# driver = webdriver.Firefox(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/geckodriver')  # mac firefox
# driver = webdriver.Chrome(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/chromedriver')  # mac  chrome
# driver = webdriver.Safari() #Mac os
# 格式化时间
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
    # 执行操作 输入文件路径
    time.sleep(1)
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
    # 点击打开上传文件
    time.sleep(1)
    try:
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    except Exception as msg_alert:
        driver.get_screenshot_as_file(
            "C:/Users/zb/Downloads/FireShot/" + time_format() + 'ckeditor' + ".png")  # modify截图
        print('截图', msg_alert)  # 上传文件失败
        driver.switch_to.alert.accept()


##################################################登录网络学堂###########################################################
print("======登录网络学堂=====")
print('测试浏览器:' + driver.name)
# driver.get('http://learn.tsinghua.edu.cn')
driver.get("http://wlxt160.thitc.cn")
driver.maximize_window()
# 登录网络学堂，第一个窗口
print('登录后句柄:' + driver.current_window_handle)
driver.find_element_by_name('i_user').clear()
driver.find_element_by_name('i_pass').clear()
# time.sleep(30)
driver.find_element_by_name('i_user').send_keys('2014013024')
# driver.find_element_by_name('i_user').send_keys('2010010545')
driver.find_element_by_name('i_pass').send_keys('123')
# user = input('name:')
# password = input('pw:"')
# driver.find_element_by_name("i_user").send_keys(user)
# driver.find_element_by_name("i_pass").send_keys(password)
# time.sleep(2)
driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
time.sleep(2)
print(driver.title, "第1个窗口")
# try:
#     driver.switch_to.alert.accept('日历服务漫游失败')
# except UnexpectedAlertPresentException as msg:
#     pass
driver.find_element_by_xpath("//a[contains(text(),'60240202-0')]").click()  # 开发60240202-0
# driver.find_element_by_xpath("//a[contains(text(),'20740084-998')]").click()  # 正式20740084-998
time.sleep(2)
# 切换到第二个窗口
window_1 = driver.current_window_handle  # 当前窗口句柄
print('课程句柄:' + window_1)
windows = driver.window_handles  # 窗口总数
for current_window in windows:
    if current_window != window_1:
        driver.switch_to.window(current_window)
time.sleep(3)
print(driver.title, "第2个窗口")
print('新窗口句柄:' + current_window)
print('=====登录成功=====')
print('登录时间：', time_format())
time.sleep(3)
# driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + 'DL-' + time_format() + ".png")  # modify截图
####################################################课程公告############################################################
# print("=====测试课程公告=====")
# driver.find_element_by_xpath("//a[@id='wlxt_kcgg_wlkc_ggb']").click()
# time.sleep(3)  # 休眠
# driver.find_element_by_xpath("//*[@id='table']/tbody/tr[1]/td[1]/a").click()
# time.sleep(2)
# ggfj = driver.find_element_by_xpath("//div[@id='ggfj']").is_displayed()
#
# print('是否含有附件:', ggfj)
# if ggfj:
#     print('预览公告附件!')
#     driver.find_element_by_xpath("//div[@id='ggfj']//a[@id='wjid']").click()  # 浏览公告附件
#     time.sleep(2)
#     # 切换第3个窗口
#     windows = driver.window_handles  # 窗口总数
#     driver.switch_to.window(windows[2])  # 切换到第3个窗口
#     window_2 = driver.current_window_handle
#     print('所有句柄:', windows)
#     print("当前窗口：", window_2)
#     time.sleep(2)
#     driver.close()
#     driver.switch_to.window(windows[1])  # 切换到第2个窗口
#     window_2 = driver.current_window_handle
#     print("当前窗口：", window_2)
# else:
#     print('无公告附件！')
#     driver.find_element_by_id('backBtn').click()
# print('=====公告测试完毕=====')
# time.sleep(2)
####################################################课程信息#############################################################
# print('=====测试课程信息=====')
# driver.find_element_by_css_selector('#wlxt_kc_v_kcxx_jskcxx').click()
# driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
# time.sleep(2)
# driver.execute_script("document.documentElement.scrollTop = 0;")  # 滚动条
# print('=======课程信息测试完毕=====')
# time.sleep(2)
####################################################课程文件#############################################################
# print("=====测试课程文件=====")
# driver.find_element_by_xpath("//a[@id='wlxt_kj_wlkc_kjxxb']").click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="tabbox"]/ul/li[1]/p').click()  # 电子教案类
# time.sleep(3)
# kjs = len(driver.find_elements_by_xpath("//i[contains(@class,'webicon-download downLoadFile')]"))
# li = driver.find_elements_by_xpath("//i[contains(@class,'webicon-download downLoadFile')]")
# print('课件总数', kjs)
# ran = random.randrange(15)  # 随机数,前[0-14)个文件
# print('随机数', ran)
# li.pop(ran).click()  # Download
# print('下载课件')
# # element = driver.find_element_by_xpath("//div[@id='content']")
# # target = driver.find_element_by_xpath("//iframe[@id='playFrame']")
# # ActionChains(driver).drag_and_drop(element, target).perform()
# driver.find_element_by_xpath("//div[@class='playli']")
# js = "document.getElementsByClassName('playli')[0].scrollTop = 1000;"
# driver.execute_script(js)
# time.sleep(1)
# driver.switch_to.frame('playFrame')
# print('开始预览课件')
# # 无法预览的文件
# try:
#     driver.find_element_by_xpath("//a[@class='downLoadFile']").click()
#     print('下载无法预览的文件')
#     time.sleep(3)
# except NoSuchElementException as msg:
#     print('压缩文件暂时无法预览', msg)
# # Play Video
# try:
#     driver.find_element_by_xpath("//button[@class='vjs-big-play-button']").click()
#     print('预览视频文件!')
#     time.sleep(5)
# except NoSuchElementException as msg:
#     print('暂无视频文件', msg)
# # Play Audio
# try:
#     driver.find_element_by_css_selector("#mp3")
#     js_audio = "var audio = document.getElementById('mp3');audio.play();"
#     driver.execute_script(js_audio)
#     print('预览音频文件!')
#     time.sleep(2)
# except NoSuchElementException as msg:
#     print('暂无音频文件', msg)
# # 预览文本
# try:
#     driver.find_element_by_xpath("//body/a").click()
#     time.sleep(2)
#     print('预览文本文件!')
# except NoSuchElementException as msg:
#     print('暂无文本文件', msg)
# driver.switch_to.parent_frame()
# time.sleep(2)
# print('=====课件测试完毕=====')
# time.sleep(1)
####################################################课程作业############################################################
# print('=====测试课程作业=====')
# driver.find_element_by_xpath("//a[@id='wlxt_kczy_zy']").click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="wtj"]/tbody/tr[1]/td[2]/a').click()
# time.sleep(1)
# try:
#     driver.find_element_by_xpath('//input[@id="saveBtn"]')
# except NoSuchElementException as msg:
#     print('作业逾期不能提交!', msg)
# else:
#     driver.find_element_by_xpath('//input[@id="saveBtn"]').click()
#     time.sleep(1)
#     print('去提交作业')
#     driver.find_element_by_xpath("//p[@class='zhan']").click()  # 展开查看更多
#     time.sleep(2)
#     print("下载作业附件")
#     try:
#         driver.find_element_by_xpath("//a[@class='ml-10']").click()
#     except NoSuchElementException as msg:
#         print("无作业附件", msg)
#     driver.find_element_by_xpath('//textarea[@id="s_documention"]')
#     js = "document.getElementById('s_documention').value= new Date().toLocaleDateString()"
#     driver.execute_script(js)
#     driver.find_element_by_id('fileupload').send_keys(r'D:\Homework.pdf')  # 上传文件modify
#     # driver.find_element_by_id('fileupload').send_keys(r'/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/readme.txt')  # Mac上传文件
#     driver.find_element_by_xpath("//input[@onclick='daijiao()']").click()
#     time.sleep(1)
#     try:
#         print('弹框结果:' + driver.find_element_by_css_selector(
#             "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
#     except NoSuchElementException as msg:
#         print('截图', msg)
#         driver.get_screenshot_as_file(
#             "C:/Users/zb/Downloads/FireShot/" + time_format() + 'TJZY' + ".png")  # modify截图
# print('=====作业测试完毕=====')
# time.sleep(3)
########################################################我的分组#########################################################
# print('=====测试我的分组=====')
# driver.find_element_by_xpath('//*[@id="wlxt_qz_v_wlkc_qzcyb"]').click()
# print('=====我的分组测试完毕=====')
# time.sleep(2)
####################################################课程讨论#############################################################
print('=====测试课程讨论=====')
driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_tltb"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/a').click()
time.sleep(2)
print('浏览讨论帖')
# 隐藏讨论区顶部的蓝条
driver.execute_script('document.getElementById("tlbt").style.display="none"')
#  Play Audio
try:
    driver.find_element_by_xpath("//p[@id='wtnr']//p//audio")
    print('预览音频文件')
    js_audio = "var audio = document.getElementsByTagName('audio')[0];audio.play();"
    driver.execute_script(js_audio)
    time.sleep(5)
except NoSuchElementException as msg_MP3:
    print('无音频文件', msg_MP3)
# Play Video
try:
    driver.find_element_by_xpath("//p[@id='wtnr']//p//video")
    print('预览视频文件!')
    js_video = "var video = document.getElementsByTagName('video')[0];video.play();"
    driver.execute_script(js_video)
    time.sleep(5)
except NoSuchElementException as msg_MP4:
    print('无视频文件', msg_MP4)
print('下载楼主的附件')
try:
    driver.find_element_by_xpath("//*[@id='answerFirstLink']/preceding::a[@id='']").click()
except NoSuchElementException as msg:
    print('楼主没有附件!', msg)
print('回复楼主')
driver.find_element_by_xpath('//*[@id="answerFirstLink"]').click()
time.sleep(3)
# 切换编辑器
driver.find_element_by_xpath('//*[@id="editFirstAnswerFormId"]/div[1]/p/span[2]').click()
time.sleep(3)
print('CKeditor传音频文件')
driver.find_element_by_xpath('//*[@id="cke_41"]').click()
time.sleep(3)
try:
    winUpLoadFile("D:\Artists.mp3", "打开")  # 往输入框输入绝对地址D:\modify
    time.sleep(2)
except UnexpectedAlertPresentException as msg_alert:
    print('截图', msg_alert)
    driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'ckeditor' + ".png")  # modify截图
    driver.switch_to.alert.accept()
time.sleep(5)
# # 上传答疑文件
driver.find_element_by_id('fileupload0').send_keys(r'D:\Homework.pdf')  # modify
time.sleep(1)
# 发表话题
driver.find_element_by_xpath("//div[@class='rt huifu']//input").click()
time.sleep(3)
try:
    print('弹框结果:' + driver.find_element_by_css_selector(
        "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
except NoSuchElementException as msg:
    print('截图', msg)
    driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'HT' + ".png")  # modify截图
# driver.execute_script("document.documentElement.scrollTop = 0;")
time.sleep(3)
print('回复自己的跟帖')
driver.refresh()
try:
    # 回复自己的跟帖
    driver.find_element_by_xpath("//*[starts-with(@onclick,'delHf')]/following-sibling::*[@class='huifu']")
except NoSuchElementException as msg:
    print('暂无回复', msg)
else:
    hf_list = len(
        driver.find_elements_by_xpath("//*[starts-with(@onclick,'delHf')]/following-sibling::*[@class='huifu']"))
    ran_hf = random.randrange(hf_list)
    print('随机数', ran_hf)
    # 获取回复楼层id
    span_first = driver.find_elements_by_xpath(
        "//*[starts-with(@onclick,'delHf')]/following-sibling::*[@class='huifu']//*[contains(@id,'span_first')]").pop(
        ran_hf)
    item = span_first.get_attribute('id')
    print('span元素ID:' + item)
    num = re.sub(r'\D', '', item)
    print("定位回复楼层id:", num)
    ###此功能暂不使用###
    # 定位回复他人文本域
    # textarea = "//*[contains(@id," + "\'" + num + "\'" + ")]//*[@name='nr']"
    # 定位点击查看其他人跟帖
    # click_span = "//*[contains(@id," + "\'" + num + "\'" + ")]//*[@id='hufuitem']/a"
    ########
    # 定位发表按钮 //div[contains(@id,'38380462')]//input[@class='rt count_submit']
    submit = "//*[contains(@id," + "\'" + num + "\'" + ")]//*[@class='rt count_submit']"
    # 定位切换编辑器 //div[contains(@id,'38380462')]//span[@class='rt toeditor']
    switch_span = "//*[contains(@id," + "\'" + num + "\'" + ")]//*[@class='rt toeditor']"
    # 定位添加附件   //input[@id='fileupload38380462']
    str1 = "fileupload"
    add_attch = "//*[@id=" + "\'" + str1 + num + "\'" + "]"
    print('学生对楼主回复帖总数:', hf_list)
    print('回复贴楼层:', ran_hf + 2)
    # 点回复
    driver.find_elements_by_xpath(
        "//*[starts-with(@onclick,'delHf')]/following-sibling::*[@class='huifu']").pop(
        ran_hf).click()
    # element1 = driver.find_elements_by_xpath(
    #     "//*[starts-with(@onclick,'delHf')]/following-sibling::*[@class='huifu']").pop(
    #     ran_hf)
    # driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    # 切换ckeditor
    driver.find_element_by_xpath(switch_span).click()
    print('定位切换编辑器:',switch_span)
    time.sleep(2)
    # driver.find_elements_by_xpath("//div[@id='mypanel']//span[contains(@class,'toeditor')]").pop(ran_hf).click()
    try:
        # 加富文本表情
        driver.find_element_by_xpath('//a[@id="cke_117"]')
    except NoSuchElementException as msg:
        driver.refresh()
        time.sleep(3)
    else:
        driver.find_element_by_xpath('//a[@id="cke_117"]').click()
        js = "document.getElementsByClassName('cke_dialog_background_cover')[0].style.display = 'none'"
        driver.execute_script(js)
        time.sleep(5)
        driver.find_element_by_xpath('//*/table/tbody/tr[1]/td[1]/a/img').click()
        time.sleep(5)
        print('上传回复附件')
        driver.find_element_by_xpath(add_attch).send_keys(r'D:\Homework.pdf')  # modify
        time.sleep(2)
        print('发表自己的跟帖')
        # driver.execute_script("document.documentElement.scrollTop = 10000;")
        # element2 = driver.find_element_by_xpath(submit)
        # driver.execute_script("arguments[0].click();", element2)
        print('回复按钮:', submit)
        driver.find_element_by_xpath(submit).click()
        # print('回复按钮:', submit)
        time.sleep(2)
        try:
            print('弹框结果:' + driver.find_element_by_css_selector(
                "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
        except NoSuchElementException as msg:
            print('截图', msg)
            driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'HD' + ".png")  # modify截图
driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_tltb"]').click()
print('浏览我参与的讨论话题')
driver.find_element_by_xpath("//*[@id='canyu']").click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="canyutable"]/tbody/tr[1]/td[2]/a').click()
time.sleep(2)
# 隐藏讨论区顶部的蓝条
driver.execute_script('document.getElementById("tlbt").style.display="none"')
# Play Video
try:
    driver.find_element_by_xpath("//video")
    print('预览视频文件!')
    js_video = "var video = document.getElementsByTagName('video')[0];video.play();"
    driver.execute_script(js_video)
    time.sleep(3)
except NoSuchElementException as msg_MP4:
    print('无视频文件', msg_MP4)
# Play Audio
try:
    driver.find_element_by_xpath('//audio')
    print('预览音频文件!')
    js_audio = "var audio = document.getElementsByTagName('audio')[0];audio.play();"
    driver.execute_script(js_audio)
    time.sleep(3)
except NoSuchElementException as msg_MP3:
    print('无音频文件', msg_MP3)

print('随机下载讨论附件')
try:
    driver.find_element_by_xpath("//*[@id='removeFile']")
except NoSuchElementException as msg:
    print('无子回复附件', msg)
else:
    key = len(driver.find_elements_by_xpath("//*[@id='removeFile']"))
    print("子回复附件个数:", key)
    ran = random.randrange(key)
    print('讨论附件随机数:', ran)
    driver.find_elements_by_xpath("//*[@id='removeFile']").pop(ran).click()
print('回复我参与的话题')
driver.find_element_by_xpath('//*[@id="answer_first"]').send_keys('Textarea我参与的话题')
time.sleep(1)
driver.find_element_by_xpath('//div[@class="rt huifu"]//input').click()
time.sleep(1)
try:
    print('弹框结果:' + driver.find_element_by_css_selector(
        "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
except NoSuchElementException as msg:
    print('截图', msg)
    driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'FBHT' + ".png")  # modify截图
print('=====课程讨论测试完毕=====')
time.sleep(3)
######################################################课程答疑###########################################################
# print('=====测试课程答疑=====')
# driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
# time.sleep(1)
# print('学生提问')
# driver.find_element_by_xpath('//*[@id="content"]//span[2]/a').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="addFormId"]//div[2]/input[1]').send_keys(time_format() + '测试课程答疑')
# driver.execute_script("document.documentElement.scrollTop = 10000;")
# # 富文本视频win32gui
# try:
#     driver.find_element_by_xpath('//*[@id="cke_41"]')
# except NoSuchElementException as msg_MP4:
#     print('CKeditor未加载,刷新一次浏览器!', msg_MP4)
#     driver.refresh()
#     time.sleep(2)
# driver.find_element_by_xpath('//*[@id="cke_41"]').click()
# time.sleep(1)
# winUpLoadFile("D:\mov.mp4", "打开")  # 往输入框输入绝对地址D:\modify
# time.sleep(5)
# print('ckeditor传MP4')
# # AutoIt v3
# # os.system("D:/Video.exe")
# print('上传答疑附件')
# driver.find_element_by_id('fileupload').send_keys(r'D:\Photo.jpg')  # modify
# driver.find_element_by_xpath('//*[@id="saveBtn"]').click()
# time.sleep(2)
# try:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# except NoSuchElementException as msg:
#     print('截图', msg)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'TW' + ".png")  # modify截图
# time.sleep(3)
# print('编辑未答问题')
# driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
# driver.find_element_by_xpath('//tr[1]//td[4]//a[1]').click()
# time.sleep(1)
# # 编辑答疑
# driver.find_element_by_xpath("//a[@class='ml-10 show-textar']").click()
# time.sleep(2)
# # 富文本音频win32gui
# try:
#     driver.find_element_by_xpath('//*[@id="cke_41"]')
# except NoSuchElementException as msg_MP4:
#     print('CKeditor未加载，刷新一次浏览器!', msg_MP4)
#     driver.refresh()
#     time.sleep(1)
# # finally:
# driver.find_element_by_xpath('//*[@id="cke_41"]').click()
# time.sleep(1)
# winUpLoadFile("D:\Artists.mp3", "打开")
# time.sleep(5)
# print('ckeditor传MP3')
# # AutoIt v3
# # os.system("D:/Audio.exe")
# # 保存
# driver.find_element_by_xpath('//*[@id="saveTltBtn"]').click()
# time.sleep(1)
# try:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# except NoSuchElementException as msg_mp3:
#     print("截图", msg_mp3)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'BJTW' + ".png")  # modify截图
# time.sleep(5)
# print('查看已回答问题')
# driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
# # 已回答问题tab
# driver.find_element_by_xpath('//*[@id="tabbox"]/ul/li[2]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]//td[6]//a[1]').click()
# time.sleep(2)
# # 下载全部答疑附件
# print('下载全部已回复的答疑文件')
# try:
#     driver.find_element_by_xpath('//*[@id="hfjg"]//a[@id="removeFile"]')  # 全部教师的答疑文件
# except NoSuchElementException as msg:
#     print('无答疑附件', msg)
# else:
#     Downloads = driver.find_elements_by_xpath('//*[@id="hfjg"]//a[@id="removeFile"]')
#     print('已回复答疑附件数:', len(Downloads))
#     for i in Downloads:
#         try:
#             i.click()
#             time.sleep(1)
#         except ElementNotInteractableException as msg:
#             print('未加载答疑附件', msg)
#             driver.refresh()
#             time.sleep(2)
#             driver.find_elements_by_xpath('//*[@id="hfjg"]//a[@id="removeFile"]').pop(0).click()
# driver.execute_script("document.documentElement.scrollTop = 10000;")
# time.sleep(1)
# # Play Audio
# try:
#     driver.find_element_by_xpath("//audio")
#     print('预览音频文件!')
#     js_audio = "var audio = document.getElementsByTagName('audio')[0];audio.play();"
#     driver.execute_script(js_audio)
#     time.sleep(5)
# except NoSuchElementException as msg_MP3:
#     print('无音频文件', msg_MP3)
#
# # Play Video
# try:
#     driver.find_element_by_xpath("//video")
#     print('预览视频文件!')
#     js_video = "var video = document.getElementsByTagName('video')[0];video.play();"
#     driver.execute_script(js_video)
#     time.sleep(5)
# except NoSuchElementException as msg_MP4:
#     print('无视频文件', msg_MP4)

######等待正式环境修改############
# print('=====继续提问=====')
# driver.find_element_by_xpath('//a[@class="ml-10 show-textar"]').click()
# # CKeditor上传图片
# driver.find_element_by_xpath("//a[@id='cke_40']").click()
# # os.system("D:/image.exe")
# # time.sleep(3)
# driver.find_element_by_xpath('//*[@id="saveBtn"]').click()
# time.sleep(2)
# try:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# except NoSuchElementException as msg:
#     print('截图', msg)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'KCDY' + ".png")  # modify截图
# time.sleep(3)
####################################################################################
# print('查看问题集锦')
# driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="tabbox"]/ul/li[3]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//tr[1]//td[2]/a').click()
# time.sleep(3)
# driver.execute_script("document.documentElement.scrollTop = 10000;")
# time.sleep(1)
# # Play Audio
# try:
#     driver.find_element_by_xpath("//p[@id='wtnr']//p//audio")
#     print('预览音频文件')
#     js_audio = "var audio = document.getElementsByTagName('audio')[0];audio.play();"
#     driver.execute_script(js_audio)
#     time.sleep(5)
# except NoSuchElementException as msg_MP3:
#     print('无音频文件', msg_MP3)
# # Play Video
# try:
#     driver.find_element_by_xpath("//p[@id='wtnr']//p//video")
#     print('预览视频文件')
#     js_video = "var video = document.getElementsByTagName('video')[0];video.play();"
#     driver.execute_script(js_video)
#     time.sleep(5)
# except NoSuchElementException as msg_MP4:
#     print('无视频文件', msg_MP4)
# # 随机下载答疑附件
# print('随机下载问题集锦文件')
# try:
#     driver.find_element_by_xpath('//a[@id="removeFile"]')
# except NoSuchElementException as msg:
#     print('无答疑附件', msg)
# else:
#     key = len(driver.find_elements_by_xpath('//a[@id="removeFile"]'))
#     print("答疑附件个数", key)
#     ran = random.randrange(key)
#     print('随机数', ran)
#     try:
#         time.sleep(1)
#         driver.find_elements_by_xpath('//a[@id="removeFile"]').pop(ran).click()
#     except ElementNotInteractableException as msg:
#         print('未加载文件', msg)
#         driver.refresh()
#         time.sleep(3)
#         driver.find_elements_by_xpath('//a[@id="removeFile"]').pop(0).click()
# print('=====答疑测试完毕=====')
# time.sleep(2)
####################################################课程邮件############################################################
print('=====测试课程邮件=====')
driver.find_element_by_xpath("//a[@id='wlxt_mail_yj_yjxxb']").click()
time.sleep(1)
driver.find_element_by_xpath('//*[@class="detail"]//i').click()
print('浏览邮件')
driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]/a').click()  # 浏览邮件
time.sleep(1)
# driver.find_element_by_id('returnButton').click()
driver.back()
time.sleep(3)
driver.find_element_by_xpath('//span[@class="rt right"]/child::a[2]').click()  # 去发邮件
# addresses = driver.find_elements_by_xpath("//span[contains(@class,'text-icon')]")
# for i in addresses:
#     # if i.get_attribute('text') != '肖大兴':
#     i.click()
#     time.sleep(1)
driver.find_element_by_xpath('//ul[@id="myTags"]//li[1]//input').send_keys('wlxt@tsinghua.edu.cn')
driver.find_element_by_xpath('//ul[@id="myTags"]//li[1]//input').send_keys(Keys.ENTER)
time.sleep(2)
# driver.find_element_by_xpath('//ul[@id="myTags"]//li[2]/input').send_keys('谢老师')
# driver.find_element_by_xpath('//ul[@id="myTags"]//li[2]//input').send_keys(Keys.ENTER)
# time.sleep(1)
# driver.find_element_by_xpath('//ul[@id="myTags"]//li[3]/input').send_keys('杜娟')
# driver.find_element_by_xpath('//ul[@id="myTags"]//li[3]//input').send_keys(Keys.ENTER)

# 正式环境不抄送本人
# print("抄送到本人邮箱")
# driver.find_element_by_xpath('//label[@class="mycheck"]').click()
js = "document.getElementById('bt').value = new Date().toLocaleString();"
val = driver.execute_script(js)
driver.find_element_by_xpath('//input[@id="bt"]').send_keys('wlxt160自动化测试结果—学生端功能正常')
# 定位iframe
iframe = driver.find_element_by_xpath("//iframe[contains(@title,'nrStr')]")
# 切入iframe
driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//body[starts-with(@class,'cke')]").send_keys('学生端功能正常')
# 跳出iframe
driver.switch_to.default_content()
# driver.find_element_by_id('fileupload').send_keys(r'/Users/xiaodaxing/Desktop/Race.pdf')  # Mac上传文件
# driver.find_element_by_id('fileupload').send_keys(r'D:\review.docx')  # modify
time.sleep(1)
driver.find_element_by_xpath('//input[@id="submitButton"]').click()
time.sleep(2)
try:
    print('弹框结果:' + driver.find_element_by_css_selector(
        "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
except NoSuchElementException as msg:
    print('截图', msg)
    driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'YJ' + ".png")  # modify截图
print('=====邮件测试完毕=====')
time.sleep(2)
##################################################退出网络学堂##########################################################
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
driver.quit()
print('关闭浏览器，删除cookie')
