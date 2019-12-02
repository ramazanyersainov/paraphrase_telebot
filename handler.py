import telebot
from googletrans import Translator

translator = Translator()
f = open('token.txt')

bot = telebot.TeleBot(f.readline().split('\n')[0])

f.close()

@bot.message_handler(content_types=['text'])
def send_text(message):

    language = translator.detect(message.text).lang
    temp = translator.translate(message.text, dest='fr').text
    temp = translator.translate(message.text, dest='mt').text
    temp = translator.translate(temp, dest=language).text
    bot.send_message(message.chat.id, temp)

bot.polling()