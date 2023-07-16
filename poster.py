import string
from datetime import datetime, timedelta
from random import randint, choice

import requests
from faker import Faker

CATEGORIES = {
    '01': 'health',
    '02': 'clothes',
    '03': 'eating out',
    '04': 'food',
    '05': 'trips',
    '06': 'entertainments',
    '07': 'connection',
    '08': 'car',
    '09': 'payments',
    '99': 'other',
}
LINK = 'http://127.0.0.1:8000/create/'
METHODS = ['cash', 'card']


def time_generator():
    random_string = ''.join(choice(string.ascii_letters) for _ in range(10))

    now = datetime.now()  # получаем текущую дату и время

    # создаем объект типа timedelta, который представляет разницу
    delta = timedelta(minutes=randint(1, 5))  # выбираем случайное количество минут
    random_time = str(now - delta)
    return random_time if choice([1, 2]) == 1 else random_string


def payer_generator():
    return Faker().name()


def amount_generator():
    return str(randint(1, 10))


def category_generator():
    return choice(list(CATEGORIES.values()))


def method_generator():
    return choice(METHODS)


def create():
    data = {
        "time": time_generator(),
        "payer": payer_generator(),
        "amount": amount_generator(),
        "category": category_generator(),
        "method": method_generator()
    }
    r = requests.post(LINK, json=data)
    return r.text


if __name__ == '__main__':
    for _ in range(100):
        result = create()
        print(result)
