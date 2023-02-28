import telebot
from telebot import types
import sqlite3
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage

state_storage = StateMemoryStorage()
conn = sqlite3.connect('db/base.db', check_same_thread=False)
cursor = conn.cursor()

bot = telebot.TeleBot('5798841213:AAFoLRcbeMrrmF4NpFhxX0B6zJU5s4U1ESQ')

class MyStates(StatesGroup):
    isn = State()
    num_app = State()
    t_isn = State()
    t_n_a = State()
    t_un = State()
    t_isn1 = State()
    t_n_a1 = State()
    t_un1 = State()
    t_isn2 = State()
    t_n_a2 = State()
    t_un2 = State()

def add_data(isn1: str, app1: str, username: str):
    cursor.execute('INSERT INTO test (isn, num_app, username) VALUES (?,?,?)',
    (isn1, app1, username,))
    conn.commit()


text1 = "«Народ, не знающий своего прошлого, не имеет будущего» М.Ломоносов."
text2 = "Выберите, какая информация необходима: "
text3 = "Выберите раздел меню, пожалуйста."
text4 = "Здесь могли бы быть ответы на КЗ."
text5 = "<b><u>Последние заявки в базе данных:</u></b>\n" + "<u>|ИСН| Номер заявки| Автор заявки|</u>\n"


