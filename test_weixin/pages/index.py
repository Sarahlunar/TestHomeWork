from appium.webdriver.common.mobileby import MobileBy

from test_weixin.pages.address_list import AddressList
from test_weixin.pages.base import Base


class Index(Base):
    def goto_mesage(self):
        pass

    def goto_addresslist(self):
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return  AddressList(self._driver)

    def goto_workbench(self):
        pass

    def goto_prifile(self):
        pass