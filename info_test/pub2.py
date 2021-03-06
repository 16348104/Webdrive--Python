import time
import xlwt
import xlrd
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class LoginInfo():

    # 登录
    def user_login(self, driver, user, password):
        print('清除登录框')
        driver.find_element_by_id('user').send_keys('user')
        driver.find_element_by_id('pass').send_keys('password')
        time.sleep(2)
        icons = len(driver.find_elements_by_xpath("//*[contains(@class,'icon-t_close')]"))
        for i in range(0, icons):
            driver.find_elements_by_xpath("//*[contains(@class,'icon-t_close')]").pop(i).click()
        time.sleep(1)
        driver.find_element_by_id('user').send_keys(user)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
        time.sleep(3)

    # 退出
    def user_logout(self, driver):
        # driver.find_element_by_id('user').send_keys(user)
        # driver.find_element_by_id('pass').send_keys(password)
        # driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
        # time.sleep(5)
        js_logout = "beforeLogout();"
        driver.execute_script(js_logout)
        # time.sleep(1)
        driver.find_element_by_xpath("//*[@class='btn btn-sub']").send_keys(Keys.ENTER)
        print('=====退出info=====')
        driver.delete_all_cookies()
        driver.quit()

    # 切换到第二个窗口
    def switch_window(self, driver):
        windows = driver.window_handles  # 窗口总数
        window_1 = driver.current_window_handle  # 当前窗口句柄
        for current_window in windows:
            if current_window != window_1:
                driver.switch_to.window(current_window)
        print('所有句柄:', windows)
        print("当前窗口:", window_1)
        # print("窗口title:", driver.title)
        time.sleep(2)
        driver.close()
        # 切换回第一个窗口
        driver.switch_to.window(windows[0])
        window_2 = driver.current_window_handle
        print("当前窗口：", window_2)

    # 读取Excel文件
    def open_excel(file='E://test.xls'):
        try:
            # 打开Excel文件读取数据
            data = xlrd.open_workbook(file)
            return data
        except Exception as e:
            print(e, "文件不存在!")

    # 设置表格样式
    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        return style

    # 写入各个院系链接
    def write_excel(self, row0, col_module, col_dep, col_link):
        # 初始化样式
        style_head = xlwt.XFStyle()
        # 初始化字体相关
        font = xlwt.Font()
        font.name = "微软雅黑"
        font.bold = True
        font.colour_index = 1  # 必须是数字索引

        # # 初始背景图案
        # bg = xlwt.Pattern()
        # # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        # bg.pattern = xlwt.Pattern.SOLID_PATTERN
        # # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray
        # bg.pattern_fore_colour = 4
        # 设置字体
        style_head.font = font
        # 设置背景
        # style_head.pattern = bg
        f = xlwt.Workbook(encoding='utf-8')
        # f = xlwt.Workbook()
        sheet1 = f.add_sheet('各院系链接', cell_overwrite_ok=True)
        # 写第一行
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i])
            # 写模块
            for m in range(0, len(col_module)):
                sheet1.write(m + 1, 0, col_module[m])
                # 写院系
                for d in range(0, len(col_dep)):
                    sheet1.write(d + 1, 1, col_dep[d])
                    # 写链接
                    for k in range(0, len(col_link)):
                        sheet1.write(k + 1, 2, col_link[k])
        f.save('test.xls')
        # print("模块:", len(col_module), "个")
        print('院系:', len(col_link), '个')
        print("网站URL:", len(col_dep), "个")
