import telebot
import os

API_TOKEN = os.getenv('7218079882:AAGYrv9K047rLfsoE4p59orPA73kUUeNais')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Clicker Game!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
