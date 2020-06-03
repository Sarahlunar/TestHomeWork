import json

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.uiframe_improve.pages.wrapper import handle_black


class Base:
    _params = {}
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

    def steps(self, path, fun_name):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)[fun_name]
        s = json.dumps(steps)
        for key, value in self._params.items():
            s = s.replace(f"${{{key}}}", value)
        steps = json.loads(s)
            # self.find(MobileBy.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
        element: WebElement
        elements: list
        for step in steps:
            if "find" in step.keys():
                element = self.find(step["find"], step["locator"])
            if "finds" in step.keys():
                elements = self.finds(step["finds"], step["locator"])
            if "action" in step.keys():
                if "click" == step["action"]:
                    element.click()
                if "send" == step["action"]:
                    element.send_keys(step["value"])
                if "len > 0" == step["action"]:
                    return len(elements) > 0