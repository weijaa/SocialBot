import requests
import re
from bs4 import BeautifulSoup
import random

url = 'http://news.fcu.edu.tw/wSite/lp?ctNode=31973&mp=101001&idPath='

view = requests.get(url)

soup = BeautifulSoup(view.text, 'html.parser')

report = soup.find_all('a', href = re.compile('http://web.pr.fcu.edu.tw/~pr/fest*'))

news = []
link = []

for i in report:
    if '力' in i.text:
        news.append(i.text)
        link.append(i['href'])
num = random.randint(0,len(news)-1)
print(num)
print(news[num])
print('link：',link[num])


