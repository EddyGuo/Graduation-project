#!/usr/bin/python
# -*- coding: UTF-8 -*-


import xlrd
import xlwt
from xlutils.copy import copy
from pyecharts import Line, Bar
import os
import tinify


class Data2file:
    def __init__(self, settings):
        """
        Convert data into image or excels.
        :param settings: Settings.
        """
        self.settings = settings
        self.folder = self.settings.folder
        self.report_name = os.path.join(self.folder, self.settings.xls)
        self.row_type = self.settings.time_now
        self.col_type = self.settings.bug_type
        # 启用tinify压缩
        tinify.key = self.settings.tinify_key

    @staticmethod
    def bug_list2xls(table, xls, sheet):
        """
        Generate excel table. Overwrite excel.
        :param table: 2d list.
        :param xls: Excel name.
        :param sheet:Sheet name.
        :return:
        """
        wb = xlwt.Workbook()
        sheet1 = wb.add_sheet(sheet)
        for i in range(0, len(table)):
            for j in range(0, len(table[0])):
                sheet1.write(i, j, table[i][j])
        wb.save(xls)

    def data2xls(self, data, sheet_index=0):
        """
        Add data to excel. Update excel.
        :param data: List.
        :param sheet_index: Index of excel sheets.
        :return:
        """
        rb = xlrd.open_workbook(self.report_name)
        rs = rb.sheet_by_index(sheet_index)
        wb = copy(rb)
        ws = wb.get_sheet(sheet_index)
        if rs.cell_value(rs.nrows-1, 0) != self.row_type:
            ws.write(rs.nrows, 0, self.row_type)
            for i in range(len(self.col_type)):
                ws.write(rs.nrows, i+1, data[i])
        wb.save(self.report_name)

    def data2img(self, title, rows, sheet_index=0):
        """
        Render line chart.
        :param title: Chart title.
        :param sheet_index: Index of excel sheets.
        :param rows: The maximum of data.
        :return:
        """
        rb = xlrd.open_workbook(self.report_name)
        rs = rb.sheet_by_index(sheet_index)
        if rows < rs.nrows:
            # 控制图像数据数量
            n_rows = rows
        else:
            n_rows = rs.nrows
        data_type = []
        bug_line = Line(title)
        for i in range(0, len(self.col_type)+1):
            data_list = []
            for j in range(rs.nrows-n_rows, rs.nrows):
                data_list.append(rs.cell_value(j, i))
            data_type.append(data_list)
            if i > 0:
                bug_line.add(self.col_type[i-1], data_type[0], data_type[i])

        bug_line.render(os.path.join(self.folder, title+'.html'))
        img_path = os.path.join(self.folder, title+'.png')
        bug_line.render(path=img_path)
        tinify.from_file(img_path).to_file(img_path)
        print('图片压缩成功')

    def data2img_bar(self, title, x, y):
        """
        Render bar chart.
        :param title: Chart title.
        :param x: X-axis.
        :param y: Y-axis.
        :return:
        """
        bar = Bar(title)
        bar.add("", x, y)
        bar.render(os.path.join(self.folder, title+'.html'))
        img_path = os.path.join(self.folder, title+'.png')
        bar.render(path=img_path)
        tinify.from_file(img_path).to_file(img_path)
        print('图片压缩成功')

    def read_xls(self, sheet_index=0):
        """
        Read excel data.
        :param sheet_index: Index of excel sheets.
        :return: 2d list.
        """
        rb = xlrd.open_workbook(self.report_name)
        rs = rb.sheet_by_index(sheet_index)
        data = []
        for i in range(0, rs.nrows):
            data_row = []
            for j in range(0, rs.ncols):
                cell = rs.cell_value(i, j)
                if isinstance(cell, float):
                    cell = int(cell)
                data_row.append(cell)
            data.append(data_row)

        return data


if __name__ == '__main__':
    """调试"""
    tinify.key = '3k1rKxY7xTpFdsm98ZHHBcdv0CKfsJzX'
    tinify.from_file('attach\\P1Pro.png').to_file('attach\\P1Pro.png')
    print('压缩成功')
