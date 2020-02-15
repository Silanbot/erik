import telebot
from telebot import types
ref_link = 'https://telegram.me/{}?start={}'


bot = telebot.TeleBot('1057186464:AAFXhlbsDq02N7GTd3XQZrZGQibDErw_uNQ')



markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
markup = types.InlineKeyboardMarkup(row_width=2)



@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("💼 My account")
    item2 = types.KeyboardButton("👥 My Downline")
    item3 = types.KeyboardButton("ℹ Join Channels")


    markup.add(item1,item2,item3)

    bot.send_message(message.chat.id, 'Hello {0.first_name}\nWelcome to {1.first_name}!'.format(message.from_user, bot.get_me()),parse_mode = 'html', reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def keyboard(message):
    if message.chat.type == 'private':
        if message.text == '💼 My account':
            bot_name = bot.get_me().username
            bot.send_message(message.chat.id, 'Account ID: '+str(message.chat.id)+'\nRefferal link: '+ref_link.format(bot_name, message.chat.id))
        elif message.text == '👥 My Downline':
            bot.send_message(message.chat.id, 'Your refferal level - 0')
        elif message.text == 'ℹ Join Channels':
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton(text='Crypto News', url='https://t.me/Crypto_God_Father')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Join Crypto News channel to get our coin news and to share them to your friends.'
                                              '\n(and in case the posts doesnt work we add another button and link to @Crypto_God_Father):'
                                              '\nJoin Crypto Waves Pumps to get the coin for the pump.', reply_markup=markup)







if __name__ == '__main__':
    bot.polling(none_stop=True)
