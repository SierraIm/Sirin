const TelegramBot = require('node-telegram-bot-api')
const token = '1139441431:AAGK1mff_XD1rRHqSNWsskRjMNWVmSFtH_w'
const bot = new TelegramBot(token,{pplling:true});

bot.onText(/\/echo(.+)/,(msg,match) =>{
	const chatId = msg.chat.id;
	const resp = match[1];
	bot.sendMessage(chatId,resp);
})

bot.on('message',(msg) => {
	const chatId = msg.chat.id;
	bot.sendMessage(chatId,'pong');
})
