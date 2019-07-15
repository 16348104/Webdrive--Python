# coding=utf-8
import re
import os
import time
import random
import win32gui
import win32con
import win32api
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/chromedriver')  # MacOS


# driver = webdriver.Firefox()
driver = webdriver.Chrome()


# driver = webdriver.Firefox(
#     executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/geckodriver')  # mac firefox
# driver = webdriver.Chrome(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/wlxt/chromedriver')  # mac  chrome
# driver = webdriver.Safari() #Mac os
def time_format():
    current_time = time.strftime("%y-%m-%d %H-%M-%S", time.localtime(time.time()))
    return current_time


# class WinUpLoadFile:
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
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)


# if __name__ == "__main__":
#     Win32UpLoadFile().winUpLoadFile("D:\mov.mp4", "打开")
######################################################登录网络学堂######################################################
# 打开网络学堂
driver.get("http://wlxt160.thitc.cn")
# driver.get("http://learn.tsinghua.edu.cn")
driver.maximize_window()
print("======登录网络学堂=====")
print(driver.title)
print('测试浏览器:' + driver.name)
ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 计算明天时间
tomorrow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 3600))
print("当前时间戳为:", ticks)
# print ("当前时间戳为:", tomorrow)
driver.find_element_by_name("i_user").send_keys("")
driver.find_element_by_name("i_pass").send_keys("")
driver.find_element_by_id("loginButtonId").click()
print(driver.title, "【第1个窗口】")
time.sleep(1)
# driver.find_element_by_xpath("//a[contains(text(),'20740084-998')]").click()  # 正式20740084-998
driver.find_element_by_xpath("//a[contains(text(),'60240202-0')]").click()  # 开发环境60240202-0
# 【切换到第二个窗口】
window_1 = driver.current_window_handle  # 当前窗口句柄
print('课程句柄:' + window_1)
windows = driver.window_handles  # 窗口总数
for current_window in windows:
    if current_window != window_1:
        driver.switch_to.window(current_window)
time.sleep(3)
print(driver.title, "【第2个窗口】")
print('新窗口句柄:' + current_window)
print('=====登录成功=====')
time.sleep(2)
######################################################课程公告##########################################################
# print('=====测试课程公告=====')
# driver.find_element_by_xpath("//a[@id='wlxt_kcgg_wlkc_ggb']").click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="content"]//span[2]/a').click()
# print('=====发布公告=====')
# time.sleep(2)
# driver.find_element_by_name("bt").send_keys("测试公告" + ticks)
# driver.find_element_by_xpath("//div[@class='list title notext']//label[1]").click()  # 选标记重要公告
# driver.find_element_by_xpath("//div[@class='list order clearfix']//label[1]").click()  # 不推送邮件、微信
# time.sleep(1)
# print('上传公告附件')
# driver.find_element_by_xpath("//input[@id='fileupload']").send_keys(r"D:/Artists.mp3")  # modify
# time.sleep(1)
# driver.find_element_by_xpath('//a[@id="cke_37"]').click()
# js = "document.getElementsByClassName('cke_dialog_background_cover')[0].style.display = 'none'"
# driver.execute_script(js)
# time.sleep(2)
# driver.find_element_by_xpath('//*/table/tbody/tr[1]/td[1]/a/img').click()
# driver.find_element_by_id("saveBtn").click()# 发公告
# time.sleep(2)
# try:
#     driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
# except NoSuchElementException as msg:
#     print('截图', msg)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'gg' + ".png")  # 截图modify
# else:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(4)
# print('=====预览公告详情=====')
# driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]/a').click()
# driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
# time.sleep(1)
# print('=====公告测试完毕=====')
# time.sleep(4)

