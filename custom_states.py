import telebot # telebot
import sqlite3
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup #States

# Хранение состояний
from telebot.storage import StateMemoryStorage


# Начиная с версии 4.4.0+ мы поддерживаем хранилища.
# StateRedisStorage -> Хранилище на основе Redis.
# StatePickleStorage -> Хранилище на основе Pickle.
# Для Redis вам необходимо установить Redis.
# Передать хост, базу данных, пароль или что-то еще,
# если вам нужно изменить конфиг для redis.
# Для Pickle требуется путь. Путь по умолчанию находится в папке .state-saves.
# Если вы использовали более старую версию pytba для рассола,
# вам нужно перейти со старого pickle на новый с помощью
# StatePickleStorage().convert_old_to_new()



# Теперь вы можете передать хранилище боту.
state_storage = StateMemoryStorage() # здесь можно инициализировать другое хранилище
conn = sqlite3.connect('db/base.db', check_same_thread=False)
cursor = conn.cursor()


bot = telebot.TeleBot('5855602296:AAH3Opri00m9o1TZ9aMZ6OrfzLhqXznENwc')


class MyStates(StatesGroup):
    isn = State()
    num_app = State()

def add_data(isn1: str, app1: str, username: str):
    cursor.execute('INSERT INTO test (isn, num_app, username) VALUES (?,?,?)', (isn1, app1, username,))
    conn.commit()




@bot.message_handler(commands=['add'])
def start_ex(message):
    """
    Стартовая команда. Здесь мы находимся в начальном состоянии
    """
    bot.set_state(message.from_user.id, MyStates.isn, message.chat.id)
    bot.send_message(message.chat.id, 'Введите ИСН')
 

# Any state
@bot.message_handler(state="*", commands=['cancel'])
def any_state(message):
    """
    Состояние отмены
    """
    bot.send_message(message.chat.id, "Ваше состояние было отменено.")
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=MyStates.isn)
def name_get(message):
    """
    State 1. Будет обрабатываться, когда состояние пользователя MyStates.name.
    """
    bot.send_message(message.chat.id, 'Введи номер заявки')
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
    

    # bot.delete_state(message.from_user.id, message.chat.id)

#incorrect number
# @bot.message_handler(state=MyStates.age, is_digit=False)
# def age_incorrect(message):
#     """
#     Неправильный ответ для MyStates.age
#     """
#     bot.send_message(message.chat.id, 'Похоже, вы отправляете строку в поле age. Пожалуйста, введите номер')

# register filters

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling(skip_pending=True)