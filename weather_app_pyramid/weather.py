from datetime import datetime
import os
import pytz
import requests
import math

API_KEY = '4964406b266b1b8d27d5f09d0f190d8f'
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}'


def query_api(city):
    try:
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        data = None
    return data
