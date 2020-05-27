from appium.webdriver.common.mobileby import MobileBy

from test_weixin.pages.base import Base
from test_weixin.pages.member_invite import MemberInvite
from test_weixin.pages.member_profile import MemberProfile


class AddressList(Base):
    def add_member(self):

        self.scroll_find("添加成员").click()
        # self._driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        return MemberInvite(self._driver)

    def to_member_profile(self, username="yang"):
        self.scroll_find(username).click()
        return MemberProfile(self._driver)
