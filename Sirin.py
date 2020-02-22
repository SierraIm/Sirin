import telepot
import pprint
bot = telepot.Bot('879508978:AAFr1ngABRI9vP2r2Jl9K58hlCwn4vPinAc')

res = bot.getUpdates()
print(pprint(res))