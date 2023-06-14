import time
from typing import List

import requests

from Remembers import AssistantRemembers
from TOKEN import TOKEN, TOKEN_TELEGRAM


def get_time(text: str) -> str | None:
    """
    from just phrase, return date_time, when deadline
    :param text: example 'напомни мне 27 мая в 17:00 сделать то-то'
    return: 27.05
    """
    month = {
        'январ': 1,
        'феврал': 2,
        'март': 3,
        'апрел': 4,
        'мая': 5,
        'май': 5,
        'июн': 6,
        'июл': 7,
        'август': 8,
        'сентябр': 9,
        'октябр': 10,
        'ноябр': 11,
        'декабр': 12,
    }
    answer = None
    for i in range(len(text.split())):
        if text.split()[i].isalnum():

            if text.split()[i + 1] not in ['май', 'мая']:
                len_text = len(text.split())
                answer = f'{text.split()[i]}.{month[text.split()[i + 1][:len_text - 1]]}'
                # '27.05'
            # you should always say number with month

    return answer


class Assistent:
    def __init__(self):
        self.cache = AssistantRemembers()

    def set_remember(self, text: str):
        self.cache.add(text)

    def get_remembers(self) -> List[str]:
        pass

    def send_to_telegram(self, text):

        requests.post(
            f'https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage?chat_id=644823883&text={text}')

    def get_weather(self):

        lat, lon = 53.195873, 50.100193  # Samara

        url = f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&[lang=ru_RU]'

        headers = {'X-Yandex-API-Key': TOKEN}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # print(data)
            fact = data['fact']
            good = 'ЕБААА ВУХУ, МИР ОХУЕНЕН, Я ОХУЕНЕН, ЛЮБЛЮ ЖИЗНЬ'
            bad = 'ЕБААААААААААААААААААААТЬ НАХУЙ'
            good_not_rainy = 'Щииищ, ещё и дождя не будет'
            bad_with_rainy = 'Ебал этот день, ебал этот час. Дождь с шансем:'
            condition = good if fact['condition'] == 'clear' else bad
            temp = fact['temp']
            rainy = good_not_rainy if 0 == fact['prec_strength'] else str(float(bad_with_rainy) * 100)
            return f'Сейчас {condition} {rainy}, температура {temp} градусов по Цельсию.'
        else:
            return 'Не удалось получить информацию о погоде.'
            # pprint(response.json())


def main():
    print('Hi')
    End = True
    while End:
        Assistent().send_to_telegram(Assistent().get_weather())
        time.sleep(7200)


if __name__ == '__main__':
    main()