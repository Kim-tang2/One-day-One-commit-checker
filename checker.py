import requests
from bs4 import BeautifulSoup

response = requests.get('https://github.com/Kim-tang2')
html = BeautifulSoup(response.content, 'html.parser')
commitDatas = html.select('rect.day')

for commitData in commitDatas:
    date = commitData.attrs['data-date']
    count = commitData.attrs['data-count']
    print(date, count)