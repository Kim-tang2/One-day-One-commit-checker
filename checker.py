import requests
from bs4 import BeautifulSoup
import datetime
import time
from multiprocessing import Pool


def convertDate(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").date()


beforeWeek = datetime.date.today() - datetime.timedelta(weeks=1)  # 일주일 전 날짜
weeks = ['(월)', '(화)', '(수)', '(목)', '(금)', '(토)', '(일)']
users = ['Kim-tang2', 'bell2lee', 'kimgyuri', 'sunwoopia',
         'wwjdtm', 'jhg3522', 'Chord-West', 'hyeonn',
         'hyeonsang010716', 'youngho-C', 'ddugel3',
         'KMUsungwon', 'kookminju']

usersDic = {'Kim-tang2': '김태훈', 'bell2lee': '이종휘', 'kimgyuri': '김규리',
            'sunwoopia': '김선우', 'wwjdtm': '김윤정', 'jhg3522': '정현구',
            'Chord-West': '김현서', 'hyeonn': '임이현', 'hyeonsang010716': '조현상',
            'youngho-C': '차영호', 'ddugel3': '최건웅', 'KMUsungwon': '임성원',
            'kookminju': '김민주'
            }


def getCommitData(user):
    response = requests.get('https://github.com/' + user)
    html = BeautifulSoup(response.content, 'html.parser')
    commitDatas = html.select('rect.day')

    print(usersDic[user] + "님의 최근 7일 커밋입니다.")
    for commitData in commitDatas:
        if convertDate(commitData.attrs['data-date']) >= beforeWeek:
            date = commitData.attrs['data-date']
            dayOfTheWeek = convertDate(date).weekday()
            count = commitData.attrs['data-count']
            print(date, weeks[dayOfTheWeek], count)


if __name__ == '__main__':
    startTime = time.time()
    with Pool(processes=4) as pool:
        pool.map(getCommitData, usersDic)

    print(time.time() - startTime)
