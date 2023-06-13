from typing import List

import requests

from Remembers import AssistantRemembers


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

    def get_weather(self):

        api_key = 'your_api_key'
        lat, lon = 55.75396, 37.620393  # координаты Москвы

        url = f'https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}'

        headers = {'X-Yandex-API-Key': api_key}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            fact = data['fact']
            condition = fact['condition']
            temp = fact['temp']
            print(f'Сейчас {condition}, температура {temp} градусов по Цельсию.')
        else:
            print('Не удалось получить информацию о погоде.')


def main():
    print('Hi')


if __name__ == '__main__':
    main()