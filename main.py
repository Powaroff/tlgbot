import telebot
from telebot import types
import sqlite3
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage

state_storage = StateMemoryStorage()
conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()

bot = telebot.TeleBot()

class MyStates(StatesGroup):
    isn = State()
    num_app = State()


def add_data(isn1: str, app1: str, username: str):
    cursor.execute('INSERT INTO test (isn, num_app, username) VALUES (?,?,?)',
    (isn1, app1, username,))
    conn.commit()



text1 = "«Народ, не знающий своего прошлого, не имеет будущего» М.Ломоносов "
text2 = "Выбери, какая информация необходима: "
text3 = "Выбери раздел меню, пожалуйста"
# text4 =
# text5 =



@bot.message_handler(commands=['add'])
def start_ex(message):
    """
    Стартовая команда. Здесь мы находимся в начальном состоянии
    """
    bot.set_state(message.from_user.id, MyStates.isn, message.chat.id)
    bot.send_message(message.chat.id, 'Введите ИСН:')


@bot.message_handler(state="*", commands=['exit'])
def any_state(message):
    """
    Состояние отмены
    """
    bot.send_message(message.chat.id, "Работа с заявками завершена.")
    bot.delete_state(message.from_user.id, message.chat.id)
    start(message)


@bot.message_handler(state=MyStates.isn)
def name_get(message):
    """
    State 1. Будет обрабатываться, когда состояние пользователя MyStates.name.
    """
    bot.send_message(message.chat.id, 'Введите номер заявки:')
    bot.set_state(message.from_user.id, MyStates.num_app, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['isn'] = message.text

@bot.message_handler(state=MyStates.num_app)
def ready_for_answer(message):
    """
    State 2. Будет обрабатываться, когда состояние пользователя MyStates.age.
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        isn1 = data['isn']
        app1 = message.text
        username = message.from_user.username
        
        
        add_data(isn1, app1, username)

        bot.send_message(message.chat.id, "Готово! Заявка учтена.")
        bot.send_message(message.chat.id, "Для завершения работы с заявками нажмие: /exit\nДля регистрации следующей заявки нажми: /add")
        





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
        bot.send_message(message.chat.id, "Позвоните на номер 999 и нажмите: /add", parse_mode='html')




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

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.polling(none_stop=True, interval=0)
