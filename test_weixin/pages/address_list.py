from appium.webdriver.common.mobileby import MobileBy

from test_weixin.pages.base import Base
from test_weixin.pages.member_invite import MemberInvite


class AddressList(Base):
    def add_member(self):
        self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                                'scrollable(true).instance(0)).'
                                                                'scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        # self._driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        return MemberInvite(self._driver)