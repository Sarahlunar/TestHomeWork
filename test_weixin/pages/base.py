from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class Base:
    _max_num = 3
    _cur_num = 0
    _except_list = [
        (MobileBy.XPATH, '//*[@text="确定"]'),
        (MobileBy.XPATH, '//*[@text="是"]')
    ]
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, content: str = None):
        el: WebElement
        try:
            el = self._driver.find_element(*locator) if isinstance(locator, tuple) else\
                self._driver.find_element(locator, content)
            # 如果找到了元素, _cur_num=0
            self._cur_num = 0
            # 找到了隐式等待恢复3秒
            self._driver.implicitly_wait(3)
            return el
        except Exception as e:
            # 找不到设置隐式等待1秒
            self._driver.implicitly_wait(1)
            if self._cur_num >= self._max_num:
                raise  e
            self._cur_num += 1
            for loc in self._except_list:
               els = self._driver.find_elements(*loc)
               if len(els) > 0:
                    els[0].click()
                    break
            return self.find(locator, content)



    def scroll_find(self, content):
       return self.find(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().'
       f'scrollable(true).instance(0)).'
       f'scrollIntoView(new UiSelector().'
       f'text("{content}").instance(0));')
        # self._driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()