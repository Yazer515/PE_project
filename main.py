import os

import telebot

key = os.environ["BOT_TOKEN"]

bot = telebot.TeleBot(key)
  
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Напиши /help")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)