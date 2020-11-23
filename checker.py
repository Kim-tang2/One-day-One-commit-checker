import requests
from bs4 import BeautifulSoup
import datetime

def convertDate(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").date()

beforeWeek = datetime.date.today() - datetime.timedelta(weeks=1) #일주일 전 날짜

weeks = ['(월)', '(화)', '(수)', '(목)', '(금)', '(토)', '(일)']

response = requests.get('https://github.com/Kim-tang2')
html = BeautifulSoup(response.content, 'html.parser')
commitDatas = html.select('rect.day')

for commitData in commitDatas:
    if(convertDate(commitData.attrs['data-date']) >= beforeWeek):
        date = commitData.attrs['data-date']
        dayOfTheWeek = convertDate(date).weekday()
        count = commitData.attrs['data-count']
        print(date, weeks[dayOfTheWeek], count)



