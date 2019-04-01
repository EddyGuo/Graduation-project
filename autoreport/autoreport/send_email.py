#!/usr/bin/python
# -*- coding: UTF-8 -*-


import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from autoreport.settings import Settings
from email.utils import parseaddr, formataddr
import os


class SendEmail:
    def __init__(self, settings):
        """
        Send email.
        :param settings: Settings
        """
        self.settings = settings

        self.msgRoot = MIMEMultipart('related')
        self.msgRoot['Subject'] = Header(self.settings.subject, 'utf-8')
        name, addr = parseaddr(self.settings.sender)
        self.msgRoot['From'] = formataddr((Header(name, 'utf-8').encode(), addr))
        receivers, to_addrs = self.read_addr(self.settings.receivers)
        cc, cc_addrs = self.read_addr(self.settings.cc)
        self.msgRoot['to'] = to_addrs
        self.msgRoot['cc'] = cc_addrs
        self.sender = self.settings.sender
        self.receivers = receivers + cc
        self.msg_html = ''
        self.msgAlternative = MIMEMultipart('alternative')
        self.msgRoot.attach(self.msgAlternative)

    @staticmethod
    def read_addr(name_email_list):
        """
        Format address. e.g. name<usr@mail.com> TO name and usr@mail.com
        :param name_email_list: name<usr@mail.com>
        :return email_list: name
        :return addrs_format: usr@mail.com
        """
        email_list = []
        email_header_list = []
        for i in range(0, len(name_email_list)):
            name, addr = parseaddr(name_email_list[i])
            email_list.append(addr)
            addr_format = formataddr((Header(name, 'utf-8').encode(), addr))
            email_header_list.append(addr_format)
        addrs_format = ",".join(email_header_list)
        return email_list, addrs_format

    def text2html(self, text, weight=False):
        """
        Insert the text to the HTML body.
        :param text: Single line text.
        :param weight: Font Weight. True/False.
        :return:
        """
        if weight:
            text = '<strong>'+text+'</strong>'
        text_html = '<p>'+text+'</p>'
        self.msg_html = self.msg_html + text_html

    def table2html(self, data, width=1000):
        """
        Convert a 2d-array data to an HTML table.
        :param data: A 2d-array.
        :param width: Table Width. 1000 px.
        :return:
        """
        width = str(width)
        table_col = ''
        for i in range(0, len(data)):
            table_row = ''
            for j in range(0, len(data[0])):
                table_row = table_row+'<td>'+str(data[i][j])+'</td>'
            table_col = table_col+'<tr>'+table_row+'</tr>'
        table_html = '<table width="'+width+'" border="1" cellspacing="0">'+table_col+'</table>'
        self.msg_html = self.msg_html + table_html

    def img2html(self, img, tag, width=1000, height=500):
        """
        Insert the picture into the HTML body.
        :param img: Image Name.
        :param tag: The image HTML tag. Do not include non-code characters.
        :param width: Image Width. 1000 px.
        :param height: Image Height. 500 px.
        :return:
        """
        width = str(width)
        height = str(height)
        img_html = '<p><img src="cid:'+tag+'" alt="'+tag+'" width="'+width+'" height="'+height+'"/></p>'
        self.msg_html = self.msg_html+img_html
        with open(img, 'rb') as fp:
            msg_image = MIMEImage(fp.read())
        msg_image.add_header('Content-ID', '<' + tag + '>')
        self.msgRoot.attach(msg_image)

    def add_html(self):
        """
        Add HTML to the mail body.
        :return:
        """
        self.msgAlternative.attach(MIMEText(self.msg_html, 'html', 'utf-8'))

    def add_attach(self, file):
        """
        Add attachment.
        :param file: File name. e.g. xxx.xls
        :return:
        """
        att = MIMEText(open(os.path.join(self.settings.folder, file), 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="'+file+'"'
        self.msgRoot.attach(att)

    def send_email(self):
        """
        Send email.
        :return:
        """
        try:
            # 使用SSL验证，端口为465
            smtp_obj = smtplib.SMTP_SSL(self.settings.mail_host, 465)
            smtp_obj.login(self.settings.mail_user, self.settings.mail_pass)
            smtp_obj.sendmail(self.settings.sender, self.receivers, self.msgRoot.as_string())
            smtp_obj.quit()
            print('邮件发送成功')
        except smtplib.SMTPConnectError as e:
            print('邮件发送失败，连接失败:', e.smtp_code, e.smtp_error)
        except smtplib.SMTPAuthenticationError as e:
            print('邮件发送失败，认证错误:', e.smtp_code, e.smtp_error)
        except smtplib.SMTPSenderRefused as e:
            print('邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error)
        except smtplib.SMTPRecipientsRefused as e:
            print('邮件发送失败，收件人被拒绝:', e.recipients)
        except smtplib.SMTPDataError as e:
            print('邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error)
        except smtplib.SMTPException:
            print('邮件发送失败')


if __name__ == '__main__':
    """调试"""
    ts_settings = Settings()
    sender = SendEmail(ts_settings)
    sender.table2html([[1, 5, 5, 4, 5], [1, 5, 5, 4, 5]])
    sender.add_html()
    sender.add_attach('attach\\report.xls')
    sender.send_email()
