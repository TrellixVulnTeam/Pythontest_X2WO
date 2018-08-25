# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp_host = 'smtp.exmail.qq.com'
sender = 'me@zhanxueyou.me'
receiver = 'zhanxueyou@126.com'
user = 'me@zhanxueyou.me'
password = '895544Zhanxueyou'
subject = 'python email test'


msg = MIMEText('hello', 'text', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtp_host)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()