#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime


class Settings:
    def __init__(self):
        self.time_now = datetime.datetime.now().strftime('%Y/%m/%d')

        """
        邮箱设置：
        :param mail_host: SMTP服务器
        :param mail_user: 登录账户
        :param mail_pass: 登录密码
        :param sender: 发件人，name<usr@mail.com>
        :param receivers: 收件人，name<usr@mail.com>，多个收件人为一个数组
        :param cc: 抄送，同收件人
        :param subject: 邮件标题
        """
        self.mail_host = 'smtp.mxhichina.com'
        self.mail_user = 'cunnian.guo@dpvr.cn'
        self.mail_pass = 'Dpv18403492721'
        self.sender = '郭存念<cunnian.guo@dpvr.cn>'
        self.receivers = [
            '郭存念<cunnian.guo@dpvr.cn>'
        ]
        self.cc = [
            '郭存念<cunnian.guo@dpvr.cn>'
        ]
        self.subject = 'P1pro Bug统计 '+self.time_now

        """
        禅道设置：
        :param sleep_time: 模拟点击间隔时间，太小速度太快，可能无法找到元素
        :param in_address: 内部禅道
        :param in_account: 内部禅道账户
        :param in_password: 内部禅道密码
        :param ex_address: 外部禅道地址
        :param ex_account: 外部禅道密码
        :param ex_password: 外部禅道密码
        """
        self.sleep_time = 0.5
        self.in_address = 'http://192.168.0.90/zentaopms/www/'
        self.in_account = 'cunnian.guo'
        self.in_password = 'nianKJ0409'
        self.ex_address = 'http://182.254.139.206:8080/zentao/'
        self.ex_account = 'cunnian.guo'
        self.ex_password = 'nianKJ0409'

        """
        其他设置：
        :param folder: 生成附件所在文件夹位置，需手动修改
        :param xls: bug数据表
        :param num_table_data: 邮件表格显示最近的数据个数
        :param num_img_data: 邮件图像显示的最近的数据个数
        """
        self.folder = 'C:\\Users\\Administrator\\Desktop\\autoreport\\attach'  # 注意修改
        self.xls = 'report.xls'
        self.num_table_data = 4
        self.num_img_data = 120

        """
        图片压缩：
        使用邮箱登录https://tinypng.com/developers获取key，每个key每月可压缩500张图片
        参考地址：https://tinypng.com/developers/reference/python
        """
        self.tinify_key = '3k1rKxY7xTpFdsm98ZHHBcdv0CKfsJzX'

        self.bug_type = ['Closed', 'Not Closed', 'Activated', 'P1(Activated)', 'P2(Activated)']
