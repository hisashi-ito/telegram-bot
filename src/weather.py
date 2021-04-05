#!/usr/bin/env python3
#
# 【weather】
#
import requests
import json
import datetime

API_KEY = ""
CITY = 'tokyo'
URL = 'http://api.openweathermap.org/data/2.5/forecast?q=' + CITY + ',jp&units=metric&APPID=' + API_KEY

def weather():
    response = requests.get(URL)
    data = response.json()
    # 直近のデータのみ取り扱う
    data = data["list"][0]
    utime = int(data["dt"])
    time = datetime.datetime.fromtimestamp(utime)
    return "{} の東京の天気は{}".format(time, data["weather"][0]["main"])
