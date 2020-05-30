from appium.webdriver.common.mobileby import MobileBy

from app.uiframe.pages.base import Base
from app.uiframe.pages.quotes import Quotes


class Index(Base):
    def goto_quotes(self):
        self.find(MobileBy.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
        return Quotes(self._driver)