import telebot
from telebot import types

bot = telebot.TeleBot("5482533311:AAGqxDsilbepgsswuCqCbBginASmEGwSImg")


@bot.message_handler(commands=['start'])
def start (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sta = types.KeyboardButton("Вітаю вас.")
    sta2 = types.KeyboardButton("Поїхали !")
    markup.add(sta, sta2)
    bot.send_message(message.chat.id, text="Вітаю вас {0.first_name} {0.last_name} у чат-боті, котрий допоможе тобі вивчти основи QA, тебе чекають 25 питань для початківців".format(
        message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Вітаю вас."):
        bot.send_message(
            message.chat.id, "Вітаю, я дуже хочу допомогти тобі розібратись в всьому що стосуєтся QA, тож почнемо разом.")
    elif (message.text == "Поїхали !"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        ques1 = types.KeyboardButton("Перше")
        ques2 = types.KeyboardButton("Друге")
        ques3 = types.KeyboardButton("Третье")
        ques4 = types.KeyboardButton("Четверте")
        ques5 = types.KeyboardButton("П'яте")
        ques6 = types.KeyboardButton("Шосте")
        ques7 = types.KeyboardButton("Сьоме")
        ques8 = types.KeyboardButton("Восьме")
        ques9 = types.KeyboardButton("Дев'яте")
        ques10 = types.KeyboardButton("Десяте")
        ques11 = types.KeyboardButton("Одинадцяте")
        ques12 = types.KeyboardButton("Дванадцяте")
        ques13 = types.KeyboardButton("Тринадцяте")
        ques14 = types.KeyboardButton("Чотирнадцяте")
        ques15 = types.KeyboardButton("П'ятнадцяте")
        ques16 = types.KeyboardButton("Шістнадцяте")
        ques17 = types.KeyboardButton("Сімнадцяте")
        ques18 = types.KeyboardButton("Вісімнадцяте")
        ques19 = types.KeyboardButton("Дев'ятнадцяте")
        ques20 = types.KeyboardButton("Двадцяте")
        ques21 = types.KeyboardButton("Двадцять Перше")
        ques22 = types.KeyboardButton("Двадцять Друге")
        ques23 = types.KeyboardButton("Двадцять Третє")
        ques24 = types.KeyboardButton("Двадцать Четверте")
        ques25 = types.KeyboardButton("Двадцять П'яте")
        
        markup.add
        (ques1, ques2, ques3, ques4, ques5,
                   ques6, ques7, ques8, ques9, ques10,
                   ques11, ques12, ques13, ques14, ques15,
                   ques16, ques17, ques18, ques19, ques20,
                   ques21, ques22, ques23, ques24, ques25)
        bot.send_message(message.chat.id, text="Вибери одне з 25 запитань, та відповідай в бот, в текстовому форматі. Після цього обов'язково перевірь свою відповідь у відкритих джерелах. Успіху тобі.", reply_markup=markup)

    elif(message.text == "Перше"):
        bot.send_message(
            message.chat.id, "Що так тестування та нащо тестувати ПО ?")

    elif(message.text == "Друге"):
        bot.send_message(message.chat.id, "Які існують єтапи тестування ?")

    elif(message.text == "Третье"):
        bot.send_message(message.chat.id, "Які ви знаєте типи тестування ?")

    elif(message.text == "Четверте"):
        bot.send_message(message.chat.id, "Які ви знаєте рівні тестування ?")

    elif(message.text == "П'яте"):
        bot.send_message(
            message.chat.id, "Які техніки тест-дизайну ви знаєте ? ")

    elif(message.text == "Шосте"):
        bot.send_message(
            message.chat.id, "Розкажіть про техніку класів еквівалентності ? ")

    elif(message.text == "Сьоме"):
        bot.send_message(
            message.chat.id, "Що таке техніка аналізу граничних значень? У чому цінність цієї техніки ?")

    elif(message.text == "Восьме"):
        bot.send_message(
            message.chat.id, "Що таке Regression та Confirmation тестування, яка між ними різниця ?")

    elif(message.text == "Дев'яте"):
        bot.send_message(
            message.chat.id, "Як часто слід проводити регресійне тестування ?")

    elif(message.text == "Десяте"):
        bot.send_message(
            message.chat.id, "Які бувають види інтеграційного тестування ?")

    elif(message.text == "Одинадцяте"):
        bot.send_message(
            message.chat.id, "Що таке Configuration Testing ? ")

    elif(message.text == "Дванадцяте"):
        bot.send_message(
            message.chat.id, "Що таке Exploratory Testing ? ")

    elif(message.text == "Тринадцяте"):
        bot.send_message(message.chat.id, "Які існують стандарти UI ?")

    elif(message.text == "Чотирнадцяте"):
        bot.send_message(
            message.chat.id, "Що таке Black/Grey/White Box Testing ?")

    elif(message.text == "П'ятнадцяте"):
        bot.send_message(message.chat.id, "Що таке Performance Testing ?")

    elif(message.text == "Шістнадцяте"):
        bot.send_message(
            message.chat.id, "Що таке Smoke та Sanity тестування та яка між ними різниця ? ")

    elif(message.text == "Сімнадцяте"):
        bot.send_message(
            message.chat.id, "Що таке Traceability Matrix? ")

    elif(message.text == "Вісімнадцяте"):
        bot.send_message(
            message.chat.id, "Що таке Sanity Testing ?")

    elif(message.text == "Дев'ятнадцяте"):
        bot.send_message(message.chat.id, "Що таке End-to-End тест ?")

    elif(message.text == "Двадцяте"):
        bot.send_message(message.chat.id, "Що таке тестування безпеки ?")

    elif(message.text == "Двадцять Перше"):
        bot.send_message(
            message.chat.id, "Що таке випробування на основі ризиків ?")

    elif(message.text == "Двадцять Друге"):
        bot.send_message(
            message.chat.id, "Що таке динамічне тестування ? ")

    elif(message.text == "Дванадцять Третє"):
        bot.send_message(
            message.chat.id, "Що таке Bug, Error, Failure, Fault? ")

    elif(message.text == "Двадцять Четверте"):
        bot.send_message(
            message.chat.id, "Які атрибути баг-репорта? Які основні поля заповнення ? ")

    elif(message.text == "Дванадцять П'яте"):
        bot.send_message(
            message.chat.id, "Яка різниця між чеклістом та тест-кейсами ? ")
    else:
        pass


bot.polling(none_stop=True)
