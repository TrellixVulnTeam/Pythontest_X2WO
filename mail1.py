# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp_host = 'smtp.exmail.qq.com'
# smtp_port = 25
sender = 'me@zhanxueyou.me'
receiver = 'zhanxueyou@chainup.com'
user = 'me@zhanxueyou.me'
password = ''
subject = 'python email test测试验证报错'


msg = MIMEText('hello', 'text', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
# smtp.connect(smtp_host, smtp_port)
smtp.connect(smtp_host)     # 不需要port也能发送成功
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
