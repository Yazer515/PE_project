import telebot


bot = telebot.TeleBot('6204926151:AAH_u-Fjhs0C-NcX3kwaBdMps8I9C65fzv0')
    

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)