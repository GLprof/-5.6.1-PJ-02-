import requests

class APIException(Exception):
    pass

class CurrencyConverter:

    @staticmethod
    def get_price(base, quote, amount):
        url = f'https://api.exchangerate-api.com/v4/latest/{base}'
        response = requests.get(url)

        if response.status_code != 200:
            raise APIException('ошибка при извлечении данных из API')

        data = response.json()

        if quote not in data['rates']:
            raise APIException('Валюта не поддерживается')

        price: object = data['rates'][quote] * amount
        return price