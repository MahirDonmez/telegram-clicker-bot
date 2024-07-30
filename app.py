from flask import Flask, request
import telegram
import os

TOKEN = '7218079882:AAGYrv9K047rLfsoE4p59orPA73kUUeNais'
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat_id
    text = update.message.text

    if text == '/start':
        bot.sendMessage(chat_id=chat_id, text="Welcome to my Telegram bot!")
    elif text == '/ping':
        bot.sendMessage(chat_id=chat_id, text="Pong!")
    else:
        bot.sendMessage(chat_id=chat_id, text="Sorry, I don't understand that command.")

    return 'ok'

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(threaded=True)
