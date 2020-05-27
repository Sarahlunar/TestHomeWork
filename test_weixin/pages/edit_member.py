from appium.webdriver.common.mobileby import MobileBy

from test_weixin.pages.base import Base


class EditMember(Base):
    def delete_member(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/dve").click()
        self.find(MobileBy.XPATH, '//*[@text="确定"]').click()
        # 需要回到消息页, 才能继续进行删除操作, 有待优化
        self.find(MobileBy.XPATH, '//*[@text="消息"]').click()
