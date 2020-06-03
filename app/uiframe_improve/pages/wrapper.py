import logging

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy


def handle_black(func):
    logging.basicConfig(level=logging.INFO)
    def handled(*args, **kwargs):
        from app.uiframe.pages.base import Base
        instance: Base = args[0]
        element: WebElement
        try:
            logging.info(f"run:{func.__name__}\n args:{args[1:]}\n kwargs: {kwargs}")
            element = func(*args, **kwargs)
            # 如果找到了元素, _cur_num=0
            instance._cur_num = 0
            # 找到了隐式等待恢复3秒
            instance._driver.implicitly_wait(3)
            return element
        except Exception as e:
            # 找不到设置隐式等待1秒

            instance._driver.implicitly_wait(1)
            if instance._cur_num >= instance._max_num:
                raise e
            instance._cur_num += 1
            logging.error("元素未找到, 处理黑名单")
            for loc in instance._black_list:
                els = instance._driver.find_elements(*loc)
                if len(els) > 0:
                    els[0].click()
                    break
            return handled(*args, **kwargs)
    return handled