from appium.webdriver.common.mobileby import MobileBy

from app.uiframe.pages.base import Base


class Search(Base):
    def add_my_stock(self):
        self.find(MobileBy.ID, "search_input_text").send_keys("alibaba")
        self.find(MobileBy.XPATH, '//*[@text="BABA"]').click()
        el = self.find(MobileBy.XPATH, '//*[@text="阿里巴巴"]/../..//*[@text="加自选"]').click()

    def is_add(self):
        el = self.finds(MobileBy.XPATH, '//*[@text="阿里巴巴"]/../..//*[@text="已添加"]')
        if len(el) > 0:
            return True
        else:
            return False