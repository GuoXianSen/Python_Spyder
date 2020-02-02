"""
@author:Clay_Guo
@time:2020/2/2 23:15
@filename:SpyderWholeWeb.py
"""
# 爬取整个网页
import requests
from bs4 import BeautifulSoup
from time import sleep

url = "https://www.clayguo.tech"

html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')

list1 = soup.find_all('a', 'post-title-link')
print(len(list1))
for title in list1:
    sleep(1)
    print("网页正在爬取中....")
    print("文章标题为：" + title.string, end=" ")
    print("目标地址为：" + url + '/' + title['href'])


