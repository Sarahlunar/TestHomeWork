from appium.webdriver.common.mobileby import MobileBy

from test_weixin.pages.base import Base


class ContactAdd(Base):
    def input_name(self):
        user = self._driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]')
        user.send_keys("霍格03")
        return self

    def set_gender(self):
        self.find(MobileBy.XPATH, '//*[@text="性别"]/..//*[contains(@class, "ImageView")]').click()
        self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    def input_phonenum(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/eqx').send_keys("13900000003")
        return self

    def click_save(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/gvk').click()

        from test_weixin.pages.member_invite import MemberInvite
        return  MemberInvite(self._driver)