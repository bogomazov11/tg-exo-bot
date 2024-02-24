import telebot 
token = '6792331573:AAF9q4_lXwzorboMwF9s6B8TbDthQAZ-tZI' # Токен указан, чтобы бот работал в телеграмме
bot= telebot.TeleBot(token) # Здесь указываем боту на его токен

@bot.message_handler(commands=['start']) # Действие бота при комманде /start
def start_message(m, res=False):
    bot.send_message(m.chat.id, 'Приветствую, напишите мне что-нибудь')

@bot.message_handler(commands=['help']) # Действие при комманде /help
def start_message(m, res=False):
    bot.send_message(m.chat.id, 'Просто напишите какой-нибудь текст')

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Хватит повторять' or message.text == 'хватит повторять':
        bot.send_message(message.chat.id, 'ну ладно((')
    elif message.text == 'Перестань' or message.text == 'перестань':
        bot.send_message(message.chat.id, 'Не могу')
    else:
        bot.send_message(message.chat.id, 'Мне показалось? Или ' + message.text)

bot.polling(none_stop=True, interval=0)