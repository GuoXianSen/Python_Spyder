"""
@author:Clay_Guo
@time:2020/2/3 0:15
@filename:doubanTop250.py
"""
# 爬取豆瓣top250榜单
import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250"

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/75.0.3770.142 Safari/537.36 "
}

html = requests.get(url, headers=header)
soup = BeautifulSoup(html.content,'html.parser')

movie = soup.find_all('div', 'hd')
print(movie[0].a.span.string)

# print(movie)


# print(html)
