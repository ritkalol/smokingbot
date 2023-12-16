import telebot
import stuff
from my_utils import *
import random
from telebot import types
from datetime import datetime
import threading
import schedule
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
        message.chat.id, "Мы начали челлендж, ждите следующего оповещения! Пока что можете посмотреть видео о вреде курения")
    set_date(message.chat.id, datetime.now().strftime("%d/%m/%Y"))


@bot.message_handler(commands=['video'])
def video_message(message):
    video_0 = 'https://www.youtube.com/watch?v=PBR-Yev5vO8&t=58s'
    video_1 = 'https://www.youtube.com/watch?v=MG52aw2hoWI'
    video_2 = 'https://www.youtube.com/watch?v=Y5KvDrWX3ls'
    video_3 = 'https://www.youtube.com/watch?v=lOx4HgqchUw'
    video_4 = 'https://www.youtube.com/watch?v=Qt_0JwpuSkU'
    mass_videos = [video_0, video_1, video_2, video_3, video_4]
    bot.send_message(
        message.chat.id, "Предоставляем вам видео")
    bot.send_message(
        message.chat.id, mass_videos[random.randint(0, len(mass_videos)-1)])


@bot.message_handler(commands=['books'])
def sbooks_message(message):
    bot.send_message(
        message.chat.id, "Предоставляем вам книги")


@bot.message_handler(commands=['want_smoke'])
def want_smoke_message(message):
    bot.send_message(
        message.chat.id, "Не кури, брат")


@bot.message_handler(commands=['reset_timer'])
def start_reset_timer(message):
    bot.send_message(
        message.chat.id, "Не переживайте это норм РАСПИСАТЬ")
    set_date(message.chat.id, datetime.now().strftime("%d/%m/%Y"))


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


@bot.message_handler(commands=['days'])#выводит сколько дней не курил
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
        bot.send_message(message.chat.id, "Ойойой",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    elif (message.text == "Вред для близких💗"):
        bot.send_message(message.chat.id, "Good boy",
                         reply_markup=telebot.types.ReplyKeyboardRemove())


def notification():
    print("[INFO] Start sending notifications")
    # возвращает список с id пользователей, которые сейчас участвуют
    ids = get_users()
    for id in ids:
        pass


def schedule_func():
    schedule.every(10).seconds.do(notification)
    while run_schedule:
        time.sleep(1)
        schedule.run_pending()


run_schedule = True
threading.Thread(target=schedule_func).start()

bot.infinity_polling()
print("[INFO] Bot closed")
run_schedule = False
