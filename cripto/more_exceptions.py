import json

import requests

from cripto.APP import APIException, values, keys


class More_Exception(Exception):
    quote, base, amount = values
    if quote == base:
        raise APIException('Зачем тебе сравнение валюты самой с собой!?')
    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise APIException('Не удалось обработать валюту.')
    try:
        base_ticker = keys[base]
    except KeyError:
        raise APIException('Не удалось обработать валюту.')
    try:
        amount = float(amount)
    except ValueError:
        raise APIException(f'Не удалось обработать количество {amount}')




