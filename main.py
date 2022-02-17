import telebot
import random
import traceback
from bs4 import BeautifulSoup
import requests
bot = telebot.TeleBot('')
@bot.message_handler(commands=['checkapprating'])
def check(message):
	try:
		text = message.text
		text = text.split(' ')
		try:
			url = text[1]
			response = requests.get(url)
			soup = BeautifulSoup(response.text, 'lxml')
			quotes = str(soup.find('span',class_="AYi5wd TBRnV")).split('"')[3].split(' ')[0]
			soup = BeautifulSoup(response.text, 'lxml')
			rare = str(soup.find('div',class_="BHMmbe")).split("=")[1].split('"')[1]
			bot.send_message(message.chat.id,"👤"+quotes+" всего оценок\n⭐️"+rare)
		except:
			bot.send_message(message.chat.id,"Вы не дали ссылку на приложение\n"+traceback.format_exc())
	except Exception:
		bot.send_message(message.chat.id,traceback.format_exc())

bot.polling(none_stop=True)
