import telebot
import stuff

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
   bot.send_message(
        message.chat.id, "Мотивацию надо пооднять!!!")
   
@bot.message_handler(commands=['days'])
def start_days(message):
   bot.send_message(
        message.chat.id, "Вы не курите столько дней:")
   
bot.infinity_polling()
