# Python_Spyder
> 记录Python爬虫学习过程

## 与爬虫相关的库

### requests

官方中文文档地址：[传送门](http://2.python-requests.org/zh_CN/latest/index.html)

`requests`是一个Python第三方库，用于处理url资源

#### 使用方法

```python
import requests

url = "https://www.clayguo.tech"
html = requests.get(url)

```



### BeautifulSoup

官方中文文档地址：[传送门](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#)

`BeautifulSoup`是一个Python第三方库，用于解析网页或者xml文件





#### 使用方法

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```



