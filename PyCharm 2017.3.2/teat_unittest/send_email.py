from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


# 发送邮件服务器地址
smtp_server = 'smtp.qq.com'
username = '179644835'
password = 'hdaotwqnzkaabhjb'

smtp = SMTP()
smtp.connect(host=smtp_server)
ret = smtp.login(username, password)
print(ret)

# todo 编写邮件正文
# msgroot = MIMEText('<h1>python</h1>','html','utf-8')
# msgroot = MIMEText('<h1>python</h1>','html','utf-8')

# todo 邮件标题
# msgroot['Subject'] = Header('sendemail','utf-8')

# todo 发送附件
subject = '发送一个附件'
# 发送html文件
with open(r"D:\PyCharm 2017.3.2\teat_unittest\test_case\report.html") as f:
    sendfile = f.read()
# data = MIMEText(sendfile,'base64','utf-8')
data = MIMEText(sendfile,'html','utf-8')
data['Content-Type'] = 'application/octet-stream'
# data['Content-Disposition'] = "attachment;filename='test.txt'"


# 发送一个普通的文件
# with open('./test.txt') as f:
#     sendfile = f.read()
# data = MIMEText(sendfile,'base64','utf-8')
# data['Content-Type'] = 'application/octet-stream'
# data['Content-Disposition'] = "attachment;filename='test.txt'"


# 将附件加载到正文
msgroot = MIMEMultipart('related')
msgroot['Subject'] = subject
msgroot.attach(data)


smtp.sendmail('179644835@qq.com','179644835@qq.com',msgroot.as_string())
smtp.quit()
