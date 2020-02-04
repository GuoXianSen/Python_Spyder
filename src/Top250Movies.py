"""
@author:Clay_Guo
@time:2020/2/4 23:13
@filename:Top250Movies.py
"""
import requests
from bs4 import BeautifulSoup
from time import sleep
import pprint

page_index = list(range(1))

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/75.0.3770.142 Safari/537.36 "
}


# print(type(page_index))
# print(page_index)

def download_all_htmls():
    htmls = []
    for idx in page_index:
        url = f"https://movie.douban.com/top250?start={idx}&filter="
        print("正在爬取的网页为:", url)
        r = requests.get(url, headers=header)
        if r.status_code != 200:
            raise Exception("Http错误代码，非200")
        htmls.append(url)
        sleep(1)
    return htmls


htmls = download_all_htmls()

print(htmls[0].text)

def parse_single_html(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    article_items = (
        soup.find("div", class_="article")
            .find("ol", class_="grid_view")
            .find_all("div", class_="item")
    )
    datas = []
    for article_item in article_items:
        rank = article_item.find("div", class_="pic").find("em").get_text()
        info = article_item.find("div", class_="info")
        title = info.find("div", class_="hd").find("span", class_="title").get_text()
        stars = (info.find("div", class_="bd").find("div", class_="star").find_all("span"))
        rating_star = stars[0]["class"]
        rating_num = stars[1].get_text()
        comment_num = stars[3].get_text()
        datas.append({
            "rank": rank,
            "title": title,
            "rating_star": rating_star.replace("rating", "").replace("-t", ""),
            "rating_num": rating_num,
            "comment_num": comment_num.replace("人评价", "")
        }
        )
    return datas


# pprint.pprint(parse_single_html(htmls[0]))
