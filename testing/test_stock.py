# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStock:
    def setup_class(self):
        # 此处使用setup_class, 多个用例也只用初始化一次
        caps = {}
        caps["platformName"] = "android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".common.MainActivity"
        caps["noReset"] = "true"
        caps["dontStopAppOnReset"] = "true"
        caps["skipDeviceInitialization"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(4)

    def teardown(self):
        # 返回上一页保证下一次能够正确执行
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize('company, stockCode', yaml.safe_load(open("../datas/stockdatas/stock.yaml", "rb")))
    def test_case(self, company, stockCode):
        # 1. 找到输入框并点击
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        # 2.找到输入框并输入查询内容
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(f"{company}")
        # 3.找到要查询的内容并点击
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{stockCode}']").click()
        # 4.找到指定股票后面的"加自选"并点击
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{stockCode}']/../../..//*[@text='加自选']").click()
        # 5.断言加自选成功
        locator = (MobileBy.XPATH, f"//*[@text='{stockCode}']/../../..//*[@resource-id='com.xueqiu.android:id/followed_btn']")
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        res = self.driver.find_element(*locator).text
        assert res == "已添加"



