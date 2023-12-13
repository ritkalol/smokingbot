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


bot.infinity_polling()
