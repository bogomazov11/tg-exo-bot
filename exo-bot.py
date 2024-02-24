import telebot 
token = '6792331573:AAF9q4_lXwzorboMwF9s6B8TbDthQAZ-tZI'
bot= telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(m, res=False):
    bot.send_message(m.chat.id, 'Приветствую, напишите мне что-нибудь')

@bot.message_handler(content_types='text')
def message_reply(message):
    bot.send_message(message.chat.id, 'По-моему, ' + message.text)

bot.polling(none_stop=True, interval=0)
