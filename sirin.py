#!/usr/lib/python3
# _*_ coding:utf-8 _*_
#sirin.py

import telegram
import time
from telegram.ext import Updater
from telegram.ext import CommandHandler

tk = '879508978:AAFr1ngABRI9vP2r2Jl9K58hlCwn4vPinAc'

bot = telegram.Bot(token=tk)
updater = Updater(token=tk,use_context=True)
dispatcher = updater.dispatcher

def yurui(update,context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="boom!")
    
def yurui_test(update,context):
    context.bot.sendSticker(chat_id=update.effective_chat.id,sticker="CAACAgUAAxkBAAIBQV8nvdnbQqb1NLH2Z0PjEH9xvO2qAAJYAAPFBioILE-pYyaFaRYaBA")
    
boom = CommandHandler('yurui', yurui)
yuruiTest =CommandHandler('yurui_test',yurui_test)

dispatcher.add_handler(boom)   
dispatcher.add_handler(yuruiTest) 

updater.start_polling()
