import requests
import slack
from bs4 import BeautifulSoup as BS
from datetime import datetime


with open('token.txt','r') as f:
    SLACK_TOKEN = f.read()
    f.close()

currentDate = datetime.now()

try:
    client = slack.WebClient(token=SLACK_TOKEN)
    print ("[PyCalendar]"+currentDate.strftime('%Y-%m-%d %H:%M:%S')+" Le bot est connecté à Slack!")
except:
    print ("[PyCalendar]"+currentDate.strftime('%Y-%m-%d %H:%M:%S')+" Le bot n'a pas pu se connecter à Slack!")
    exit()

def getTodayQuestion():
    currentDate = datetime.now()
    today = currentDate.strftime('%d')
    req = "https://adventmyfriend.com/198081/f9ccdd2795/"+today+"/"
    result = requests.get(req)
    html = result.text
    soup = BS(html,"html.parser")
    try:
        question = soup.find('div',{'class':'day_message_container'})
        send="La question du jour est: \n \n" + question.string
        client.chat_postMessage(channel='christmas-calendar',text=send)
        print ("[PyCalendar]"+currentDate.strftime('%Y-%m-%d %H:%M:%S')+" La question du jour "+today+" a été envoyé!")
    except:
        print ("[PyCalendar]"+currentDate.strftime('%Y-%m-%d %H:%M:%S')+" La question du jour "+today+" n'a pas été récupéré!")

def getTomorowQuestion():
    currentDate = datetime.now()
    tomorrow = str(int(currentDate.strftime('%d'))+1)
    req = "https://adventmyfriend.com/198081/f9ccdd2795/"+tomorrow+"/"
    result = requests.get(req)
    html = result.text
    soup = BS(html,"html.parser")
    try:
        question = soup.find('div',{'class':'day_message_container'})
        send="La question du jour est: \n \n" + question.string
        client.chat_postMessage(channel='christmas-calendar',text=send)
        print ("[PyCalendar]"+currentDate.strftime('%Y-%m-%d %H:%M:%S')+" La question du jour "+tomorrow+" a été envoyé!")
    except:
        print ("[PyCalendar]"+currentDate.strftime('%Y-%m-%d %H:%M:%S')+" La question du jour "+tomorrow+" n'a pas été récupéré!")

getTodayQuestion()
getTomorowQuestion()
