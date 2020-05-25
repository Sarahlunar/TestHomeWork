from appium.webdriver.webdriver import WebDriver


class Base:
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, content=None):
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, content)
