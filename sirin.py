#!/usr/lib/python3
# _*_ coding:utf-8 _*_
#sirin.py

import telegram
import time
from telegram.ext import Updater
from telegram.ext import CommandHandler

tk = '879508978:AAFr1ngABRI9vP2r2Jl9K58hlCwn4vPinAc'

bot = telegram.Bot(token=tk)
updater = Updater(token=tk)
dispatcher = updater.dispatcher

def yurui(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="boom!")
    
boom = CommandHandler('yurui', yurui)
dispatcher.add_handler(boom)    

updater.start_polling()
