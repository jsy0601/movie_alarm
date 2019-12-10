import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from telegram.ext import Updater, MessageHandler, Filters
from datetime import datetime

# 오늘 날짜 구해오기
now = datetime.now()


def day_fungtion() :
    if (now.day <10):
        return '0'+str(now.day)
    else :
        return str(now.day)

# 날짜 문자형으로 변환
year = str(now.year)
month = str(now.month)
day= day_fungtion()
# print(day)
today = year + month + day
print(today)


my_token = '1039755136:AAGlJnHWrw3762j4uVQFh_8bXxOfh5C0PxE'
bot = telegram.Bot(token = my_token)
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0059&date='+today

updates  = bot.getUpdates() # 업데이트 내역을 받아옴
chat_id = bot.getUpdates()[-1].message.chat.id #가장 최근에 온 메세지의 chat id를 가져옵니다
new_msg = bot.getUpdates()[-1].message.text
# print(new_msg)


bot.sendMessage(chat_id=chat_id,text='4D영화는 1번, IMAX는 2번을 입력해주세요!!*^^*')

def job_fungtion():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    forDX = soup.select_one('span.forDX')
    if(forDX):
        forDX = forDX.find_parent('div', class_='col-times')
        title = forDX.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=chat_id,text=title + ' 4D 예매가 열렸습니다~~!!!')
        sched.pause()
    else:
        bot.sendMessage(chat_id=chat_id,text='4D 예매가 아직 열리지 않았습니다.')



# def job_fungtion():
#     html = requests.get(url)
#     soup = BeautifulSoup(html.text, 'html.parser')
#     forDX = soup.select_one('span.forDX')
#     if(forDX):
#         forDX = forDX.find_parent('div', class_='col-times')
#         title = forDX.select_one('div.info-movie > a > strong').text.strip()
#         return title
#     else:
#         return no_title
#
# ismovie = job_fungtion()
# print(ismovie)

# def get_message(bot, update) :
#     if(update.message.text == '1'):
#         update.message.reply_text("4D를 선택하셨군요!!!") #상대방으로부터 메세지 받았을때


    # update.message.reply_text(update.message.text) #상대방 말한거 그대로 말하기

# 텔레그램과 상호 처리를 위한 객체
# updater = Updater(my_token)
# # 메세지를 처리하기 위한 핸들거
# message_handler = MessageHandler(Filters.text, get_message)
# # 디스패처 핸들러 추가
# updater.dispatcher.add_handler(message_handler)
# #
# updater.start_polling(timeout=3, clean=True)
# updater.idle()



# for u in updates :
#     # print(u.message.text, u.message.chat_id)
#     print(chat_id)
#
# def job_fungtion():
#     html = requests.get(url)
#     soup = BeautifulSoup(html.text, 'html.parser')
#     forDX = soup.select_one('span.forDX')
#     if(forDX):
#         forDX = forDX.find_parent('div', class_='col-times')
#         title = forDX.select_one('div.info-movie > a > strong').text.strip()
#         bot.sendMessage(chat_id=951368755,text=title + ' 4D 예매가 열렸습니다.')
#         # sched.pause()
#           # 알림 보내고 나서 스케줄러 중지
#     # else:
#     #     bot.sendMessage(chat_id=951368755,text='4D 예매가 아직 열리지 않았습니다.')
#

# 블로킹 스케줄러 선언
sched = BlockingScheduler()
sched.add_job(job_fungtion, 'interval',seconds=1)
# 스케줄러에 펑션 등록, 일정간격마다 반복하겠다, 30초에 한번씩
sched.start()
