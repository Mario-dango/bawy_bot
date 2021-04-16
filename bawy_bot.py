#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '1733267643:AAG0KXIZdVUMGoI-g1Y1bg5osjrFhnGZKKQ'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hola a todos yo soy BawyBot... etoou... también puedes llamarme BB hehe.
Pues.. mi amo me ha creado para ser un asistente domótico y estaré en cosntante modificación, espero dar lo mejor de mí n.n\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.polling()