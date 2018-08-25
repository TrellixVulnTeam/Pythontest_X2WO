# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

sender = 'me@zhanxueyou.me'
password = '895544Zhanxueyou'

receiver = 'zhanxueyou@chainup.com'

smtp_server = 'smtp.exmail.qq.com'
smtp_port = 25

server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()
server.login(sender,password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()

