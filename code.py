import telebot

# Создаем бота
bot = telebot.TeleBot('5003885450:AAGF_z-v9F6Wc2NZGCXrOwvhk-_MEqwPo5U')

# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("🌐 О Центре")
    item2 = telebot.types.KeyboardButton("🏛 Отделения")
    item3 = telebot.types.KeyboardButton("🏢 Недра")
    item4 = telebot.types.KeyboardButton("🤝 Мероприятия")
    item5 = telebot.types.KeyboardButton("🎓 Образование")
    item6 = telebot.types.KeyboardButton("🎤 Лекторий")
    item7 = telebot.types.KeyboardButton("💼 Компетенции")

    markup.add(item1)
    markup.add(item2, item3)
    markup.add(item4, item5)
    markup.add(item6, item7)
    bot.send_message(m.chat.id,
                     'Здравствуйте!\nНа связи виртуальный консультант Центра ЮНЕСКО.\nВыберите интересующую вас '
                     'тему.\n\nВы можете сразу написать вопрос, и он будет переадресован в Центр.',
                     reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == '🌐 О Центре':
        answer = '*Центр компетенций под эгидой ЮНЕСКО* стремится к продвижению принципов устойчивого развития ' \
                 'применительно к минерально-сырьевому сектору экономики в поддержку глобальных приоритетов ' \
                 'ЮНЕСКО на национальном и межгосударственном уровне.\n\n' \
                 'В числе *целей и задач* Центра:\n✅ внесение вклада в разработку политики в области ' \
                 'горнотехнического образования на государственном и межгосударственном ' \
                 'уровнях;\n✅ содействие разработке идей и инноваций, а также глобальному диалогу ' \
                 'между государствами и университетами в области естественных наук и технического ' \
                 'образования;\n✅ работа над созданием единой системы международной профессиональной ' \
                 'сертификации инженерного персонала;\n✅ создание благоприятных условий для глобальной ' \
                 'мобильности студентов и аспирантов, преподавателей и ученых.\n\n' \
                 '*Контакты*:\nАдрес: Российская Федерация, 199106, г. Санкт-Петербург, 21-я линия В.О., д. 2\n' \
                 'Телефон: +7 (812) 382-04-22\nE-mail: unesco@spmi.ru\nСайт: spmi.ru'
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '🏛 Отделения':
        answer = 'Список отделений'
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '🏢 Недра':
        answer = 'Консорциум Недра'
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '🤝 Мероприятия':
        answer = 'Мероприятия'
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '🎓 Образование':
        answer = 'Образование'
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '🎤 Лекторий':
        answer = 'Лекторий'
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '💼 Компетенции':
        answer = 'Компетенции'
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    else:
        if message.text[0] == '$':
            mes = message.text.split('$')
            bot.send_message(chat_id=str(mes[1]), text=str(mes[2]))
        else:
            that_text = str(message.from_user.first_name) + ', ' + str(message.from_user.username) + ', ' + str(message.from_user.id) + ': ' + message.text
            bot.send_message(chat_id="417794071", text=that_text)
            answer = 'Спасибо, ваш вопрос передан в Центр ✅'
            bot.send_message(message.chat.id, answer, parse_mode="Markdown")

# Запускаем бота
bot.polling(none_stop=True, interval=0)
