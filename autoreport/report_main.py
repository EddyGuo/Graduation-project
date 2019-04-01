#!/usr/bin/python
# -*- coding: UTF-8 -*-

from autoreport.zentao_driver import ZenTao
from autoreport.data2file import Data2file
from autoreport.send_email import SendEmail
from autoreport.settings import Settings
import os


def bug_count_report1(settings, sender, data2file):
    driver = ZenTao(settings)
    sheet_index = 0
    img_name = 'P1Pro'                 # 生成的图片名称.png
    img_tag = 'P1Pro'                  # 图片标签，不得包含中文和其他非法字符
    title = 'P1Pro Launcher C端BUG概况曲线图： '
    project = 'P系列/P1pro'
    num_table_data = settings.num_table_data   # 表格数据行数
    num_img_data = settings.num_img_data      # 折线图数据个数

    data = driver.bug_search_case1(project, driver.xpath.search_value1_chosen2)   # 抓取数据
    driver.driver.close()
    data2file.data2xls(data, sheet_index)    # 生成excel
    data2file.data2img(img_name, num_img_data, sheet_index)   # 生成折线图
    data2table = data2file.read_xls(sheet_index)              # 获取excel数据
    sender.text2html(title, weight=True)                      # 添加标题
    if num_table_data > len(data2table)-1:                    # 判断数据量是否超过最大显示数量
        num_table_data = len(data2table) - 1
    sender.table2html([data2table[0]] + data2table[-num_table_data:])    # 添加表格，类型+num_table_data行数据
    sender.img2html(os.path.join(settings.folder, img_name+'.png'), img_tag)     # 添加折线图


def bug_count_report2(settings, sender, data2file):
    driver = ZenTao(settings)
    sheet_index = 1
    img_name = 'P1Pro播控'
    img_tag = 'RemoteControl'
    title = 'P1Pro 一体播控BUG概况曲线图： '
    project = 'P系列/P1pro_一体播控'
    num_table_data = settings.num_table_data
    num_img_data = settings.num_img_data

    data = driver.bug_search_case1(project)
    driver.driver.close()
    data2file.data2xls(data, sheet_index)
    data2file.data2img(img_name, num_img_data, sheet_index)
    data2table = data2file.read_xls(sheet_index)
    sender.text2html(title, weight=True)
    if num_table_data > len(data2table)-1:
        num_table_data = len(data2table) - 1
    sender.table2html([data2table[0]] + data2table[-num_table_data:])
    sender.img2html(os.path.join(settings.folder, img_name+'.png'), img_tag)


def bug_count_report3(settings, sender, data2file):
    driver = ZenTao(settings)
    sheet_index = 2
    img_name = 'P1Pro外部'
    img_tag = 'P1Pro_EX'
    title = 'P1Pro 外部禅道BUG概况曲线图： '
    project = 'P1_Pro'
    num_table_data = settings.num_table_data
    num_img_data = settings.num_img_data

    data = driver.bug_search_case3(project)
    driver.driver.close()
    data2file.data2xls(data, sheet_index)
    data2file.data2img(img_name, num_img_data, sheet_index)
    data2table = data2file.read_xls(sheet_index)
    sender.text2html(title, weight=True)
    if num_table_data > len(data2table) - 1:
        num_table_data = len(data2table) - 1
    sender.table2html([data2table[0]] + data2table[-num_table_data:])
    sender.img2html(os.path.join(settings.folder, img_name+'.png'), img_tag)


def str_count(data, count_index):
    """
    统计某一列中数据出现次数
    :param data: 2d list
    :param count_index: 统计数据所在列数
    :return data_assign_list:  数据
    :return data_assign_counts:  数据统计个数
    """
    data_assign = []
    data_assign_counts = []
    for i in range(0, len(data)):
        data_assign.append(data[i][count_index])
    data_assign_set = set(data_assign)
    for j in data_assign_set:
        data_assign_count = data_assign.count(j)
        data_assign_counts.append(data_assign_count)
    data_assign_list = list(data_assign_set)
    print(data_assign_list, data_assign_counts)
    return data_assign_list, data_assign_counts


def p1_bug_report(settings, sender, data2file):
    driver = ZenTao(settings)
    sheet_name = 'P1ProP1'
    xls_name = 'buglist.xls'
    img_name = 'P1Pro_P1'
    img_tag = 'P1Pro_P1'
    title = 'P1Pro Launcher C端一级BUG指派统计: '
    project = 'P系列/P1pro'
    p1pro_p1_col = ['Bug编号', '严重程度', '优先级', '标题', 'Bug状态', '指派给']

    bug_count, data = driver.bug_search_case2(project, driver.xpath.search_value1_chosen2)
    driver.driver.close()

    sender.text2html(title, weight=True)
    if bug_count > 0:
        data_assign_list, data_assign_counts = str_count(data, 5)

        data.insert(0, p1pro_p1_col)
        data2file.bug_list2xls(data, os.path.join(settings.folder, xls_name), sheet_name)
        data2file.data2img_bar(img_name, data_assign_list, data_assign_counts)
        sender.table2html(data)
        sender.img2html(os.path.join(settings.folder, img_name+'.png'), img_tag)
        sender.add_attach(xls_name)
    else:
        sender.text2html('无一级Bug。', weight=False)


if __name__ == '__main__':
    """
    如果增加新的表，需在report.xls中添加新的sheet，并在第一行添加title
    """
    _settings = Settings()
    _data2file = Data2file(_settings)
    _sender = SendEmail(_settings)

    # 添加函数
    p1_bug_report(_settings, _sender, _data2file)
    bug_count_report1(_settings, _sender, _data2file)
    bug_count_report2(_settings, _sender, _data2file)
    bug_count_report3(_settings, _sender, _data2file)

    _sender.add_html()
    _sender.add_attach(_settings.xls)
    _sender.send_email()

