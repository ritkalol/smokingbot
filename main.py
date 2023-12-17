import telebot
import stuff
import random
import sqlite3 as sql
from my_utils import *
from telebot import types
from datetime import datetime
import schedule
import threading
import time

print("[INFO] Bot started")

with open("tokfile", 'r') as tf:
    token = tf.readlines()[0].replace('\n', '')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, stuff.start_prompt)


@bot.message_handler(commands=['start_challenge'])
def start_challenge_message(message):
    bot.send_message(
        message.chat.id, "Мы начали челлендж!")
    con = sql.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS 'test' (id INTEGER)")
        con.commit()


@bot.message_handler(commands=['stop_challenge'])
def start_reset_timer(message):
    bot.send_message(
        message.chat.id, "Мы закончили челлендж :/")
    delete_user(message.chat.id)

@bot.message_handler(commands=['books'])
def start_books(message):
    bot.send_message(
            message.chat.id, "Предлагаем почитать Вам следующую книгу:")
    book_0 = 'Р. Дальке, М. Дальке. Психология курения'
    book_1 = 'У.М. Эрасалиев. О вреде курения'
    book_2 = 'В. Уланов. Вред курения'
    book_3 = 'Лев Кругляк. Свобода от зависимости. Что семья должна знать о наркотиках, азартных играх и виртуальной реальности'
    book_4 = 'Аллен Карр. Как помочь нашим детям бросить курить'
    book_5 = 'Келли Макгонигал. Сила воли. Как развить и укрепить'
    mass_books = [book_0, book_1, book_2, book_3, book_4, book_5]
    bot.send_message(
            message.chat.id, mass_books[random.randint(0,len(mass_books)-1)])

@bot.message_handler(commands=['video'])
def video_message(message):
    video_0 = 'https://www.youtube.com/watch?v=PBR-Yev5vO8&t=58s'
    video_1 = 'https://www.youtube.com/watch?v=MG52aw2hoWI'
    video_2 = 'https://www.youtube.com/watch?v=Y5KvDrWX3ls'
    video_3 = 'https://www.youtube.com/watch?v=lOx4HgqchUw'
    video_4 = 'https://www.youtube.com/watch?v=Qt_0JwpuSkU'
    video_5 = 'https://www.youtube.com/watch?v=2xDGW8_xCB80'
    video_6 = 'https://youtu.be/VooEzH8ShJg?si=6vIFYPhqcJdzQ63R'
    video_7 = 'https://www.youtube.com/watch?v=eqlOXjOUcGI'
    video_8 = 'https://www.youtube.com/watch?v=3CPrJmZahJE'
    video_9 = 'https://www.youtube.com/watch?v=YfZ6BanNDek'
    mass_videos = [video_0, video_1, video_2, video_3,
                   video_4, video_5, video_6, video_7, video_8, video_9]
    bot.send_message(
        message.chat.id, "Предоставляем вам видео")
    bot.send_message(
        message.chat.id, mass_videos[random.randint(0, len(mass_videos)-1)])


@bot.message_handler(commands=['want_smoke'])
def want_smoke_message(message):
    bot.send_message(
        message.chat.id, "Не кури, брат")


@bot.message_handler(commands=['reset_timer'])
def start_reset_timer(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, )
    btn4 = types.KeyboardButton("Да,покурил(а)😓")
    btn5 = types.KeyboardButton("Нет😁")
    markup.add(btn4, btn5)
    bot.send_message(message.chat.id, text="Вы хотите сбросить таймер?".format(
        message.from_user), reply_markup=markup)


@bot.message_handler(commands=['motivation'])
def start_motivation(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, )
    btn1 = types.KeyboardButton("Здоровье💊")
    btn2 = types.KeyboardButton("Беременность🤰")
    btn3 = types.KeyboardButton("Вред для близких💗")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Выберите тему мотивации, которая вам ближе всего".format(
        message.from_user), reply_markup=markup)


@bot.message_handler(commands=['days'])  # выводит сколько дней не курил
def start_days(message):
    dats = datetime.strptime(get_from(message.chat.id), '%d/%m/%Y')
    dat = datetime.now() - dats
    bot.send_message(message.chat.id, "Вы не курите " +
                     str(dat.days) + " дней")


