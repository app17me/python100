# Day32
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

# Day41  
學習HTML&CSS  
google==>216.58.210.46  
文件；HTML，CSS和JavaScript  
HTML:網站的架構  
CSS:網站的外觀  
JavaScript:實際建構者(功能)  
<h1>~<h6>
字級大小
<p>
段落
<br>
換行
<em>
斜體
<strong>
粗體
<ul><li>
無序列表
<ol><li>
有序列表
<img src=" " alt="圖形未顯示得提示字 ">
讀取圖形 
<a href=" ">提示文字</a>
連結路徑  



# Day42  
1.表格的使用方式
<table>
<tr> ==><table row>   列
<td> ==><table data>  資料
<tbody>
<tfoot>


2.使用form表單輸入資料
3.網站上傳github
4.https://app17me.github.io/cv/


# Day43
1.css使用方式
2.inner
3.head
4.css file

5.tag selectors
6.class selectors
7.id selectors

class selectors可以套用多個

# Day44
1.css 進階用法