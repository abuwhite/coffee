from coffeeboom.api.telegram import bot
import telebot
from telebot import types


@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup()
    btn_menu = types.KeyboardButton('Меню 📖')
    btn_receive = types.KeyboardButton('Заказать 🛒')
    btn_contact = types.KeyboardButton('Контакты 📞')

    markup.row(btn_menu, btn_receive)
    markup.row(btn_contact)

    bot.send_message(message.chat.id, 'Это бот coffeeboom', reply_markup=markup)


# @bot.message_handler(content_types=["text"])
# def gen_message(message):
#     # bot.send_message(message.chat.id, answer, parse_mode='Markdown')
# 
#     time.sleep(11)
#     quest = '**Если вы хотите узнать что-то ещё, задайте вопрос или нажмите на "🪄"**'
#     bot.send_message(message.chat.id, quest, parse_mode='Markdown', reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
