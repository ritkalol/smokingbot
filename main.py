import telebot
import stuff
import sqlite3 as sql
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


def delete_user(id):
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.executescript("""
            DELETE FROM users
            WHERE id == '{}'  
        """.format(id))
        con.commit()


def clear_db():
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.executescript("""
            DELETE FROM users  
        """.format(id))
        con.commit()


def set_date(id, date_from):
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT * FROM users
            WHERE id == '{}'  
        """.format(id))
        records = cur.fetchall()
        if len(records) == 0:
            cur.executescript("""
            INSERT INTO users (id, date_from) VALUES ('{}', '{}')  
            """.format(id, date_from))
        else:
            cur.executescript("""
            UPDATE users
            SET date_from='{}'
            WHERE id == '{}' 
            """.format(date_from, id))
        con.commit()


def get_from(id):
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT date_from FROM users
            WHERE id == '{}'  
        """.format(id))
        records = cur.fetchall()
        return records[0][0].split(' ')[0]


def get_users():
    con = sql.connect('users.db')
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT id FROM users 
        """.format(id))
        records = cur.fetchall()
        return [i[0] for i in records]


@bot.message_handler(commands=['start_challenge'])
def start_challenge_message(message):
    bot.send_message(
        message.chat.id, "Мы начали челлендж!")
    set_date(message.chat.id, datetime.now().strftime("%d/%m/%Y"))


@bot.message_handler(commands=['video'])
def video_message(message):
    bot.send_message(
        message.chat.id, "Предоставляем вам видео")


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
        message.chat.id, "Начинаем заново")


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


@bot.message_handler(content_types=['text'])
def func(message):

    if (message.text == "Здоровье💊"):
        bot.send_message(
            message.chat.id, "Преходящее повышение артериального давления.Одышка.", reply_markup=telebot.types.ReplyKeyboardRemove())
    elif (message.text == "Беременность🤰"):
        bot.send_message(message.chat.id, "Ойойой",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, "Good boy",
                         reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(commands=['days'])
def start_days(message):
    bot.send_message(
        message.chat.id, "Вы не курите столько дней:")


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
