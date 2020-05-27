from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeixin:
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["platformVersion"] = "6.0"
        desire_caps["deviceName"] = "127.0.0.1:7555"
        desire_caps["appPackage"] = "com.xueqiu.android"
        desire_caps["appActivity"] = ".common.MainActivity"
        desire_caps["noReset"] = "true"
        desire_caps["dontStopAppOnReset"] = "true"
        desire_caps["skipDeviceInitialization"] = "true"
        desire_caps["unicodeKeyBoard"] = "true"
        desire_caps["resetKeyBoard"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()

    def test_add_contact(self):
        print("添加联系人")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys("霍格1")
        self.driver.find_element(MobileBy.XPATH, ).send_keys("霍格1")

