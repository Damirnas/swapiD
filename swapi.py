import requests
from pathlib import Path


class APIRequester:

    def __init__(self, base_url):
        # Храним базовый URL API
        self.base_url = base_url

    def get(self, url=''):
        # Запрос к серверу Отправляем GET-запрос к API по указанному URL
        try:
            response = requests.get(self.base_url + url)
        # Обрабатываем возможные ошибки при отправке запроса
        # Проверяем сатутс ответа API
            response.raise_for_status()
        # Возвращаем ответ API в виде объекта response
            return response
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')


class SWRequester(APIRequester):

    def get_sw_categories(self, url='/'):
        # Получаем список категорий данных из API SWAPI
        response = self.get(url).json()
        return response.keys()

    def get_sw_info(self, sw_type):
        # Получаем информацию о конкретной категории данных из API SWAPI
        response = self.get(f'/{sw_type}/')
        return response.text


def save_sw_data():
    swapi = SWRequester('https://swapi.dev/api')
    Path('data').mkdir(exist_ok=True)
    for category in swapi.get_sw_categories():
        with open(f'data/{category}.txt', 'w', encoding='utf-8') as file:
            file.write(swapi.get_sw_info(category))


save_sw_data()
