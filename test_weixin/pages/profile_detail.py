from appium.webdriver.common.mobileby import MobileBy

from test_weixin.pages.base import Base
from test_weixin.pages.edit_member import EditMember


class ProfileDetail(Base):
    def to_edit_member(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/azk").click()
        return EditMember(self._driver)
