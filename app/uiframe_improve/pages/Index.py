import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy

from app.uiframe_improve.pages.base import Base
from app.uiframe_improve.pages.quotes import Quotes


class Index(Base):

    def goto_quotes(self):
        self.steps("../datas/steps/index.yaml", "goto_quotes")
        return Quotes(self._driver)
