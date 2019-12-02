import telebot
from googletrans import Translator

translator = Translator()
bot = telebot.TeleBot('1001004694:AAHaLKSS0oz86QYnQqtuWm02aNcqY03m6Gc')

@bot.message_handler(content_types=['text'])
def send_text(message):

    language = translator.detect(message.text).lang
    temp = translator.translate(message.text, dest='fr').text
    temp = translator.translate(temp, dest=language).text
    bot.send_message(message.chat.id, temp)

bot.polling()