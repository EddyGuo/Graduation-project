class XPath:
    def __init__(self):
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
        self.search_submit = '//*[@id="submit"]'                                          # 提交搜索
