#!/usr/bin/env python
#
#【bot】
#
# 概要: telegram 用のサンプルbot
#       OpenWeatherMap を利用して天気予報を返信する
#
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time
import random
import weather as wt
import re

TOKEN = ""

def reply():
    return wt.weather()

class Bot(object):
    def __init__(self):
        self.user_context = {}

    def start(self, bot, update):
        # システムからの最初の発話
        update.message.reply_text('こんにちは。対話を始めましょう。')

    def message(self, bot, update):
        # ユーザ発話
        user_message = update.message.text
        m = re.search(r"天気予報", user_message)
        send_message = reply() if m else "東京の天気予報をお教えできます。天気予報と聞いてください"
        # 発話を送信
        update.message.reply_text(send_message)
        
    def run(self):
        updater = Updater(TOKEN)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(MessageHandler(Filters.text, self.message))
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    mybot = Bot()
    mybot.run()
