from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium_homework.page.add_member import AddMember


class Index:
    def __init__(self):
        options = Options
        options.debugger_address = "127.0.0.1:9222"
        self._driver = webdriver.Chrome(options=options)
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def goto_add_member(self):
        self._driver.find_element_by_id("menu_contacts").click()
        self._driver.find_elements_by_css_selector('.qui_btn ww_btn js_add_member').click()
        return AddMember(self._driver)