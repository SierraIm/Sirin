# coding=utf-8

import telepot
import time
import pprint
import re
from telepot.loop import MessageLoop

bot = telepot.Bot('879508978:AAFr1ngABRI9vP2r2Jl9K58hlCwn4vPinAc')

pp = pprint.PrettyPrinter(indent=4)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pp.pprint(msg)
    
    text = msg['text']
    
    if text =='/ping':
        bot.sendMessage(chat_id,'pong!')
        
    elif text == '/yurui':
        bot.sendMessage(chat_id,'boom!')
        
    elif text == '/showdetail':
        bot.sendMessage(chat_id,msg)
        
    elif text == '/boom':
        response=msg['reply_to_message']['from']['first_name']+' boom!'
        bot.sendMessage(chat_id,response)


MessageLoop(bot, handle).run_as_thread()

While(1)
    time.sleep(10)

