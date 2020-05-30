from appium.webdriver.common.mobileby import MobileBy

from app.uiframe.pages.base import Base
from app.uiframe.pages.search import Search


class Quotes(Base):
    def goto_search(self):
        # self.find(MobileBy.ID, "action_search").click()
        return Search(self._driver)