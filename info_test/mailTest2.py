from selenium import webdriver
from public2 import Login


class LoginTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(10)
        self.driver.get('http://infoen.syx.thcic.cn')

    # admin 用户登录
    def test_admin_login(self):
        username = '2011990118'
        password = 'a123456'
        Login().user_login(self.driver, username, password)
        self.driver.quit()

    # guest 用户登录
    def test_guest_login(self):
        username = 'guest'
        password = '321'
        Login().user_login(self.driver, username, password)
        self.driver.quit()


# 执行测试
LoginTest().test_admin_login()
LoginTest().test_guest_login()
