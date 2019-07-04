import telebot
import urllib.request as req
from random import randint

import tokens
import time


bot = telebot.TeleBot(tokens.token, threaded=False)
max_num = 2170
user_messages = 0


@bot.message_handler(content_types=['text'])
def send_timetable(message):
    global user_messages
    user_messages += 1
    print(user_messages)
    url = "https://xkcd.com/" + str(randint(1, max_num)) + "/"
    image_url = ""
    url_tokens = req.urlopen(url).read().split()
    for token in url_tokens:
        if str(token).find('https://imgs.xkcd.com/') != -1:
            image_url = token
    bot.send_photo(message.chat.id, req.urlopen(image_url.decode('ASCII')).read())


while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        print('Connection error, restart in 1 sec')
        time.sleep(1)