######################################################课程信息##########################################################
# print('=====测试课程信息=====')
# driver.find_element_by_xpath("//*[@id='wlxt_kc_v_kcxx_jskcxx']").click()
# driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
# time.sleep(2)
# driver.execute_script("document.documentElement.scrollTop = 0;")  # 滚动条
# time.sleep(1)
# print('=====漫游教务系统=====')
# driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/p[2]/a').click()
# try:
#     driver.switch_to.alert.accept()
# except Exception:  # 捕获到异常
#     print(Exception)
#     pass
# else:  # 未捕获到
#     print(UnexpectedAlertPresentException)
#     print(driver.switch_to.alert.text)
#     driver.switch_to.alert.accept()
# time.sleep(3)
# driver.back()
# print('=====上传课程图片=====')
# driver.find_element_by_id('doc').send_keys(r"D:/Photo.jpg")  # Modify
# # driver.find_element_by_id('doc').send_keys(r"/Users/xdx/Downloads/Map.png")  # Mac
# time.sleep(1)
# try:
#     driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
# except NoSuchElementException as msg:
#     print('截图', msg)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'kctp' + ".png")  # 截图modify
# else:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(3)
######################################################课程文件##########################################################
# print('=====测试课程文件=====')
# driver.find_element_by_xpath("//a[@id='wlxt_kj_wlkc_kjxxb']").click()
# time.sleep(2)
# print('=====发课件=====')
# driver.find_element_by_xpath('//span[@class="rt right"]/child::a').click()  # 上课件
# time.sleep(1)
# js = "document.getElementById('fileupload').style.display=\'block\'"
# driver.execute_script(js)
# driver.find_element_by_name("bt").send_keys("测试课件" + ticks)
# driver.find_element_by_xpath("//div[@class='list']//label[1]").click()  # 重要标记
# driver.find_element_by_name("fileupload").send_keys("D:/Lost Horizon.mp4")  # modify
# # driver.find_element_by_id('fileupload').send_keys(
# #     r'/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/readme.txt')  # mac上传文件
# driver.find_element_by_id("sub").click()
# time.sleep(5)
# try:
#     driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
# except NoSuchElementException as msg:
#     print('截图', msg)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'KJ' + ".png")  # 截图modify
# else:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(5)
# print('=====查看课件详情=====')
# # driver.find_element_by_xpath("//a[@id='wlxt_kj_wlkc_kjxxb']").click()
# # time.sleep(2)
# driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/a').click()
# driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
# print('=====下载课件=====')
# driver.back()
# time.sleep(1)
# driver.find_element_by_xpath("//tbody//tr[1]//td[8]//a[1]").click()
# print('=====预览课件=====')
# time.sleep(2)
# str1 = driver.find_element_by_xpath("//tbody//tr[1]//td[8]//a[2]").get_attribute('class')
# print(str1)
# searchObj = re.search(r'disabled', str1, re.I)  # 正则表达式
# if searchObj is None:
#     print('课件可以预览!')
#     time.sleep(2)
#     driver.find_element_by_xpath("//tbody//tr[1]//td[8]//a[2]").click()  # 点预览按钮
#     windows = driver.window_handles  # 显示所有句柄
#     window_1 = driver.current_window_handle
#     print('所有句柄:', windows)
#     print("当前窗口：", window_1)
#     # 切换窗口
#     driver.switch_to.window(windows[2])  # 切换到第3个窗口
#     time.sleep(1)
#     # sate = driver.find_element_by_css_selector(
#     #     "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").get_attribute('class')
#     # if sate == 'zeromodal-title1':
#     #     print(driver.find_element_by_css_selector(
#     #         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
#     #     driver.get_screenshot_as_file(
#     #         "C:/Users/zb/Downloads/FireShot/" + time_format() + 'ZHUANMA' + ".png")  # modify截图
#     # 课件异常情况
#     try:
#         driver.find_element_by_css_selector(
#             "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
#     except NoSuchElementException:
#         print('课件已经转码')
#     else:
#         print(driver.find_element_by_css_selector(
#             "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
#         driver.get_screenshot_as_file(
#             "C:/Users/zb/Downloads/FireShot/" + time_format() + 'ZHUANMA' + ".png")  # modify截图
#
#     try:  # Play Video
#         Video = driver.find_element_by_xpath("//button[@class='vjs-big-play-button']")
#     except NoSuchElementException as msg:
#         print('暂无视频文件', msg)
#     else:
#         Video.click()
#         print('预览视频文件')
#         time.sleep(5)
#     try:  # Play Audio
#         Audio = driver.find_element_by_css_selector("#mp3")
#     except NoSuchElementException as msg:
#         print('暂无音频文件', msg)
#     else:
#         js_audio = "var audio = document.getElementById('mp3');audio.play();"
#         driver.execute_script(js_audio)
#         print('预览音频文件')
#         time.sleep(5)
#     windows = driver.window_handles  # 窗口总数
#     # 切换到第2个窗口
#     driver.switch_to.window(windows[1])
#     print("当前窗口：", window_1)
# else:
#     print('文件不支持预览', searchObj)
# print('=====文件测试完毕=====')
# time.sleep(4)
######################################################课程作业##########################################################
# print('=====测试课程作业=====')
# driver.find_element_by_xpath("//a[@id='wlxt_kczy_zy']").click()
# time.sleep(3)
# 布置作业
# print('=====布置作业=====')
# driver.find_element_by_xpath('//*[@id="content"]//span[2]/a').click()
# driver.find_element_by_name("bt").send_keys("测试全体作业" + ticks)
# # 定位上传按钮，添加本地文件
# js = "document.getElementById('fileupload').style.display=\'block\'"
# driver.execute_script(js)
# driver.find_element_by_name("fileupload").send_keys("D:/listening.pdf")  # modify
# # 设置截止时间
# # driver.find_element_by_name("jzsj").send_keys(tomorrow)
# scroll = "document.documentElement.scrollTop = 10000;"
# driver.execute_script(scroll)
# time.sleep(1)
# driver.find_element_by_id('endtime').click()
# time.sleep(2)
# driver.find_element_by_xpath("//span[@class='laydate-btns-confirm']").click()
# time.sleep(1)
# driver.find_element_by_id("goBtn").click()  # 发布作业
# time.sleep(2)
# try:
#     driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
# except NoSuchElementException as msg:
#     print(msg, '截图')
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'ZY' + ".png")
# else:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(3)
# print('=====编辑作业=====')
# driver.find_element_by_xpath("//tr[2]//td[8]//a[3]").click()
# zy_geren = driver.find_element_by_xpath('//*[@id="r1"]').get_attribute('checked')  # 选作业完成方式:个人
# print('是否个人作业：', zy_geren)
# zy_zu = driver.find_element_by_xpath('//*[@id="r2"]').get_attribute('checked')  # 选作业完成方式:组
# print('是否组作业：', zy_zu)
# jf_fz = driver.find_element_by_xpath('//*[@id="r7"]').get_attribute('checked')  # 成绩计分方式:分值成绩
# print('是否分值:', jf_fz)
# jf_ffz = driver.find_element_by_xpath('//*[@id="r8"]').get_attribute('checked')  # 成绩计分方式:非分值成绩
# print('是否非分值:', jf_ffz)
# time.sleep(3)
# print('=====批阅作业=====')
# driver.find_element_by_xpath("//a[@id='wlxt_kczy_zy']").click()
# time.sleep(2)
# # 批阅作业列表beforePageList
# driver.find_element_by_xpath('//tr[2]//td[8]//a[1]').click()  # 去批阅作业
# driver.find_element_by_xpath("//*[@class='zhan']").click()  # 展开
# time.sleep(1)
# if zy_geren == 'true' and jf_fz == 'true':  # 个人分值作业
#     try:
#         driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[11]/a')  # 已交作业名单beforePiYue
#     except NoSuchElementException as msg:
#         print('表中数据为空,作业未提交', msg)
#     else:
#         driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[11]/a').click()  # 批阅作业
#         time.sleep(2)
#         try:
#             driver.find_element_by_xpath('//*[@id="attachment222"]/div[2]/a[2]')  # 学生作业附件
#         except NoSuchElementException as msg:
#             print('无上交作业附件', msg)
#         else:
#             driver.find_element_by_xpath('//*[@id="attachment222"]/div[2]/a[2]').click()  # 下载学生的作业附件
#         driver.find_element_by_xpath("//*[@id='cj']").clear()
#         gr_cj = random.randint(0, 100)
#         print('成绩:', gr_cj)
#         driver.find_element_by_xpath("//*[@id='cj']").send_keys(gr_cj)  # 打分
#         driver.find_element_by_xpath("//*[@id='documention']").clear()
#         driver.find_element_by_xpath("//*[@id='documention']").send_keys('个人作业已阅')  # 填评语
#         driver.find_element_by_id('fileupload').send_keys(
#             r'C:/Users/zb/Desktop/test/python/review.docx')  # modify      # 传评语附件
#         time.sleep(1)
#         driver.find_element_by_xpath("//div[@class='sub-back sub-back-3 absolute']//input[1]").click()
#         time.sleep(2)
#         try:
#             driver.find_element_by_css_selector(
#                 "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
#         except NoSuchElementException as msg:
#             print('批阅截图', msg)
#             driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'PZJ' + ".png")  # modify
#         else:
#             print('弹框结果:' + driver.find_element_by_css_selector(
#                 "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# elif zy_geren == 'true' and jf_ffz == 'true':  # 个人非分值作业
#     try:
#         driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[11]/a')  # 已交作业名单beforePiYue
#     except NoSuchElementException as msg:
#         print('表中数据为空,作业未提交', msg)
#     else:
#         driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[11]/a').click()  # 批阅作业
#         time.sleep(1)
#         try:
#             driver.find_element_by_xpath("//a[@class='ml-10']")  # 学生作业附件
#         except NoSuchElementException as msg:
#             print('无上交作业附件', msg)
#         else:
#             driver.find_element_by_xpath("//a[@class='ml-10']").click()  # 下载学生的作业附件
#         driver.find_element_by_xpath('//*[@id="select2-cj-container"]').click()  # 定位下拉菜单
#         time.sleep(1)
#         driver.find_element_by_xpath('//ul[@id="select2-cj-results"]')
#         time.sleep(1)
#         key = len(driver.find_elements_by_xpath("//li[@class='select2-results__option']"))
#         print("等级成绩个数", key)
#         li = random.randrange(1, key, 1)
#         print('成绩:', driver.find_elements_by_xpath("//li[@class='select2-results__option']").pop(li).text)
#         driver.find_elements_by_xpath("//li[@class='select2-results__option']").pop(li).click()  # 选成绩
#         driver.find_element_by_xpath("//*[@id='documention']").clear()
#         driver.find_element_by_xpath("//*[@id='documention']").send_keys('个人作业已阅')  # 填评语
#         time.sleep(1)
#         driver.find_element_by_id('fileupload').send_keys(
#             r'C:/Users/zb/Desktop/test/python/review.docx')  # modify      # 传评语附件
#         time.sleep(1)
#         driver.find_element_by_xpath("//*[@class='sub-back sub-back-3 absolute']//input[1]").click()
#         time.sleep(2)
#         try:
#             driver.find_element_by_css_selector(
#                 "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
#         except NoSuchElementException as msg:
#             print('批阅截图', msg)
#             driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'PZJ' + ".png")  # modify
#         else:
#             print('弹框结果:' + driver.find_element_by_css_selector(
#                 "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# elif zy_zu == 'true' and jf_fz == 'true':  # 分值组作业
#     try:
#         driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[8]/a')  # 已交作业名单beforePiYue
#     except NoSuchElementException as msg:
#         print('表中数据为空,作业未提交', msg)
#     else:
#         driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[8]/a').click()  # 批阅作业
#         time.sleep(1)
#         try:
#             driver.find_element_by_xpath('//*[@id="attachment2"]/div[2]/a[2]')  # 无学生作业附件
#         except NoSuchElementException as msg:
#             print('无上交作业附件', msg)
#         else:
#             driver.find_element_by_xpath('//*[@id="attachment2"]/div[2]/a[2]').click()  # 下载学生作业附件
#         driver.find_element_by_id('resetPL').click()  # 重置
#         zu_cj = random.randint(0, 100)
#         print('成绩：', zu_cj)
#         driver.find_element_by_id('inputPL').send_keys(zu_cj)  # 打分
#         driver.find_element_by_id('recommandPL').send_keys('组作业已阅')  # 填评语
#         driver.find_element_by_id('setPL').click()  # 设定成绩
#         driver.find_element_by_id('fileupload').send_keys(
#             r'C:/Users/zb/Desktop/test/python/review.docx')  # modify # 传评语附件
#         time.sleep(1)
#         driver.find_element_by_xpath("//div[@class='sub-back sub-back-3 absolute']//input[1]").click()
#         time.sleep(1)
#         try:
#             driver.find_element_by_css_selector(
#                 "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
#         except NoSuchElementException as msg:
#             print('截图', msg)
#             driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'PZY' + ".png")  # modify
#         else:
#             print('弹框结果:' + driver.find_element_by_css_selector(
#                 "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# elif zy_zu == 'true' and jf_ffz == 'true':  # 非分值组作业
#     try:
#         driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[8]/a')  # 已交作业名单beforePiYue
#     except NoSuchElementException as msg:
#         print('表中数据为空,作业未提交', msg)
#     else:
#         driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[8]/a').click()  # 批阅作业
#         time.sleep(1)
#         try:
#             driver.find_element_by_xpath('//*[@id="attachment2"]/div[2]/a[2]')  # 无学生作业附件
#         except NoSuchElementException as msg:
#             print('无上交作业附件', msg)
#         else:
#             driver.find_element_by_xpath('//*[@id="attachment2"]/div[2]/a[2]').click()  # 下载学生作业附件
#         driver.find_element_by_id('resetPL').click()  # 重置
#         time.sleep(1)
#         # sel = driver.find_element_by_id('//*[@id="selectPL"]')
#         # Select(sel).select_by_value('-98')
#         driver.find_element_by_xpath('//*[@id="select2-selectPL-container"]').click()
#         driver.find_element_by_xpath('//*[@id="select2-selectPL-results"]')
#         key = len(driver.find_elements_by_xpath("//li[@class='select2-results__option']"))  # 定位下拉菜单
#         print("等级成绩个数", key)
#         li = random.randrange(1, key, 1)
#         print('成绩:', driver.find_elements_by_xpath("//li[@class='select2-results__option']").pop(li).text)
#         driver.find_elements_by_xpath("//li[@class='select2-results__option']").pop(li).click()  # 选成绩
#         driver.find_element_by_id('recommandPL').send_keys('组作业已阅')  # 填评语
#         driver.find_element_by_id('setPL').click()  # 设定成绩
#         driver.find_element_by_id('fileupload').send_keys(
#             r'C:/Users/zb/Desktop/test/python/review.docx')  # modify # 传评语附件
#         time.sleep(1)
#         driver.find_element_by_xpath("//div[@class='sub-back absolute sub-back-3']//input[1]").click()
#         time.sleep(2)
#         try:
#             driver.find_element_by_css_selector(
#                 "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
#         except NoSuchElementException as msg:
#             print('截图', msg)
#             driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'PZY' + ".png")  # modify
#         else:
#             print('弹框结果:' + driver.find_element_by_css_selector(
#                 "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# print('=====作业测试完毕=====')
# time.sleep(4)
######################################################课程答疑###########################################################
# print('=====测试课程答疑=====')
# driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
# time.sleep(2)
# print('=====回答=====')
# driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]/a[1]').click()
# driver.execute_script("document.documentElement.scrollTop = 10000;")
# time.sleep(2)
# # Play Audio
# try:
#     driver.find_element_by_xpath('//audio')
# except NoSuchElementException as msg_MP3:
#     print('无音频文件', msg_MP3)
# else:
#     print('预览音频文件!')
#     js_audio = "var audio = document.getElementsByTagName('audio')[0];audio.play();"
#     driver.execute_script(js_audio)
#     time.sleep(5)
# # Play Video
# try:
#     driver.find_element_by_xpath("//video")
# except NoSuchElementException as msg_MP4:
#     print('无视频文件', msg_MP4)
# else:
#     print('预览视频文件!')
#     js_video = "var video = document.getElementsByTagName('video')[0];video.play();"
#     driver.execute_script(js_video)
#     time.sleep(5)
# # 随机下载答疑附件
# print('=====下载答疑文件=====')
# try:
#     driver.find_element_by_xpath('//*[@id="removeFile"]')
# except NoSuchElementException as msg:
#     print('无答疑附件', msg)
# else:
#     key = len(driver.find_elements_by_xpath('//*[@id="removeFile"]'))
#     print("答疑附件个数", key)
#     ran = random.randrange(key)
#     print('随机数', ran)
#     driver.find_elements_by_xpath('//*[@id="removeFile"]').pop(ran).click()
# time.sleep(3)
# # 富文本音频win32gui
# driver.find_element_by_xpath("//a[@id='cke_41']").click()
# time.sleep(1)
# try:
#     winUpLoadFile("D:\Artists.mp3", "打开")
#     print('CKeditor传音频文件')
# except UnexpectedAlertPresentException as msg_alert:
#     print('截图', msg_alert)  # 上传文件失败
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'ckeditor' + ".png")  # modify截图
#     driver.switch_to.alert.accept()
# time.sleep(5)
# # dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
# # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
# # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
# # Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
# # button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
# # win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, "D:\Artists.mp3")  # 往输入框输入绝对地址D:\
# # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
# # win32gui.PostMessage(dialog, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
# # win32gui.PostMessage(dialog, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
# # 富文本视频win32gui
# driver.find_element_by_xpath('//*[@id="cke_41"]').click()
# time.sleep(1)
# try:
#     winUpLoadFile("D:\mov.mp4", "打开")  # 往输入框输入绝对地址D:\modify
#     print('CKeditor传视频文件')
# except UnexpectedAlertPresentException as msg_alert:
#     print('截图', msg_alert)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'ckeditor' + ".png")  # modify截图
#     driver.switch_to.alert.accept()
# time.sleep(10)
# driver.find_element_by_xpath('//*[@id="saveBtn"]').click()
# time.sleep(2)
# try:
#     driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
# except NoSuchElementException as msg:
#     print('截图', msg)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'HD' + ".png")  # modify截图
# else:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(5)
#
# print('=====编辑已回答问题=====')
# # driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
# # time.sleep(2)
# # 切换标签
# driver.find_element_by_xpath('//*[@id="tabbox"]/ul/li[2]').click()
# time.sleep(1)
# # 点编辑按钮
# driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]/a[1]').click()
# time.sleep(1)
# driver.execute_script("document.documentElement.scrollTop = 10000;")
# # CKeditor数学公式
# driver.find_element_by_xpath("//a[@id='cke_39']").click()
# time.sleep(2)
# js = "document.getElementsByClassName('cke_dialog_background_cover')[0].style.display = 'none'"
# driver.execute_script(js)
# time.sleep(1)
# driver.find_element_by_xpath("//a[contains(@class,'ok')]").click()  # 动态id
# print("CKeditor录入数学公式")
# time.sleep(2)
# # 富文本图片win32gui
# driver.find_element_by_xpath('//*[@id="cke_40"]').click()
# time.sleep(1)
# try:
#     winUpLoadFile('D:\Test.jpg', "打开")  # 往输入框输入绝对地址D:\   modify
#     print('Ckeditor传图片')
# except UnexpectedAlertPresentException as msg_ckeditor:
#     print('截图', msg_ckeditor)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'ckeditor' + ".png")  # modify截图
#     driver.switch_to.alert.accept()
# time.sleep(3)
# # 上传附件
# driver.find_element_by_xpath('//*[@id="fileupload"]').send_keys(r'D:\Homework.pdf')  # modify
# driver.find_element_by_xpath('//*[@id="saveBtn"]').click()
# time.sleep(2)
# try:
#     driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
# except NoSuchElementException as msg:
#     print('截图', msg)
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + time_format() + 'BJWT' + ".png")  # modify截图
# else:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(5)
# print('=====加入问题集锦=====')
# driver.find_element_by_xpath('//*[@id="tabbox"]/ul/li[2]').click()
# time.sleep(1)
# try:
#     driver.find_element_by_xpath('//*[@id="addWtjjBtn"]')
# except NoSuchElementException as msg:
#     print('已经加入问题集锦了！', msg)
# else:
#     driver.find_element_by_xpath('//*[@id="addWtjjBtn"]').click()
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(2)
# print('=====查看问题集锦=====')
# driver.find_element_by_xpath('//*[@id="wlxt_bbs_bbs_kcdy"]').click()
# time.sleep(2)
# # 切换标签
# driver.find_element_by_xpath('//*[@id="tabbox"]/ul/li[3]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//tr[1]//td[2]/a').click()
# time.sleep(2)
# driver.execute_script("document.documentElement.scrollTop = 10000;")
# # Play Audio
# try:
#     driver.find_element_by_xpath("//p[@id='wtnr']//p//audio")
# except NoSuchElementException as msg_MP3:
#     print('无音频文件', msg_MP3)
# else:
#     print('预览音频文件')
#     js_audio = "var audio = document.getElementsByTagName('audio')[0];audio.play();"
#     driver.execute_script(js_audio)
#     time.sleep(5)
# # Play Video
# try:
#     driver.find_element_by_xpath("//p[@id='wtnr']//p//video")
# except NoSuchElementException as msg_MP4:
#     print('无视频文件', msg_MP4)
# else:
#     print('预览视频文件')
#     js_video = "var video = document.getElementsByTagName('video')[0];video.play();"
#     driver.execute_script(js_video)
#     time.sleep(5)
# # 随机下载答疑附件
# print('随机下载问题集锦文件')
# try:
#     driver.find_element_by_xpath("//*[@class='download-file']//*[@id='removeFile']")
# except NoSuchElementException as msg:
#     print('无答疑附件', msg)
# else:
#     key = len(driver.find_elements_by_xpath("//*[@class='download-file']//*[@id='removeFile']"))
#     print("答疑附件个数", key)
#     ran = random.randrange(key)
#     print('随机数', ran)
#     driver.find_elements_by_xpath("//*[@class='download-file']//*[@id='removeFile']").pop(ran).click()
# time.sleep(1)
# print('=====课程答疑测试完毕=====')
# time.sleep(3)

