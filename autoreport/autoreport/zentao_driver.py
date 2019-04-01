#!/usr/bin/python
# -*- coding: UTF-8 -*-


from selenium import webdriver
import time
from autoreport.settings import Settings
from autoreport.data2file import Data2file


class XPath:
    def __init__(self):
        """
        XPath. It is recommended to use variables instead of XPath.
        """
        self.menu_test = '//*[@id="mainmenu"]/ul/li[4]/a'                                 # 主页/测试
        self.module_Launcher = '//*[@id="module1112"]'                                    # Launcher模块
        self.bug_count = '//*[@id="bugList"]/tfoot/tr/td/div[2]/div/strong[1]'            # bug计数
        self.search_tab = '//*[@id="bysearchTab"]/a'                                      # 搜索
        self.search_more_tab = '//*[@id="searchmore"]/i'                                  # 更多搜索
        self.search_field1 = '//*[@id="field1"]'                                          # 搜索范围1
        self.search_field1_option11 = '//*[@id="field1"]/option[11]'                      # 搜索范围1/选项11（所属模块）
        self.search_value1_chosen = '//*[@id="value1_chosen"]/a/div/b'                    # 搜索范围1/选项11/选择值
        self.search_value1_chosen2 = '//*[@id="value1_chosen"]/div/ul/li[2]'              # 搜索范围1/选项11/选择值2(Launcher)
        self.search_field2 = '//*[@id="field2"]'                                          # 搜索范围2
        self.search_field2_option7 = '//*[@id="field2"]/option[7]'                        # 搜索范围2/选项7（Bug状态）
        self.search_value2_chosen = '//*[@id="value2_chosen"]/a/div/b'                    # 搜索范围2/选项7/选择值
        self.search_value2_chosen3 = '//*[@id="value2_chosen"]/div/ul/li[3]'              # 搜索范围2/选项7/选择值3(已关闭)
        self.search_value2_chosen1 = '//*[@id="value2_chosen"]/div/ul/li[1]'              # 搜索范围2/选项7/选择值3(激活)
        self.search_field3 = '//*[@id="field3"]'                                          # 搜索范围3
        self.search_field3_option13 = '//*[@id="field3"]/option[13]'                      # 搜索范围3/选项13（严重程度）
        self.search_value3_chosen = '//*[@id="value3_chosen"]/a/div/b'                    # 搜索范围3/选项13/选择值
        self.search_value3_chosen2 = '//*[@id="value3_chosen"]/div/ul/li[2]'              # 搜索范围3/选项13/选择值2(1)
        self.search_value3_chosen3 = '//*[@id="value3_chosen"]/div/ul/li[3]'              # 搜索范围3/选项13/选择值3(2)
        self.search_submit = '//*[@id="submit"]'


