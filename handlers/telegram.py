import telebot
import os

TOKEN = os.getenv('TOKEN')  # "1130387079:AAFy-__________-yS5uFKOh1mTrBqeKQ"
USER_ID = os.getenv("USER_ID")  # 37___6279


def send_notify(message):
    bot = telebot.TeleBot(TOKEN)
    bot.send_message(USER_ID, message)