######################################################课程邮件##########################################################
# print('=====测试课程邮件=====')
# driver.find_element_by_xpath("//a[@id='wlxt_mail_yj_yjxxb']").click()
# time.sleep(2)
# print('=====发邮件=====')
# driver.find_element_by_xpath('//span[@class="rt right"]/child::a').click()
# # driver.find_element_by_class_name("ui-autocomplete-input").send_keys(
# #    "xiesp@tsinghua.edu.cn,chc@tsinghua.edu.cn,wlxt@tsinghua.edu.cn,dj1005@tsinghua.edu.cn,zhongwenfeng@tsinghua.edu.cn")
# driver.find_element_by_xpath('//*[@id="myTags"]/li/input').send_keys('wlxt@tsinghua.edu.cn')
# time.sleep(1)
# driver.find_element_by_id("bt").send_keys(ticks + "网络学堂自动测试:教师端系统正常")
# driver.find_element_by_id("submitButton").click()
# time.sleep(2)
# print('弹框结果:' + driver.find_element_by_css_selector(
#     "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# time.sleep(4)
# print("=====浏览邮件=====")
# driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]/a').click()  # 浏览邮件
# driver.find_element_by_xpath('//*[@id="returnButton"]').click()
# time.sleep(2)
# print('=====邮件测试完毕=====')
##################################################退出网络学堂##########################################################
driver.find_element_by_xpath("//i[@class='webicon-out']").click()
time.sleep(1)
driver.find_element_by_xpath("//div[contains(@class,'zeromodal-footer')]//button[contains(text(),'确定')]").send_keys(
    Keys.ENTER)
print('=====退出网络学堂=====')
driver.delete_all_cookies()
time.sleep(1)
print('关闭浏览器，删除cookie')
driver.quit()
