from appium.webdriver.common.mobileby import MobileBy

from test_weixin.pages.base import Base


class ContactAdd(Base):
    def input_name(self, username="霍格01"):
        user = self._driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]')
        user.send_keys(f"{username}")
        return self

    def set_gender(self, gender="男"):
        self.find(MobileBy.XPATH, '//*[@text="性别"]/..//*[contains(@class, "ImageView")]').click()
        self.find(MobileBy.XPATH, f'//*[@text="{gender}"]').click()
        return self

    def input_phone_num(self, mobile="13900000002"):
        self.find(MobileBy.ID, 'com.tencent.wework:id/eqx').send_keys(f"{mobile}")
        return self

    def click_save(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/gvk').click()

        from test_weixin.pages.member_invite import MemberInvite
        return  MemberInvite(self._driver)