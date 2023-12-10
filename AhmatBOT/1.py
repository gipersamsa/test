import telebot
from telebot import types

bot = telebot.TeleBot('6466021933:AAFY8tV1hKHATyCUAbUbGgzYGLUrQeAhlC8')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Помахать")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет , я Game_bot", reply_markup=markup)

@bot.message_handler(commands = ['showme'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Это ты', url='https://upload.wikimedia.org/wikipedia/commons/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Покажи меня", reply_markup = markup)

@bot.message_handler(commands=['showme2'])
def show_me(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Фото 1', callback_data='photo_1')
    btn2 = types.InlineKeyboardButton(text='Фото 2', callback_data='photo_2')
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Выберите фото для просмотра:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('photo_'))
def send_photo(call):
    chat_id = call.message.chat.id

    if call.data == 'photo_1':
        bot.send_photo(chat_id, photo=open('Ob1.jpg', 'rb'))
    elif call.data == 'photo_2':
        bot.send_photo(chat_id, photo=open('Ob2.png', 'rb'))



@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Помахать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Как стать автором на Хабре?')
        btn2 = types.KeyboardButton('Правила сайта')
        btn3 = types.KeyboardButton('Советы по оформлению публикации')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Как стать автором на Хабре?':
        bot.send_message(message.from_user.id, 'Вы пишете первый пост, его проверяют модераторы, и, если всё хорошо, отправляют в основную ленту Хабра, где он набирает просмотры, комментарии и рейтинг. В дальнейшем премодерация уже не понадобится. Если с постом что-то не так, вас попросят его доработать.\n \nПолный текст можно прочитать по ' + '[ссылке](https://habr.com/ru/sandbox/start/)', parse_mode='Markdown')

    elif message.text == 'Правила сайта':
        bot.send_message(message.from_user.id, 'Прочитать правила сайта вы можете по ' + '[ссылке](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')

    elif message.text == 'Советы по оформлению публикации':
        bot.send_message(message.from_user.id, 'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](https://habr.com/ru/docs/companies/design/)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
