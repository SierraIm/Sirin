#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#sirin.py

import telegram
import time
from telegram.ext import Updater
from telegram.ext import CommandHandler
import requests

tk = '1380016240:AAHQG1gTYvphbYcuDaHbtUUsy9uZ_RGJZIM'

bot = telegram.Bot(token=tk)
updater = Updater(token=tk,use_context=True)

'''
#本地测试用
url = 'http://127.0.0.1:10809'
tk = '971269998:AAFbzV3nltYGszPbZpyvNPmamvKv6wnMFxI'
proxy = telegram.utils.request.Request(proxy_url=url)
bot = telegram.Bot(token=tk,request=proxy)
updater = Updater(token=tk, request_kwargs={'proxy_url': 'http://127.0.0.1:10809'},use_context=True)
'''


dispatcher = updater.dispatcher

def ping(update,context):
    context.bot.sendPhoto(chat_id=update.effective_chat.id,photo=open('resource/0_error.jpg', 'rb'))
    
def yurui(update,context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="boom!")
    
def yurui_test(update,context):
    context.bot.sendSticker(chat_id=update.effective_chat.id,sticker="CAACAgUAAxkBAAIBQV8nvdnbQqb1NLH2Z0PjEH9xvO2qAAJYAAPFBioILE-pYyaFaRYaBA")  
ping = CommandHandler('ping',ping)
boom = CommandHandler('yurui', yurui)
yuruiTest = CommandHandler('yurui_test',yurui_test)

dispatcher.add_handler(ping)
dispatcher.add_handler(boom)   
dispatcher.add_handler(yuruiTest) 

print(telegram.update)

updater.start_polling()
