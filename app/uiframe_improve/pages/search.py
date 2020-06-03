from appium.webdriver.common.mobileby import MobileBy

from app.uiframe_improve.pages.base import Base


class Search(Base):
    def search(self, stock_name, stock_code):
        self._params["stock_name"] = stock_name
        self._params["stock_code"] = stock_code
        self.steps("../datas/steps/search.yaml", "search")
        return self

    def add_my_stock(self,stock_code):
        self._params["stock_code"] = stock_code
        self.steps("../datas/steps/search.yaml", "add_my_stock")

    def is_add(self, stock_code):
        self._params["stock_code"] = stock_code
        return self.steps("../datas/steps/search.yaml", "is_add")


    def reset(self, stock_code):
        self._params["stock_code"] = stock_code
        self.steps("../datas/steps/search.yaml", "reset")
        return self
