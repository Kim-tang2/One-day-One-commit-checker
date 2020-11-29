import requests
import asyncio
from functools import partial
from bs4 import BeautifulSoup
import datetime
import time

beforeWeek = datetime.date.today() - datetime.timedelta(weeks=1)  # 일주일 전 날짜
weeks = ['(월)', '(화)', '(수)', '(목)', '(금)', '(토)', '(일)']

usersDic = {'Kim-tang2': '김태훈', 'bell2lee': '이종휘', 'kimgyuri': '김규리',
            'sunwoopia': '김선우', 'wwjdtm': '김윤정', 'jhg3522': '정현구',
            'Chord-West': '김현서', 'hyeonn': '임이현', 'hyeonsang010716': '조현상',
            'youngho-C': '차영호', 'ddugel3': '최건웅', 'KMUsungwon': '임성원',
            'kookminju': '김민주'
            }

def convertDate(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").date()

async def getCommitData(url, user):
    loop = asyncio.get_event_loop()
    request = partial(requests.get, url, headers={'user-agent': 'Mozilla/5.0'})
    response = await loop.run_in_executor(None, request) #코루틴으로 짜여있지 않은 함수 비동기적으로 이용하기. 1번째 인자는 None으로 들어갈
                                                         #시 asyncio의 내장 executor가 들어감.

    html = BeautifulSoup(response.content, 'html.parser')
    commitDatas = html.select('rect.day')

    print(f'{usersDic[user]}님의 최근 7일 커밋입니다.')
    for commitData in commitDatas:
        if convertDate(commitData.attrs['data-date']) >= beforeWeek:
            date = commitData.attrs['data-date']
            dayOfTheWeek = convertDate(date).weekday()
            count = commitData.attrs['data-count']
            print(date, weeks[dayOfTheWeek], count)

async def main():
    baseUrl = 'https://github.com/{user}'

    futures = [asyncio.ensure_future(getCommitData(
        baseUrl.format(user=users), users)) for users in usersDic]

    await asyncio.gather(*futures)

if __name__ == '__main__':
    startTime = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main()) #main이라는 네이티브 코루틴이 끝날 때까지 기다림
    print(time.time() - startTime)
