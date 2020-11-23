import requests
from bs4 import BeautifulSoup
import datetime

beforeWeek = datetime.date.today() - datetime.timedelta(weeks=1) #일주일 전 날짜


response = requests.get('https://github.com/Kim-tang2')
html = BeautifulSoup(response.content, 'html.parser')
commitDatas = html.select('rect.day')

for commitData in commitDatas:
    if(datetime.datetime.strptime(commitData.attrs['data-date'], "%Y-%m-%d").date() >= beforeWeek):
        date = commitData.attrs['data-date']
        count = commitData.attrs['data-count']
        print(date, count)



