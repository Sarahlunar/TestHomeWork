from selenium.webdriver.remote.webdriver import WebDriver


class AddMember:
    def __init__(self, driver: WebDriver):
        self._driver = driver
    def add_member(self):
        self._driver.find_element_by_id("username").send_keys("awuyou")
        self._driver.find_element_by_id("memberAdd_acctid").send_keys("awuyou")
        self._driver.find_element_by_id("memberAdd_phone").send_keys("13300000001")
        self._driver.find_element_by_xpath('//*[@id="js_contacts313"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()

    def get_member(self):
        members = self._driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
        return [m.get_attribute('title') for m in members]

