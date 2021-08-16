import telebot
import random
import traceback
from bs4 import BeautifulSoup
import requests
bot = telebot.TeleBot('Telegram token')
@bot.message_handler(commands=['checkapprating'])
def check(message):
	try:
		text = message.text
		text = text.split(' ')
		appname = text[1]
		url = 'https://play.google.com/store/apps/details?id='+appname
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')
		quotes = str(soup.find('span',class_="AYi5wd TBRnV")).split('"')[3].split(' ')[0]
		soup = BeautifulSoup(response.text, 'lxml')
		rare = str(soup.find('div',class_="pf5lIe")).split('"')[3].split(' ')[1]
		bot.send_message(message.chat.id,"👤"+quotes+" всего оценок\n⭐️"+rare+" оценка приложения")
	except Exception:
		bot.send_message(message.chat.id,traceback.format_exc())

bot.polling(none_stop=True)