class ZenTao:
    def __init__(self, settings):
        """
        Grab data on ZenTao.
        :param settings: Settings.
        """
        self.settings = settings
        self.driver = webdriver.Chrome()
        self.xpath = XPath()
        self.sleep_time = self.settings.sleep_time

    def click_by_xpath(self, xpath):
        """
        Click through XPath.
        :param xpath: XPath.
        :return:
        """
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(self.sleep_time)

    def click_by_id(self, _id):
        """
        Click through ID.
        :param _id: ID.
        :return:
        """
        self.driver.find_element_by_id(_id).click()
        time.sleep(self.sleep_time)

    def click_by_text(self, text):
        """
        Click through text.
        :param text: text.
        :return:
        """
        self.driver.find_element_by_link_text(text).click()
        time.sleep(self.sleep_time)

    def bug_count(self):
        """
        Bug count.
        :return: The number of bugs.
        """
        try:
            count = self.driver.find_element_by_xpath(self.xpath.bug_count).get_attribute('innerHTML')
            count = int(count)
        except Exception as e:
            print('Error:', e)
            count = 0
        return count

    def read_table(self):
        """
        Grab table data with bugList ID.
        :return: Table data. 2d list.
        """
        table_data = []
        table = self.driver.find_element_by_id('bugList')
        table_rows = table.find_elements_by_class_name('text-center')
        for row in table_rows:
            cols = row.find_elements_by_tag_name('td')
            data_rows = []
            for col in cols:
                data = col.text
                data_rows.append(data)
            table_data.append(data_rows)
        return table_data

    def login(self, addr, account, password):
        """
        Login ZenTao.
        :param addr: ZenTao address.
        :param account: ZenTao account.
        :param password: ZenTao password.
        :return:
        """
        self.driver.get(addr)
        self.driver.find_element_by_name('account').send_keys(account)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('submit').click()

    def bug_search_case1(self, project, module_xpath=''):
        """
        获取内部禅道的Bug数据
        :param project: Project.
        :param module_xpath: Module.
        :return: 
        """""
        bug_data = []

        self.login(self.settings.in_address, self.settings.in_account, self.settings.in_password)
        self.click_by_xpath(self.xpath.menu_test)
        self.click_by_id('currentItem')
        self.click_by_text(project)
        self.click_by_xpath(self.xpath.search_tab)
        self.click_by_xpath(self.xpath.search_more_tab)

        if module_xpath:
            # 选择模块
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

    def bug_search_case2(self, project, module_xpath=''):
        """
        获取一级Bug信息
        :param project:
        :param module_xpath:
        :return:
        """
        self.login(self.settings.in_address, self.settings.in_account, self.settings.in_password)
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

        self.click_by_xpath(self.xpath.search_field2)
        self.click_by_xpath(self.xpath.search_field2_option7)
        self.click_by_xpath(self.xpath.search_value2_chosen)
        self.click_by_xpath(self.xpath.search_value2_chosen1)
        self.click_by_xpath(self.xpath.search_field3)
        self.click_by_xpath(self.xpath.search_field3_option13)
        self.click_by_xpath(self.xpath.search_value3_chosen)
        self.click_by_xpath(self.xpath.search_value3_chosen2)
        self.click_by_xpath(self.xpath.search_submit)

        bug_count = self.bug_count()

        reorder_data = []
        if bug_count > 0:
            bug_data = self.read_table()
            for i in bug_data:
                j = i[0:5] + [i[-4]]
                reorder_data.append(j)
        return bug_count, reorder_data

    def bug_search_case3(self, project):
        """
        获取外部禅道的Bug数据
        :param project:
        :return:
        """
        bug_data = []
        self.login(self.settings.ex_address, self.settings.ex_account, self.settings.ex_password)
        self.click_by_xpath(self.xpath.menu_test)
        self.click_by_id('currentItem')
        self.click_by_text(project)
        self.click_by_xpath(self.xpath.search_tab)
        self.click_by_xpath(self.xpath.search_more_tab)

        # Total
        self.click_by_xpath(self.xpath.search_submit)
        self.click_by_xpath(self.xpath.search_tab)
        bug_total = self.bug_count()

        self.click_by_xpath(self.xpath.search_field2)
        self.click_by_xpath(self.xpath.search_field2_option7)
        self.click_by_xpath(self.xpath.search_value2_chosen)
        self.click_by_xpath(self.xpath.search_value2_chosen3)
        self.click_by_xpath(self.xpath.search_submit)
        self.click_by_xpath(self.xpath.search_tab)
        bug_closed = self.bug_count()

        # Not Closed
        bug_not_closed = bug_total - bug_closed

        # Activated
        self.click_by_xpath(self.xpath.search_value2_chosen)
        self.click_by_xpath(self.xpath.search_value2_chosen1)
        self.click_by_xpath(self.xpath.search_submit)
        self.click_by_xpath(self.xpath.search_tab)
        bug_activated = self.bug_count()

        # P1(Activated)
        self.click_by_xpath(self.xpath.search_field3)
        self.click_by_xpath(self.xpath.search_field3_option13)
        self.click_by_xpath(self.xpath.search_value3_chosen)
        self.click_by_xpath(self.xpath.search_value3_chosen2)
        self.click_by_xpath(self.xpath.search_submit)
        self.click_by_xpath(self.xpath.search_tab)
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


if __name__ == '__main__':
    ts_settings = Settings()
    inZT_driver1 = ZenTao(ts_settings)
    _bug_count, data1 = inZT_driver1.bug_search_case2('P系列/P1pro', inZT_driver1.xpath.search_value1_chosen2)
    inZT_driver1.driver.close()
    P1Prp_P1_col = ['Bug编号', '优先级', '严重程度', '标题', 'Bug状态', '指派给']
    data1.insert(0, P1Prp_P1_col)
    print(data1)
    data2file = Data2file(ts_settings)
    data2file.bug_list2xls(data1, 'buglist.xls')
