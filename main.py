import telebot
from telebot import types
import sqlite3

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()

bot = telebot.TeleBot('5798841213:AAFoLRcbeMrrmF4NpFhxX0B6zJU5s4U1ESQ')

def db_table_val(isn1: str):
    cursor.execute('INSERT INTO test (isn) VALUES (?)', (isn1,))
    conn.commit()


text1 = "«Народ, не знающий своего прошлого, не имеет будущего» М.Ломоносов "
text2 = "Выбери, какая информация необходима: "
text3 = "Выбери раздел меню, пожалуйста"
# text4 =
# text5 =
isn2 = ' '

def gisn(message):
    global isn2
    isn2 = f'{message.chat.username}'
    bot.send_message(message.chat.id, "Well done!")




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('История ОСиАСУ')
    btn2 = types.KeyboardButton('Полезная информация')
    btn3 = types.KeyboardButton('График')
    btn4 = types.KeyboardButton('Руководящие документы')
    btn5 = types.KeyboardButton('Связаться с начальником')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mes(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "история осиасу":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Узнать историю')
        btn2 = types.KeyboardButton('В главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text1, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "узнать историю":
        bot.send_message(message.chat.id, "жили-были...", parse_mode='html')

    elif get_message_bot == "полезная информация":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Отправка заявок')
        btn2 = types.KeyboardButton('Перечни сбора документов')
        btn3 = types.KeyboardButton('Предметы обучения')
        btn4 = types.KeyboardButton('Учётные записи "Арсенал"')
        btn5 = types.KeyboardButton('В главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text2, parse_mode='html', reply_markup=markup)


    elif get_message_bot == "отправка заявок":
        bot.send_message(message.chat.id, "Введите ИСН оборудования", parse_mode='html')
        gisn(message)
        db_table_val(isn1 = isn2)



    elif get_message_bot == "график":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Дежурства')
        btn2 = types.KeyboardButton('Отпуск')
        btn3 = types.KeyboardButton('Больничные')
        btn4 = types.KeyboardButton('В главное меню')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text2, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "руководящие документы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('В разработке...')
        btn2 = types.KeyboardButton('В главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "В разработке...", parse_mode='html', reply_markup=markup)

    elif get_message_bot == "связаться с начальником":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Постучать к нему в телегу", url="https://t.me/pa1i4"))
        bot.send_message(message.chat.id, "Павлов Артем Юрьевич", reply_markup=markup)

    elif get_message_bot == "в главное меню":
        start(message)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        bot.send_message(message.chat.id, text3, parse_mode='html', reply_markup=markup)



#
# #
#
#
#
# # @bot.message_handler(content_types=['text'])
# # def mess(message):
# #     get_message_bot = message.text.strip().lower()
# #
# #     if get_message_bot == "история осиасу":
# #         bot.send_message (message.chat.id, "Однажды в далёкой, далёкой галактике...", parse_mode='html')
#
#
#
#
# # @bot.message_handler()
# # def get_user_text(message):
# #     if message.text == "Hello":
# #         bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
# #     elif message.text == "id":
# #         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
# #     else:
# #         bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')
#
#
# # @bot.message_handler(commands=['website'])
# # def website(message):
# #     markup = types.InlineKeyboardMarkup()
# #     markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://dzen.ru"))
# #     bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)
# #
# # @bot.message_handler(commands=['help'])
# # def help(message):
# #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
# #     website = types.KeyboardButton('/website')
# #     start = types.KeyboardButton('/start')
# #
# #     markup.add(website, start)
# #
# #     bot.send_message(message.chat.id, 'Что будешь делать?', reply_markup=markup)
#
#     # markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://dzen.ru"))
#     # bot.send_message(message.chat.id, "Good", reply_markup=markup)
#
#
#
bot.polling(none_stop=True, interval=0)
