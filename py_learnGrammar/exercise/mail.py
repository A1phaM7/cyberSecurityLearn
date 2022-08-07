import imp
import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 收件人和发件人
sender = 'student@woniuxy.com'
receiver = 'dengqiang@woniuxy.com'      

# 构建邮件的主体对象
msg = MIMEMultipart()
msg['subject'] = 'Python测试邮件'
msg['From'] = sender
msg['To'] = receiver

body = '''
<div style = font-size:30px;color:red;'>这是一个邮件的正文</div>
'''

# 附件

content = MIMEText(body,'html','utf-8')
msg.attach(content)

# 建立与邮件服务器的连接并发送邮件
smtpObj = smtplib.SMTP()
smtpObj.connect('mail.woniuxy.com','25')
smtpObj.login(user=sender, password='Student123')       
smtpObj.sendmail(sender, receiver, str(msg))
smtpObj.quit() 