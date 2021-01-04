import smtplib

my_email="17app002@gmail.com"
password="me516888888888"

with smtplib.SMTP("smtp.gmail.com") as connect:
    #TLS傳輸層安全(加密)
    connect.starttls()

    connect.login(user=my_email,password=password)
    connect.sendmail(from_addr=my_email,
    to_addrs="17app001@gmail.com",
    msg="Subject:Hello2\n\nThis is the body of my email.")

    

'''
需降低安全層級
返回google mail進行設定
'''



