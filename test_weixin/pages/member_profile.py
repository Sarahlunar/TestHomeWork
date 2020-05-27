from appium.webdriver.common.mobileby import MobileBy

from test_weixin.pages.base import Base
from test_weixin.pages.profile_detail import ProfileDetail


class MemberProfile(Base):
    def to_profile_detail(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/gvd").click()
        return ProfileDetail(self._driver)
