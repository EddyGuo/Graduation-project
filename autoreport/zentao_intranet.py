from selenium import webdriver
from xpath import XPath
import time


class InZenTao:
    """内部禅道模拟操作"""
    def __init__(self):
        """初始化函数"""
        self.driver = webdriver.Chrome()
        self.xpath = XPath()
        self.sleep_time = 0.5

    def click_by_xpath(self, xpath):
        """xpath点击"""
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(self.sleep_time)

    def click_by_id(self, _id):
        """id点击"""
        self.driver.find_element_by_id(_id).click()
        time.sleep(self.sleep_time)

    def click_by_text(self, text):
        """test点击"""
        self.driver.find_element_by_link_text(text).click()
        time.sleep(self.sleep_time)

    def bug_count(self):
        """bug计数"""
        count = self.driver.find_element_by_xpath(self.xpath.bug_count).get_attribute('innerHTML')
        return int(count)

    def login(self):
        """登录"""
        self.driver.get('http://192.168.0.90/zentaopms/www')
        self.driver.find_element_by_name('account').send_keys('cunnian.guo')
        self.driver.find_element_by_name('password').send_keys('nianKJ0409')
        self.driver.find_element_by_id('submit').click()

    def bug_search_case1(self, project, module_xpath=0):
        """Module=0, State, Priority"""
        bug_data = []

        self.login()
        self.click_by_xpath(self.xpath.menu_test)
        self.click_by_id('currentItem')
        self.click_by_text(project)
        self.click_by_xpath(self.xpath.search_tab)
        self.click_by_xpath(self.xpath.search_more_tab)

        if module_xpath:
            """选择模块"""
            self.click_by_xpath(self.xpath.search_field1)
            self.click_by_xpath(self.xpath.search_field1_option11)
            self.click_by_xpath(self.xpath.search_value1_chosen)
            self.click_by_xpath(module_xpath)

        # Total
        self.click_by_xpath(self.xpath.search_submit)
        bug_total = self.bug_count()

        self.click_by_xpath(self.xpath.search_field2)
        self.click_by_xpath(self.xpath.search_field2_option7)
        self.click_by_xpath(self.xpath.search_value2_chosen)
        self.click_by_xpath(self.xpath.search_value2_chosen3)
        self.click_by_xpath(self.xpath.search_submit)
        bug_closed = self.bug_count()

        # Not Closed
        bug_not_closed = bug_total - bug_closed

        # Activated
        self.click_by_xpath(self.xpath.search_value2_chosen)
        self.click_by_xpath(self.xpath.search_value2_chosen1)
        self.click_by_xpath(self.xpath.search_submit)
        bug_activated = self.bug_count()

        # P1(Activated)
        self.click_by_xpath(self.xpath.search_field3)
        self.click_by_xpath(self.xpath.search_field3_option13)
        self.click_by_xpath(self.xpath.search_value3_chosen)
        self.click_by_xpath(self.xpath.search_value3_chosen2)
        self.click_by_xpath(self.xpath.search_submit)
        bug_activated_p1 = self.bug_count()

        # P2(Activated)
        self.click_by_xpath(self.xpath.search_value3_chosen)
        self.click_by_xpath(self.xpath.search_value3_chosen3)
        self.click_by_xpath(self.xpath.search_submit)
        bug_activated_p2 = self.bug_count()

        bug_data.append(bug_closed)
        bug_data.append(bug_not_closed)
        bug_data.append(bug_activated)
        bug_data.append(bug_activated_p1)
        bug_data.append(bug_activated_p2)

        print(bug_data)
        return bug_data



