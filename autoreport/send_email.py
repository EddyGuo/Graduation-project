import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.qiye.163.com"            # 设置服务器
mail_user = "cunnian.guo@dpvr.cn"          # 用户名
mail_pass = "Dpv18403492721"               # 口令

sender = 'cunnian.guo@dpvr.cn'
receivers = ['cunnian.guo@dpvr.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("菜鸟教程", 'utf-8')
msgRoot['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p><strong>P1Pro Launcher C端BUG概况曲线图：</strong></p>
<table width="600" border="1" cellspacing="2">
    <tr>
        <td><strong>TIme</strong></td>
        <td><strong>Closed</strong></td>
        <td><strong>Not Closed</strong></td>
        <td><strong>Activated</strong></td>
        <td><strong>P1(Activated)</strong></td>
        <td><strong>P2(Activated)</strong></td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
</table>
<p><img src="cid:snapshot" alt="P1Pro_Launcher_Bug_Line" height="400" height="800"/></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('snapshot.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<snapshot>')
msgRoot.attach(msgImage)

# 添加附件1
att1 = MIMEText(open('report.xls', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="report.xls"'
msgRoot.attach(att1)

# 添加附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('render.html', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="render.html"'
msgRoot.attach(att2)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

