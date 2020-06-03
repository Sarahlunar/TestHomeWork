import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy

from app.uiframe_improve.pages.base import Base
from app.uiframe_improve.pages.search import Search


class Quotes(Base):
    def goto_search(self):
        self.steps("../datas/steps/quotes.yaml", "goto_search")
        return Search(self._driver)