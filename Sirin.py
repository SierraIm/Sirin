# coding=utf-8

import telepot
import time
import pprint
from telepot.loop import MessageLoop

bot = telepot.Bot('879508978:AAFr1ngABRI9vP2r2Jl9K58hlCwn4vPinAc')

pp = pprint.PrettyPrinter(indent=4)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pp.pprint(msg,/n)
    
    if msg['text']=='/ping':
        bot.sendMessage(chat_id,'boom!')
        
    if msg['text']=='/yurui':
        bot.sendMessage(chat_id,'boom!')
        
    if msg['text']=='/showdetail':
        bot.sendMessage(chat_id,msg)
        
    if msg['text']=='/boom':
        response=msg['reply_to_message']['from']['first_name']+msg['reply_to_message']['from']['last_name']+' boom!'
        bot.sendMessage(chat_id,response)


MessageLoop(bot, handle).run_as_thread()

while(1):
    time.sleep(10)

