import telebot
import os

API_TOKEN = os.getenv('API_TOKEN')

if API_TOKEN is None:
    raise ValueError("No API token provided")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Clicker Game!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
