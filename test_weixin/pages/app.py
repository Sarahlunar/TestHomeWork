from appium import webdriver

from test_weixin.pages.base import Base
from test_weixin.pages.index import Index


class App(Base):
    def start(self):
        if self._driver == None:
            desire_caps = {}
            desire_caps["platformName"] = "android"
            desire_caps["platformVersion"] = "6.0"
            desire_caps["deviceName"] = "127.0.0.1:7555"
            desire_caps["appPackage"] = "com.tencent.wework"
            desire_caps["appActivity"] = ".launch.WwMainActivity"
            desire_caps["noReset"] = "true"
            desire_caps["dontStopAppOnReset"] = "true"
            desire_caps["skipDeviceInitialization"] = "true"
            desire_caps["unicodeKeyBoard"] = "true"
            desire_caps["resetKeyBoard"] = "true"
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(3)
        return self

    def restart(self):
        self._driver.quit()
        return self

    def stop(self):
        return self

    def index(self) -> Index:
        return Index(self._driver)
