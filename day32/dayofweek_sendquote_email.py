
from email.mime.text import MIMEText
import smtplib
import datetime as dt
import random

my_email = "17app002@gmail.com"
password = "me516888888888"
smtp = "smtp.gmail.com"


def sendEmail(to_addrs, subject, body):
    with smtplib.SMTP(smtp) as connect:
        # TLS傳輸層安全(加密)
        connect.starttls()
        connect.login(user=my_email, password=password)
        # 解決中文問題
        mime = MIMEText(body, "plain", "utf-8")
        mime["Subject"] = subject
      
        email_msg = mime.as_string()
        connect.sendmail(from_addr=my_email,
                         to_addrs="17app001@gmail.com",
                         msg=email_msg)
        print(f'信件發送至{to_addrs} 成功!')


now = dt.datetime.now()
print(now)
day_of_week = now.weekday()

# 周一發送激勵信件
if day_of_week == 0:
    quotes = []
    with open('quotes.txt', encoding='utf-8') as f:
        quotes = f.readlines()

    if len(quotes) > 0:
        print('周一，信件發送中...')
        today_quote = quotes[random.randint(0, len(quotes))]
        sendEmail('vita0702@gmail.com', '今日佳句', today_quote)
