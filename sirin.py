#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#sirin.py

import telegram
import time
import requests
from telegram.ext import Updater
from telegram.ext import CommandHandler

tk = '879508978:AAFr1ngABRI9vP2r2Jl9K58hlCwn4vPinAc'

bot = telegram.Bot(token=tk)
updater = Updater(token=tk,use_context=True)

'''
#本地测试用
url = 'sock5://127.0.0.1:10808'
proxy = telegram.utils.request.Request(proxy_url=url)
bot = telegram.Bot(token=tk,request=proxy)
updater = Updater(token=tk, request_kwargs={'proxy_url': 'http://127.0.0.1:10809'},use_context=True)
'''

dispatcher = updater.dispatcher

def start(update,context):
    context.bot.sendPhoto(chat_id=update.effective_chat.id,photo=open('resource/0_error.jpg', 'rb'))
    
def yurui(update,context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="boom!")
    
def yurui_test(update,context):
    context.bot.sendSticker(chat_id=update.effective_chat.id,sticker="CAACAgUAAxkBAAIBQV8nvdnbQqb1NLH2Z0PjEH9xvO2qAAJYAAPFBioILE-pYyaFaRYaBA")
    
start = CommandHandler('start',start)
boom = CommandHandler('yurui', yurui)
yuruiTest = CommandHandler('yurui_test',yurui_test)

dispatcher.add_handler(start)
dispatcher.add_handler(boom)   
dispatcher.add_handler(yuruiTest) 

#print(telegram.update)

updater.start_polling()
