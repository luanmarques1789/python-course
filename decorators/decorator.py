import requests
import time


def calc_time(func):
    """Calculate the runtime of the function passed in the parameter"""
    def wrapper():
        init_time = time.time()
        print('Getting the exchange time...')
        func()
        final_time = time.time()
        print(f'The exchange time is: {final_time - init_time:.2f} s')
    return wrapper


@ calc_time
def get_dollar_exchange():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    request = requests.get(url)
    response = request.json()
    print(f"R${float(response['USDBRL']['bid']):.2f}")


get_dollar_exchange()
