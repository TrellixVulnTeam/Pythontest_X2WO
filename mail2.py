# -*- coding: utf-8 -*-
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = 'smtp.exmail.qq.com'
port = 25
user = 'me@zhanxueyou.me'
password = '895544Zhanxueyou'
recv = 'zhanxueyou@rqbao.com'

def main():
    if len(sys.argv) < 4:
        raise Exception('argument number must be 3')
    to = sys.argv[1]
    title = sys.argv[2]
    content = sys.argv[3]

    smtp = smtplib.SMTP(host, port)
    smtp.login(user, password)

    msg = MIMEMultipart()
    msg['From'] = user
    msg['to'] = to
    msg['Subject'] = title
    msg.attach(MIMEText(content))

    print(msg)
    smtp.sendmail(user, to, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    main()

