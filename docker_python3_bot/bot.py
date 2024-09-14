# bot.py
import os
import telebot

# Получаем токен бота из переменной окружения
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling()