@bot.message_handler(commands=['sed'])
def sed(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    btn1 = types.KeyboardButton('014а')
    btn2 = types.KeyboardButton('102б')
    btn3 = types.KeyboardButton('118')
    btn4 = types.KeyboardButton('119')
    btn5 = types.KeyboardButton('220')
    btn6 = types.KeyboardButton('226')
    btn7 = types.KeyboardButton('224')
    btn8 = types.KeyboardButton('208')
    btn9 = types.KeyboardButton('212')
    btn10 = types.KeyboardButton('301а')
    btn11 = types.KeyboardButton('301б')
    btn12 = types.KeyboardButton('301в')
    btn13 = types.KeyboardButton('305')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
    bot.send_message(message.chat.id, 'Эта функция поможет узнать адрес рабочего места СЭД.\n'
    'Выберите или введите номер помещения, чтобы продолжить:', parse_mode='html', reply_markup=markup)



@bot.message_handler(commands=['add'])
def start_ex(message):
    bot.set_state(message.from_user.id, MyStates.isn, message.chat.id)
    bot.send_message(message.chat.id, 'Вы находитесь в разделе регистрации заявки в Воентелеком.\n'
    'Для отмены нажмите: /exit\nДля продлжения введите <u><b>ИСН</b> изделия</u>:', parse_mode='html')


@bot.message_handler(state="*", commands=['exit'])
def any_state(message):
    bot.send_message(message.chat.id, "Работа с заявками завершена.")
    bot.delete_state(message.from_user.id, message.chat.id)
    start(message)


@bot.message_handler(state=MyStates.isn)
def name_get(message):
    bot.send_message(message.chat.id, 'Введите номер заявки:')
    bot.set_state(message.from_user.id, MyStates.num_app, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['isn'] = message.text

@bot.message_handler(state=MyStates.num_app)
def ready_for_answer(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        isn1 = data['isn']
        app1 = message.text
        username = message.from_user.username
        
        
        add_data(isn1, app1, username)

        bot.send_message(message.chat.id, "Готово! Заявка учтена.")
        bot.send_message(message.chat.id, "Для регистрации следующей заявки нажмите: /add\n"
        "Для корректного завершения работы с заявками нажмите: /exit\n")
        

@bot.message_handler(commands=['view'])
def view(message):
    cursor.execute('SELECT isn FROM test ORDER BY id DESC LIMIT 2, 1')
    MyStates.t_isn = (cursor.fetchone())
    cursor.execute('SELECT num_app FROM test ORDER BY id DESC LIMIT 2, 1')
    MyStates.t_n_a = (cursor.fetchone())
    cursor.execute('SELECT username FROM test ORDER BY id DESC LIMIT 2, 1')
    MyStates.t_un = (cursor.fetchone())
    cursor.execute('SELECT isn FROM test ORDER BY id DESC LIMIT 1, 1')
    MyStates.t_isn1 = (cursor.fetchone())
    cursor.execute('SELECT num_app FROM test ORDER BY id DESC LIMIT 1, 1')
    MyStates.t_n_a1 = (cursor.fetchone())
    cursor.execute('SELECT username FROM test ORDER BY id DESC LIMIT 1, 1')
    MyStates.t_un1 = (cursor.fetchone())
    cursor.execute('SELECT isn FROM test ORDER BY id DESC')
    MyStates.t_isn2 = (cursor.fetchone())
    cursor.execute('SELECT num_app FROM test ORDER BY id DESC')
    MyStates.t_n_a2 = (cursor.fetchone())
    cursor.execute('SELECT username FROM test ORDER BY id DESC')
    MyStates.t_un2 = (cursor.fetchone())
    view = MyStates.t_isn + MyStates.t_n_a + MyStates.t_un
    view1 = MyStates.t_isn1 + MyStates.t_n_a1 + MyStates.t_un1
    view2 = MyStates.t_isn2 + MyStates.t_n_a2 + MyStates.t_un2
    tab = text5 + str(view) + '\n' + str(view1) + '\n' +  str(view2)
    bot.send_message(message.chat.id, tab, parse_mode='html')



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('История и задачи')
    btn2 = types.KeyboardButton('Руководящие документы')
    btn3 = types.KeyboardButton('Канал')
    btn4 = types.KeyboardButton('Связь с начальником')
    btn5 = types.KeyboardButton('Основной раздел')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mes(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "история и задачи":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Узнать историю')
        btn2 = types.KeyboardButton('Узнать задачи ОСиАСУ')
        btn3 = types.KeyboardButton('В главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text1, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "узнать историю":
        cursor.execute('SELECT id, text FROM content WHERE id=11'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')

    elif get_message_bot == "узнать задачи осиасу":
        cursor.execute('SELECT id, text FROM content WHERE id=12'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')

    elif get_message_bot == "основной раздел":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Регистрация заявок')
        btn2 = types.KeyboardButton('Перечни сбора документов')
        btn3 = types.KeyboardButton('Учебный период')
        btn4 = types.KeyboardButton('Учётные записи "Арсенал"')
        btn5 = types.KeyboardButton('В главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text2, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "учебный период":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Контрольные занятия')
        btn2 = types.KeyboardButton('Зачет на старшего машины')
        btn3 = types.KeyboardButton('БГ')
        btn4 = types.KeyboardButton('Ведомость актуализации ИРС')
        btn5 = types.KeyboardButton('Основной раздел')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text2, parse_mode='html', reply_markup=markup)


    elif get_message_bot == "контрольные занятия":
        bot.send_message(message.chat.id, text4, parse_mode='html')


    elif get_message_bot == "ведомость актуализации ирс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Февраль')
        btn2 = types.KeyboardButton('Март')
        btn3 = types.KeyboardButton('Основной раздел')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text2, parse_mode='html', reply_markup=markup)


    elif get_message_bot == "февраль":
        cursor.execute('SELECT id, text FROM content WHERE id=13'),
        view = (cursor.fetchone()[1])
        bot.send_photo(message.chat.id, view, parse_mode='html')
        cursor.execute('SELECT id, text FROM content WHERE id=14'),
        view = (cursor.fetchone()[1])
        bot.send_photo(message.chat.id, view, parse_mode='html')
        cursor.execute('SELECT id, text FROM content WHERE id=15'),
        view = (cursor.fetchone()[1])
        bot.send_photo(message.chat.id, view, parse_mode='html')


    elif get_message_bot == "март":
        cursor.execute('SELECT id, text FROM content WHERE id=16'),
        view = (cursor.fetchone()[1])
        bot.send_photo(message.chat.id, view, parse_mode='html')
        cursor.execute('SELECT id, text FROM content WHERE id=17'),
        view = (cursor.fetchone()[1])
        bot.send_photo(message.chat.id, view, parse_mode='html')
        cursor.execute('SELECT id, text FROM content WHERE id=18'),
        view = (cursor.fetchone()[1])
        bot.send_photo(message.chat.id, view, parse_mode='html')


    elif get_message_bot == "зачет на старшего машины":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Назначается')
        btn2 = types.KeyboardButton('Изымается')
        btn3 = types.KeyboardButton('Обязан')
        btn4 = types.KeyboardButton('Запрещается')
        btn5 = types.KeyboardButton('Основной раздел')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text2, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "назначается":
        cursor.execute('SELECT id, text FROM content WHERE id=4'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')

    elif get_message_bot == "изымается":
        cursor.execute('SELECT id, text FROM content WHERE id=3'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')


    elif get_message_bot == "обязан":
        cursor.execute('SELECT id, text FROM content WHERE id=2'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')


    elif get_message_bot == "запрещается":
        cursor.execute('SELECT id, text FROM content WHERE id=1'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')


    elif get_message_bot == "бг":
        cursor.execute('SELECT id, text FROM content WHERE id=6'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')
        cursor.execute('SELECT id, text FROM content WHERE id=5'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')
        cursor.execute('SELECT id, text FROM content WHERE id=7'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')


    elif get_message_bot == "регистрация заявок":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Заявка в Воентелеком')
        btn2 = types.KeyboardButton('Заявка в ИВК (СЭД, Гарант, САООГ)')
        btn3 = types.KeyboardButton('Заявка в ГВЦ (ЗССПД, ИРС)')
        btn4 = types.KeyboardButton('Основной раздел')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text2, parse_mode='html', reply_markup=markup)
        

    elif get_message_bot == "заявка в воентелеком":
        bot.send_message(message.chat.id, "Узнайте <b>ИСН изделия</b> и позвоните по номеру: +7(495)609-50-05.\n"
        "Для учета заявки в базе нажмите: <b>/add</b>\n"
        "Для просмотра трех крайних заявок: <b>/view</b>", parse_mode='html')

    elif get_message_bot == "заявка в ивк (сэд, гарант, саоог)":
        bot.send_message(message.chat.id, "<b>Проблемы с СЭД:</b> Узнайте IP-адрес АРМ и позвоните по номеру:"
        "+7(495) 696-69-72, +7(495) 696-67-49, (10100) 91-18.\n"
        "(Чтобы узнать IP-адрес рабочего места СЭД нажмите: <b>/sed</b>)\n"
        "<b>Проблемы с ГАРАНТ:</b> Позвоните по номеру: +7(495) 647-62-38.\n"
        "<b>Проблемы с САООГ:</b> Позвоните по номеру: +7(800) 250-55-49.", parse_mode='html')

    elif get_message_bot == "заявка в гвц (зсспд, ирс)":
        bot.send_message(message.chat.id, "Для регистрации <b>обращений</b>, связанных с системами <b>ЗССПД</b> и <b>ИРС</b>,"
        " позвоните по номеру: (10100) 73-90, (10100) 97-86.", parse_mode='html')

    elif get_message_bot == 'учётные записи "арсенал"':
        bot.send_message(message.chat.id, "<u>Павлов:</u> <b>a01065</b>\n<u>Иванов:</u> <b>a01060</b>\n"
        "<u>Материкин</u>: <b>a01057</b>\n<u>Половинкин</u>: <b>a01064</b>\n<u>Демьяненко</u>: <b>a01063</b>\n"
        "<u>Кондратенко</u>: <b>a01066</b>\n<u>Николаев</u>: <b>a01062</b>\n<u>Поваров</u>: <b>a01061</b>", parse_mode='html')

    elif get_message_bot == "перечни сбора документов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Прописка при части')
        btn2 = types.KeyboardButton('Очередь на жилье')
        btn3 = types.KeyboardButton('Компенсация за поднаем')
        btn4 = types.KeyboardButton('Основной раздел')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text2, parse_mode='html', reply_markup=markup)


    elif get_message_bot == "очередь на жилье":
        cursor.execute('SELECT id, text FROM content WHERE id=8'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Читать полностью", url="https://base.garant.ru/12179855/"))
        bot.send_message(message.chat.id, 'Пр. МО РФ №1280 "О предоставлении...жилых помещений..."', reply_markup=markup)


    elif get_message_bot == "прописка при части":
        cursor.execute('SELECT id, text FROM content WHERE id=9'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Читать полностью", url="https://base.garant.ru/12157407/"))
        bot.send_message(message.chat.id, 'Пр. ФМС №288 "...по регистрационному учету граждан РФ..."', reply_markup=markup)


    elif get_message_bot == "компенсация за поднаем":
        cursor.execute('SELECT id, text FROM content WHERE id=10'),
        view = (cursor.fetchone()[1])
        bot.send_message(message.chat.id, view, parse_mode='html')



    elif get_message_bot == "руководящие документы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('ФЗ "О статусе военнослужащих"')
        btn2 = types.KeyboardButton('Пр. МО РФ №686 "Об установлении...компенсации за наем (поднаем)..."')
        btn3 = types.KeyboardButton('НФП-2009>Приложение "Таблица начисления баллов...по физической подготовке"')
        btn4 = types.KeyboardButton('В главное меню')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text2, reply_markup=markup)


    elif get_message_bot == 'фз "о статусе военнослужащих"':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Читать полностью", url="https://base.garant.ru/178792"))
        bot.send_message(message.chat.id, 'Открыть на ГАРАНТе', reply_markup=markup)

    elif get_message_bot == 'пр. мо рф №686 "об установлении...компенсации за наем (поднаем)..."':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Читать полностью", url="http://ivo.garant.ru/#/document/406003433/paragraph/1/doclist/1722/showentries/0/highlight/686%20%D0%BC%D0%BE%20%D1%80%D1%84:2"))
        bot.send_message(message.chat.id, 'Открыть на ГАРАНТе', reply_markup=markup)

    elif get_message_bot == 'нфп-2009>приложение "таблица начисления баллов...по физической подготовке"':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Читать полностью", url="https://base.garant.ru/195845/0bf34b9862b173b3ac6fa5142cdafa87/"))
        bot.send_message(message.chat.id, 'Открыть на ГАРАНТе', reply_markup=markup)


    elif get_message_bot == "канал":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылка на канал", url="https://t.me/osiasu_channel"))
        bot.send_message(message.chat.id, 'Этот канал уведомит вас об изменениях в графике работы, '
        'напомнит представить форму №7 по пятницам и даже поздравит с днем рождения.', reply_markup=markup)


    elif get_message_bot == "связь с начальником":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Постучать к нему в телегу", url="https://t.me/pa1i4"))
        bot.send_message(message.chat.id, "Павлов Артем Юрьевич", reply_markup=markup)

    elif get_message_bot == "в главное меню":
        start(message)

    elif get_message_bot == "014а":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$a</b>\nIP-адрес: 10.17.100.150", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "102б":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$2</b>\nIP-адрес: 10.17.100.2", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "118":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$J</b>\nIP-адрес: 10.17.100.190", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "119":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$w</b>\nIP-адрес: 10.17.100.176", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "220":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$b</b>\nIP-адрес: 10.17.100.110", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "226":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$G</b>\nIP-адрес: 10.17.100.171", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "224":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$3</b>\nIP-адрес: 10.17.100.3", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "208":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$5</b>\nIP-адрес: 10.17.100.142", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "212":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$H</b>\nIP-адрес: 10.17.100.140", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "301а":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$c</b>\nIP-адрес: 10.17.100.111", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "301б":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$F</b>\nIP-адрес: 10.17.100.70", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "301в":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$4</b>\nIP-адрес: 10.17.100.4", parse_mode='html')
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$W</b>\nIP-адрес: 10.17.100.175", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')

    elif get_message_bot == "305":
        bot.send_message(message.chat.id, "Логический модуль: <b>ОЮ$1</b>\nIP-адрес: 10.17.100.1", parse_mode='html')
        bot.send_message(message.chat.id, "Для выхода в главное меню нажиме: /start", parse_mode='html')



bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.polling(none_stop=True, interval=0)
