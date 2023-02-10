import telebot
from telebot import types

bot = telebot.TeleBot('5798841213:AAFoLRcbeMrrmF4NpFhxX0B6zJU5s4U1ESQ')

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
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "история осиасу":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Узнать историю')
        markup.add(btn1)
        final_text = "«Народ, не знающий своего прошлого, не имеет будущего» М.Ломоносов "

    elif get_message_bot == "полезная информация":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Отправка заявок')
        btn2 = types.KeyboardButton('Перечни сбора документов')
        btn3 = types.KeyboardButton('Предметы обучения')
        btn4 = types.KeyboardButton('Учётные записи "Арсенал"')
        markup.add(btn1, btn2, btn3, btn4)
        final_text = "Выберите, какая информация необходима: "

    elif get_message_bot == "график":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Дежурства')
        btn2 = types.KeyboardButton('Отпуск')
        btn3 = types.KeyboardButton('Больничные')
        markup.add(btn1, btn2, btn3)
        final_text = "Выберите, какая информация необходима: "

    elif get_message_bot == "руководящие документы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('В разработке...')
        markup.add(btn1)
        final_text = "В разработке..."

    elif get_message_bot == "связаться с начальником":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('связь')
        markup.add(btn1)
        final_text = "связь"
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        final_text = "Выбери раздел меню, пожалуйста!"

    bot.send_message(message.chat.id, final_text, parse_mode='', reply_markup=markup)
#
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
