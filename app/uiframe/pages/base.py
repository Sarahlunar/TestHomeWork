from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.uiframe.pages.wrapper import handle_black


class Base:
    _max_num = 3
    _cur_num = 0
    _black_list = [
        (MobileBy.ID, "action_search"),
        (MobileBy.XPATH, '//*[@text="确定"]'),
        (MobileBy.XPATH, '//*[@text="是"]')
    ]
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, locator, content: str = None):
        el: WebElement
        if isinstance(locator, tuple):
            el = self._driver.find_element(*locator)
        else:
            el = self._driver.find_element(locator, content)
        return el

    @handle_black
    def finds(self, locator, content: str = None):
        el: WebElement
        if isinstance(locator, tuple):
            el = self._driver.find_elements(*locator)
        else:
            el = self._driver.find_elements(locator, content)
        return el


    def scroll_find(self, content):
       return self.find(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().'
       f'scrollable(true).instance(0)).'
       f'scrollIntoView(new UiSelector().'
       f'text("{content}").instance(0));')
        # self._driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()