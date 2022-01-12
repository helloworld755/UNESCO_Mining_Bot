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
    item4 = telebot.types.KeyboardButton("💼 Компетенции")
    item5 = telebot.types.KeyboardButton("🎓 Образование")
    item6 = telebot.types.KeyboardButton("📓 Летние школы")
    item7 = telebot.types.KeyboardButton("🤝 Мероприятия")
    item8 = telebot.types.KeyboardButton("🎤 Лекторий")

    markup.add(item1, item2)
    markup.add(item3, item4)
    markup.add(item5, item6)
    markup.add(item7, item8)
    bot.send_message(m.chat.id,
                     'Здравствуйте!\nНа связи виртуальный консультант Центра ЮНЕСКО.\nВыберите интересующую вас '
                     'тему.\n\nℹ Вы можете сразу написать вопрос, и он будет переадресован в Центр.',
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
        answer = 'Раздел в разработке. Ожидайте новостей ⏳'
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '🏢 Недра':
        answer = '*Общественно-профессиональное сообщество вузов «Недра»* объединяет более 70 университетов, ' \
                 'чьи направления обучения связаны с подготовкой специалистов для минерально-сырьевого комплекса ' \
                 'России.\n\nВ основе коллаборации лежит необходимость объединения усилий высших учебных заведений для ' \
                 'создания внутри страны единого образовательного пространства, развития академической мобильности и ' \
                 'повышения за счёт этих механизмов качества российских выпускников.\n\nПодробная информация доступна ' \
                 'на сайте:\nnedra.spmi.ru\n\n*Контакты:*\nСолдатченко ' \
                 'Мария Владимировна\nКоординатор по работе Консорциума,\nНачальник управления Международного центра ' \
                 'компетенций в горнотехническом образовании под эгидой ЮНЕСКО\nnedra@spmi.ru\n+7 (812) 382-04-26 '
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '💼 Компетенции':
        answer = '*Профессиональная аккредитация* предполагает оценку компетенции специалиста в соответствии с ' \
                 'установленным стандартом, присвоение звания и регистрацию в реестре профессиональных инженеров. ' \
                 'Необходимым условием является вступления в ряды членов соответствующего профессионального ' \
                 'инженерного сообщества.\n\n*Профессиональное звание* является эталоном, с помощью которого ' \
                 'общественность, работодатели и их клиенты могут быть уверены в том, что зарегистрированные инженеры ' \
                 'и технические специалисты соответствуют всемирно признанным профессиональным стандартам.\n\nЗвание от ' \
                 'британского профильного совета присваивается в результате собеседования на английском языке и имеет ' \
                 'следующие степени:\n✅ От Британского инженерного совета *CEng* – инженер международного уровня\n✅ От ' \
                 'Британского научного совета *СSci* – ученый международного уровня\n✅ От Британского экологического ' \
                 'совета *CEnv* – эколог международного уровня\n\nПрисваиваемые профессиональные звания признаются более ' \
                 'чем в 120 странах мира.\n\nПодробнее о вступлении и правилах присвоения звания:\n' \
                 'namineng.com\n\n*Контакты:*\nЗырин Вячеслав Олегович\nИсполнительный ' \
                 'директор Национальной ассоциации горных инженеров,\nНачальник отдела Международного центра ' \
                 'компетенций в горнотехническом образовании под эгидой ЮНЕСКО\nnagi@spmi.ru\n+7 (812) 382-04-24 '
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '🎓 Образование':
        answer = 'Содействие российским университетам в подготовке научных кадров современного мирового уровня - ' \
                 'безусловный приоритет Консорциума "Недра". Одними из инструментов его достижения являются программы ' \
                 '*«двойной магистратуры»* и *«тройной магистратуры»*.\n\nПодробная информация доступна ' \
                 'на сайте:\nnedra.spmi.ru\n\n*Контакты:*\nСолдатченко ' \
                 'Мария Владимировна\nКоординатор по работе Консорциума,\nНачальник управления Международного центра ' \
                 'компетенций в горнотехническом образовании под эгидой ЮНЕСКО\nnedra@spmi.ru\n+7 (812) 382-04-26 '
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '📓 Летние школы':
        answer = 'Все краткосрочные образовательные программы (так называемые, *"летние школы"*), организуемые под ' \
                 'эгидой Центра, разработаны ведущими ' \
                 'преподавателями и специалистами, и получили высокую оценку международного экспертного сообщества. ' \
                 'Их тематика насыщена и разнообразна. Это не только традиционные для первого высшего технического ' \
                 'учебного заведения России направления обучения – горное, нефтегазовое, взрывное дело, переработка ' \
                 'полезных ископаемых, но также IT-технологии, геоэкология и даже гуманитарные науки.\n\nЛетние школы ' \
                 'включают лекционные и практические занятия, мастер-классы и тренинги, экскурсионные и культурные ' \
                 'мероприятия, выезды на действующие предприятия компаний-партнёров.\n\n27 программ летних школ Горного ' \
                 'университета прошли аккредитацию Международного центра компетенций под эгидой ЮНЕСКО и Британского ' \
                 'инженерного совета IOM3 – Института материалов, минералов и горного дела. Это одно из наиболее ' \
                 'авторитетных в мире профессиональных объединений инженеров, аттестация которого является ' \
                 'безусловным свидетельством высокого уровня специалиста, компании или проекта.\n\nПодробная информация ' \
                 'доступна на сайте:\nsumschool.spmi.ru\n\n*Контакты:*\nГрищенкова Екатерина Николаевна\nНачальник отдела ' \
                 'Международного центра компетенций в горнотехническом образовании под эгидой ЮНЕСКО\n' \
                 'summerschools@spmi.ru\n+7 (812) 328-86-68 '
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '🤝 Мероприятия':
        answer = 'Одним из направлений деятельности Центра является *проведение мероприятий*. Сюда входит проведение ' \
                 'крупных и общественно значимых международных мероприятий и диалогов, конференций, актовых лекций и ' \
                 'круглых столов с целью популяризации науки и горнотехнического образования, привлечения талантливой ' \
                 'молодежи, укрепления международного и регионального сотрудничества, совместной работы и координации ' \
                 'в области минерально-сырьевого комплекса.\n\nМероприятия 2022:\n🔸 XX Всероссийская конференция-конкурс ' \
                 'студентов и аспирантов «Актуальные проблемы недропользования» (апрель 2022)\n🔸 XVIII Международный ' \
                 'форум-конкурс студентов и молодых учёных «Актуальные проблемы недропользования» (май-июнь 2022)\n\n' \
                 'Подробнее об этих мероприятиях:\nvkk.spmi.ru\nmyouth.spmi.ru\n\n*Контакты*:\nКрылова Алёна Александровна ' \
                 '\nНачальник отдела Международного центра компетенций в горнотехническом образовании под эгидой ЮНЕСКО ' \
                 '\nforum-contest@spmi.ru\n+7 (812) 328-82-48 '
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    elif message.text.strip() == '🎤 Лекторий':
        answer = 'Раздел в разработке. Ожидайте новостей ⏳'
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")
    else:
        if message.text[0] == '$':
            mes = message.text.split('$')
            bot.send_message(chat_id=str(mes[1]), text=str(mes[2]))
        else:
            that_text = str(message.from_user.first_name) + ', ' + str(message.from_user.username) + ', ' + str(
                message.from_user.id) + ': ' + message.text
            bot.send_message(chat_id="417794071", text=that_text)
            answer = 'Спасибо, ваш вопрос передан в Центр ✅'
            bot.send_message(message.chat.id, answer, parse_mode="Markdown")


# Запускаем бота
bot.polling(none_stop=True, interval=0)
