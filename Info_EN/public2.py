from selenium.webdriver.common.keys import Keys


class Login_Info():
    # 登录
    def user_login(self, driver, user, password):
        driver.find_element_by_id('user').send_keys(user)
        driver.find_element_by_id('pass').send_keys(password)
        # time.sleep(1)
        driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)

    # 退出
    def user_logout(self, driver):
        js_logout = "beforeLogout();"
        driver.execute_script(js_logout)
        # time.sleep(1)
        driver.find_element_by_xpath("//*[@class='btn btn-sub']").send_keys(Keys.ENTER)
        print('=====退出info=====')
        driver.delete_all_cookies()
        driver.quit()
