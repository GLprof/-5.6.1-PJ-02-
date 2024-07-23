import telebot
import math


TOKEN = '7384750969:AAFn1AiwoJ1EE4m9DbXWdFYQINvSKUoOpmM'
bot = telebot.TeleBot(TOKEN)

# Функция для обработки команды /start или /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Этот бот вычисляет объём цилиндра."
                          "Чтобы начать, отправь мне радиус и высоту через пробел.")

# Функция для обработки других сообщений
@bot.message_handler(func=lambda message: True)
def calculate_volume(message):
    try:
        radius, height = map(float, message.text.split())
        volume = math.pi * radius**2 * height

        response = f"Объем цилиндра равен {volume:.2f} единиц объема."
    except ValueError:
        response = "Что-то пошло не так. Пожалуйста, введите: /start или /help. "

    bot.reply_to(message, response)


bot.polling()