@bot.message_handler(content_types=['text'])
def func(message):
    print(message.text)
    if (message.text == "Здоровье💊"):
        bot.send_message(
            message.chat.id, "Заострим внимание, на кратковременных отрицательных последствиях:👁\n\nПреходящее повышение артериального давления\nОтдышка\nУсиленное сердцебиение\nОслабление внимания\nГоловокружение\nСлабость\n\nНесмотря на мимолетность краткосрочных эффектов(15-20 минут), постепенно приобретаются серьёзные проблемы со здоровьем:\n\nЗаболевания сердечно-сосудистой системы🫀 : атеросклероз, гипертоническая и ишемическая болезнь, облитерирующий эндартериит, ведущий к утрате конечностей.\nБолезни органов дыхания🫁: хронический бронхит курильщика, обструктивные процессы в тканях бронхо-лёгочной системы, злокачественные образования бронхов и легких.\nСнижение потенции у мужчин🙇\nНикотин и вредные вещества, содержащиеся в дыму, становятся причиной болезненных нарушений эндокринной системы, гормональных сбоев\n\nМотивация для отказа от курения включает компонент долголетия. Регулярное табакокурение в течение 10-15 лет забирает у курящей личности около 10 лет жизни. А осложнения становятся причиной патологических состояний.\n\nСнижение умственных способностей и эмоциональное уплощение🧠\n\nРегулярное табакокурение ведет к постепенному увеличению количества выкуриваемых сигарет. Потребность появляется даже в ночные часы. Постоянное отравляющее действие дыма становится причиной недосыпания, хронической интоксикации организма. Все эти негативные проявления сказываются на когнитивных возможностях мозга. У больных появляется забывчивость (следствие атеросклероза церебральных сосудов), обеднение эмоций. Пациент теряет желание саморазвития. Агрессивные компоненты, образующиеся при горении табака, ведут к раннему развитию слабоумия. Кислородная недостаточность приводит к деструктивным процессам в клетках головного мозга. Мнимое улучшение наступает только при выкуривании очередной сигареты.\n\nОчень важно задумываться о своём будущем. Может быть сложным осознать, что последствия от курения будут! Но к сожалению, всё выше написанное может ожидать любого курильщика. Хорошо жить - значит быть здоровым!✨✨", reply_markup=telebot.types.ReplyKeyboardRemove())

    elif (message.text == "Беременность🤰"):
        bot.send_message(message.chat.id, "Рождение детей🤱\nБеременности у будущих матерей, пристрастившихся к табакокурению, страдает развивающийся ребёнок. У него отмечается гипоксия мозга. После зачатия чаще случаются выкидыши. Беременные подвергают себя и развивающийся плод дополнительной опасности осложнений🤕\n\nУ них чаще, чем у некурящих выявляются:\n\nОтслойки плаценты\nРазвитие токсикозов\nПреждевременные роды\nСлабость родовой деятельности\n\nУ мужчин от сигаретного дыма ухудшается качественный и количественный состав спермы, приводя к затруднению или отсутствию оплодотворяющей способности😳. Так что для здорового потомства необходимо, чтобы курить бросали одновременно и отец и мать.😌",
                         reply_markup=telebot.types.ReplyKeyboardRemove())

    elif (message.text == "Вред для близких💗"):
        bot.send_message(message.chat.id, "Вред для окружающих💩\nНа законодательном уровне курение запрещено во многих общественных местах. Но там, где некурящие люди попадают в зону действия дыма, они подвергаются не меньшей опасности, чем сами курильщики.\n\nПомимо очевидных минусов - таких как неприятный запах от курильщика, постоянное курение при сожителях, делает их пассивными курильщиками, что не сильно отличается от самого курения.\nПассивное вдыхание веществ образующихся при горении табака оказывает болезнетворное влияние на здоровье организма.Особый вред получают дети👶\n\nЭтот факт следует полноценно осознавать любому курильщику: он является опасным для окружающих. Если ваши близкие люди, родственники, дети не курят - то вы можете стать их причиной проблем со здоровьем💔💔",
                         reply_markup=telebot.types.ReplyKeyboardRemove())

    elif (message.text == "Да,покурил(а)😓"):
        bot.send_message(message.chat.id, "Не переживайте это норм РАСПИСАТЬ",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_sticker(
            message.chat.id, 'CAACAgIAAxkBAAI2PGV-PL7XiP9-FKZ6Vu_FNG_Jdk23AAIvFAACClqQSAVN4g4SKAGuMwQ')
        set_date(message.chat.id, datetime.now().strftime("%d/%m/%Y"))

    elif (message.text == "Нет😁"):
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI2SGV-P-RyRTdwZgABfIEr2OxFIZZ3AAOUFQACaTKISP17TjyowseiMwQ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())

    elif (message.text == "Нет"):
        dats = datetime.strptime(get_from(message.chat.id), '%d/%m/%Y')
        dat = datetime.now() - dats
        bot.send_message(message.chat.id, "Вы молодец, вы не курили уже " +
                         str(dat.days) + " дней💋",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_sticker(
            message.chat.id, 'CAACAgIAAxkBAAI2S2V-QFu94m7hgjce5IeSjAHxS7ulAAJJQgACjxHxS0gw25PrXODJMwQ')
    elif (message.text == "Да"):
        bot.send_message(message.chat.id, "Ничего страшного! Начнем наш отчёт сначала, я верю в вас!",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_sticker(
            message.chat.id, 'CAACAgIAAxkBAAI2RWV-PQZXof-YA_FloxaOccspMZL1AAK-FgACezdAS5BXvt5CbJW8MwQ')
        set_date(message.chat.id, datetime.now().strftime("%d/%m/%Y"))


def notification():
    print("[INFO] Start sending notifications")
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, )
    bt1 = types.KeyboardButton("Да")
    bt2 = types.KeyboardButton("Нет")
    markup.add(bt1, bt2)
    ids = get_users()  # возвращает список с id пользователей, которые сейчас участвуют
    print(f"users in challenge: {ids}")
    for idt in ids:
        bot.send_message(idt, text="Вы курили?🤨".format(idt),
                         reply_markup=markup)


def schedule_func():  # как часто пользователи будут получать сообщение вы курили?
    schedule.every(40).seconds.do(notification)
    while run_schedule:
        time.sleep(1)
        schedule.run_pending()


run_schedule = True
threading.Thread(target=schedule_func).start()

bot.infinity_polling()
