import telebot
from conf import TOKEN, lis
from scripts import Converter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(message, f'Чтобы перевести курс валюты из одного в другой. \
Введите через пробел валюту которую надо перевести, валюту В которую надо перевести и количество переводимой валюты.\n\
Список доступных валют можно узнать введя команду (/value)')

@bot.message_handler(commands=['value'])
def value(message):
    text = ''
    for i in lis.keys():
        text = text + ' ' + i
    bot.reply_to(message, f'Список доступных валют:{text}.')

@bot.message_handler(content_types=['text'])
def converter(message):
    bot.reply_to(message, Converter().converter(message.text))


bot.polling(none_stop=True)
