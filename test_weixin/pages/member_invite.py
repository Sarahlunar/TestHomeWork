from appium.webdriver.common.mobileby import MobileBy

from test_weixin.pages.base import Base


class MemberInvite(Base):
    def mamul_add(self):
        from test_weixin.pages.contact_add import ContactAdd
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return ContactAdd(self._driver)

    def get_toast(self):
        return self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text