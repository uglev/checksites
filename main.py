import urllib.request
from urllib.request import urlopen
import os
from time import time
from math import pi
import telebot
from dotenv import find_dotenv, load_dotenv, set_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

urls = ['https://uglev.com',
        'https://uglev.net',
        'https://uglev.ru']

bot = telebot.TeleBot(token=TELEGRAM_TOKEN)

def send_message(message):
    new_id_message = bot.send_message(chat_id=CHAT_ID, text=message)

def check_dns(url):
    try:
        return urllib.request.urlopen(url).getcode()
    except:
        return pi

def check_speed(url):
    try:
        website = urlopen(url)
        open_time = time()
        output = website.read()
        close_time = time()
        website.close()
        return round(close_time - open_time, 3)
    except:
        return pi

for url in urls:
    #print(url, check_dns(url), check_speed(url))
    if check_dns(url) != 200 or check_speed(url) >= 1:
        send_message(f'Сайт {url} недоступен!')
