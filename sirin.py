#!/usr/lib/python3
# _*_ coding:utf-8 _*_
#sirin.py

import telegram
import time
from telegram.ext import Updater

tk = '879508978:AAFr1ngABRI9vP2r2Jl9K58hlCwn4vPinAc'

bot = telegram.Bot(token=tk)
updater = Updater(token=tk)

while(1):
    time.sleep(10)

