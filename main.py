import telebot
import stuff
import random
import sqlite3 as sql
from telebot import types

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
    mass_videos = [video_0,video_1,video_2,video_3,video_4,video_5,video_6,video_7,video_8,video_9]
    bot.send_message(
        message.chat.id, "Предоставляем вам видео")
    bot.send_message(
        message.chat.id, mass_videos[random.randint(0,len(mass_videos)-1)])
    


@bot.message_handler(commands=['books'])
def sbooks_message(message):
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
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Здоровье")
        btn2 = types.KeyboardButton("Беременность")
        btn3 = types.KeyboardButton("Вред для близких")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выберите тему мотивации, которая вам ближе всего".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Здоровье"):
        bot.send_message("Преходящее повышение артериального давления.Одышка.")
    elif(message.text == "Беременность"):
        bot.send_message("Ойойой")
    else:
        bot.send_message("Good boy")

@bot.message_handler(commands=['days'])
def start_days(message):
    bot.send_message(
        message.chat.id, "Вы не курите столько дней:")


bot.infinity_polling()
