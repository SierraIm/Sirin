# coding=utf-8

import telepot
import pprint
import time
from telepot.loop import MessageLoop

bot = telepot.Bot('879508978:AAFr1ngABRI9vP2r2Jl9K58hlCwn4vPinAc')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint(msg)
    
    if msg['text']=='/ping':
        bot.sendMessage(chat_id,'boom!')
        
    if msg['text']=='/yurui':
        bot.sendMessage(chat_id,'boom!')


MessageLoop(bot, handle).run_as_thread()

while(1):
    time.sleep(10)

