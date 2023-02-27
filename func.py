import telebot
from telebot import types
import sqlite3

conn = sqlite3.connect('db/base.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("SELECT isn, num_app, username FROM test")
view = (cursor.fetchmany(5))
print(view)





# @bot.message_handler(commands=['start'])
# def mes(message):
#     cursor.execute('SELECT id, text FROM content WHERE id=3'),
#     viev = (cursor.fetchone()[1])
#     bot.send_message(message.chat.id, viev, parse_mode='html')


# bot.polling(none_stop=True, interval=0)


# import telebot
# from telebot import types

# TELEGRAM_TOKEN = '5798841213:AAFoLRcbeMrrmF4NpFhxX0B6zJU5s4U1ESQ'

# bot = telebot.TeleBot(TELEGRAM_TOKEN)

# @bot.message_handler (content_types =['text'])
# def bot_message(message):
#     if message.text == 'общежитие':
#         markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item1 = types.KeyboardButton('Привет')
#         item2 = types.KeyboardButton('МЕНЯ')
#         back = types.KeyboardButton('НАЗАД')
#         markup_1.add(item1, item2, back)
#         bot.send_message(message.chat.id,'Вот ваша ссылка:',reply_markup = markup_1)

#     if message.text == 'стипендии':
#         markup = types.InlineKeyboardMarkup(row_width=1)
#         item1 = types.InlineKeyboardButton('Cоц. стипендия',callback_data=0)
#         item2 = types.InlineKeyboardButton('Повыш. академ. стипендия',callback_data = 1)
#         item3 = types.InlineKeyboardButton('Повыш. соц. стипендия',callback_data = 2)
#         item4 = types.InlineKeyboardButton('Мат. поддержка',callback_data = 3)
#         back = types.InlineKeyboardButton('НАЗАД',callback_data = 4)
#         markup.add(item1, item2,item3,item4, back)
#         bot.send_message(message.chat.id,'СТИПЕНДИИ:',reply_markup = markup)


# bot.polling(none_stop=True, interval=0)