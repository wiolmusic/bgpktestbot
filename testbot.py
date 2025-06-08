import telebot
from telebot import types

TOKEN = '7833100588:AAFTWUPLScW-MyMM9mEcSHUDzwadG7N-IDI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Кто не пройдет практику у андрея в компании - получит по-лбу"
    )

    with open('images/vibor.png', 'rb') as photo:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("отчислиться", callback_data='choice'))
        markup.add(types.InlineKeyboardButton("взять академ", callback_data='choice'))
        markup.add(types.InlineKeyboardButton("улететь на канары", callback_data='choice'))
        bot.send_photo(message.chat.id, photo, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'choice')
def handle_choice(call):
    with open('images/otlichno.png', 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, "вы сделали правильный выбор - наслаждайтесь.")
    bot.answer_callback_query(call.id)

bot.polling(none_stop=True)
