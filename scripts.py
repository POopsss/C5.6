import requests
import json
from conf import lis

class Converter():
    @staticmethod
    def converter(message):
        try:
            error(message)
        except Exception as e:
            if type(e) is ValueError:
                return f'Неверно указано количество переводимой валюты ({message.split()[2]}).'
            else:
                return e
        else:
            try:
                m = message.lower().split()
                r = requests.get(
                    f'https://api.currencyapi.com/v3/latest?apikey=60SwZ6fyadaFQWVadd8lagfKiVPIfZkJ7OqxMVol&currencies={lis[m[1]]}&base_currency={lis[m[0]]}')
                d = json.loads(r.content)
                s = d['data'][lis[m[1]]]['value'] * float(m[2])
            except Exception:
                return 'Произошла ошибка на сервере'
            else:
                return s

def error(message):
    m = message.lower().split()
    if len(m) != 3:
        raise Exception(
            'Введите через пробел валюту которую надо перевести, валюту в которую надо перевести и количество переводимой валюты')
    if m[0] not in lis:
        raise Exception(f'Значение валюты ({message.split()[0]}) которую надо перевести указано не корректно.')
    if m[1] not in lis:
        raise Exception(f'Значение валюты ({message.split()[1]}) в которую надо перевести указано не корректно.')
    float(m[2])
