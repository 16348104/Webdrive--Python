import time
import xlwt
from selenium import webdriver
from public2 import LoginInfo
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# 教师端
class LoginTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        # driver = webdriver.Safari() #Mac os
        # self.driver.get('http://infoen.syx.thcic.cn')
        # driver.get('http://101.6.28.150:29009')
        self.driver.get('http://eng.info.tsinghua.edu.cn')
        print("======进入info教师端=====")
        self.driver.maximize_window()
        time.sleep(3)
        # driver.set_window_size(1080*760)
        # self.driver.implicitly_wait(10)

    # 教师登录
    def test_admin_login(self):
        user = '2011990118'
        password = 'a123456'
        LoginInfo().user_login(self.driver, user, password)
        time.sleep(2)

    # 退出系统
    def test_logout(self):
        user = '2017013478'
        password = 'a123456'
        LoginInfo().user_login(self.driver, user, password)
        time.sleep(5)
        # LoginInfo().user_login(self.driver)

    # 测试enginfo
    def test_enginfo(self):
        print('测试浏览器:' + self.driver.name)
        self.driver.get('http://101.6.28.150:29009')
        # driver.set_window_size(1080*760)
        print("======Forgot your password======")
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/a').click()
        time.sleep(1)
        # # 切换【第二个窗口】
        LoginInfo.switch_window(self, self.driver)
        print("======切换中文info======")
        self.driver.find_element_by_xpath("//a[@class='backCh']").click()
        time.sleep(1)
        self.driver.back()
        print("======登录English_info======")
        username = '1992990279'
        password = '123'
        LoginInfo().user_login(self.driver, username, password)
        time.sleep(2)
        print(self.driver.find_element_by_xpath('//li[@class="name"]').text)
        print(self.driver.find_element_by_xpath('//li[@class="stuId"]').text)
        print("======Edit Personal Details======")
        self.driver.find_element_by_xpath("//*[@class='btn']").click()
        # # 切换到新窗口
        LoginInfo.switch_window(self, self.driver)
        print("======Tsinghua University Information Portal======")
        mk = len(self.driver.find_elements_by_xpath("//ul[@id='tas']/a"))
        i = 0
        while i < mk:
            self.driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).click()
            time.sleep(1)
            str1 = self.driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).text
            print(str1, "模块")
            i = i + 1
            # driver.find_element_by_xpath('//*[@id="1"]').click()
            hrefs = len(self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a'))
            j = 0
            while j < hrefs:
                str2 = self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).text
                self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).click()
                time.sleep(2)
                # # 切换【第二个窗口】
                windows = self.driver.window_handles
                print("所有窗口:", windows)
                # # 切换到新窗口
                self.driver.switch_to.window(windows[1])
                print("当前窗口标题:", self.driver.title, self.driver.current_window_handle)
                time.sleep(2)
                date = self.driver.current_url
                self.driver.close()
                # 切换到第1个窗口
                self.driver.switch_to.window(windows[0])
                print("当前窗口：", self.driver.current_window_handle)
                # date = driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_property('href')
                # date = self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_attribute('href')
                # time.sleep(1)
                print(str2, ":", date)
                j = j + 1
        self.driver.find_element_by_xpath("//*[@class='btn btn-default dropdown-toggle']").click()
        print("======Change Password======")
        # 鼠标滑动Change Password
        above = self.driver.find_element_by_xpath("//ul[@class='dropdown-menu']/li[1]/a")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(above).perform()
        above.click()
        time.sleep(2)
        # # 切换到新窗口
        LoginInfo.switch_window(self, self.driver)
        LoginInfo.user_logout(self, self.driver)


# 执行测试
# LoginTest().test_admin_login()
# LoginTest().test_bachelor_login()
# LoginTest().test_logout()
LoginTest().test_enginfo()
