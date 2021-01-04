## Day32
學習有關電子郵件SMTP和日期時間模組的用法。

## 中文問題  
### 需設定成utf8
from email.mime.text import MIMEText  
mime=MIMEText("您好! 我是 Tony.", "plain", "utf-8")  
mime["Subject"]="Gmail sent by Python scripts(MIME)"  
mime["From"]="Your best friend"  
mime["To"]="mailgroup"  
mime["Cc"]="myyahoomail@yahoo.com, mycompanymail@blablabla.com.tw"  
msg=mime.as_string()  

## 練習題
自動發送email程式
exercise
