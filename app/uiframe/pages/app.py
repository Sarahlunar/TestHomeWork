from appium import webdriver

from app.uiframe.pages.Index import Index
from app.uiframe.pages.base import Base


class App(Base):
    _package = "com.xueqiu.android"
    _activity = ".common.MainActivity"
    _device_name = "127.0.0.1:7555"
    def start(self):
        if self._driver == None:
            desire_caps = {}
            desire_caps["platformName"] = "android"
            desire_caps["platformVersion"] = "6.0"
            desire_caps["deviceName"] = self._device_name
            desire_caps["appPackage"] = self._package
            desire_caps["appActivity"] = self._activity
            desire_caps["noReset"] = "true"
            desire_caps["dontStopAppOnReset"] = "true"
            desire_caps["skipDeviceInitialization"] = "true"
            desire_caps["unicodeKeyBoard"] = "true"
            desire_caps["resetKeyBoard"] = "true"
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(3)
        return self

    def restart(self):
        self._driver.quit()
        return self

    def stop(self):
        return self

    def index(self) -> Index:
        return Index(self._driver)
