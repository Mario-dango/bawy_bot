#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '1733267643:AAG0KXIZdVUMGoI-g1Y1bg5osjrFhnGZKKQ'

bawy = telebot.TeleBot(API_TOKEN)



# Handle '/start' and '/help'
@bawy.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bawy.reply_to(message, """\
Hola a todos yo soy BawyBot... etoou... también puedes llamarme BB hehe.
Pues.. mi amo me ha creado para ser un asistente domótico y estaré en cosntante modificación, espero dar lo mejor de mí n.n\
""")
    sti = open('/files/stickers/hello.webp', 'rb')
    bawy.send_sticker(message, sti)
    bawy.send_sticker(message, "FILEID")

#def sendSticker(message):|
#    # sendSticker
#    sti = open('/files/stickers/aww.webp', 'rb')
#    tb.send_sticker(chat_id, sti)
#    tb.send_sticker(chat_id, "FILEID")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bawy.message_handler(func=lambda message: True)
def echo_message(message):

    bawy.reply_to(message, message.text)



bawy.polling()