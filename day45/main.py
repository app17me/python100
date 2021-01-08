from bs4 import BeautifulSoup
import lxml

with open('day45/website.html',encoding='utf-8') as file:
    contents=file.read()

soup=BeautifulSoup(contents,'lxml')

print(soup)

print(soup.title.text)

