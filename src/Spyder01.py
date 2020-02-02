import re
import requests

url = "https://www.douban.com"

r = requests.get(url)

print(r.text)