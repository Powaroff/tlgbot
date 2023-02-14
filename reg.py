def get_name(message): #получаем имя
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname) #следующий шаг – функция get_surname

def get_surname(message): #получаем фамилию
    global city
    name = message.text
    bot.send_message(message.from_user.id, 'Из какого ты города?')
    bot.register_next_step_handler(message, get_city)

def get_city(message): #получаем город
    global city
    city = message.text
    bot.send_message(message.from_user.id,'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message): #получаем возраст
    global age
    try:
        age = int(message.text) #проверяем, что возраст введен корректно
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_age)
        
