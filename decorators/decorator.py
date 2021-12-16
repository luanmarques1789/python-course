# video: https://www.youtube.com/watch?v=P0aW1czXHio

import requests
import time


def calc_time(func):
    """Calculate the runtime of the function passed in the parameter"""
    def wrapper():
        init_time = time.time()
        print('Getting the time...')
        func()
        final_time = time.time()
        print(f'The response time was: {final_time - init_time:.2f} s')
    return wrapper


@ calc_time
def get_dollar_exchange():
    """Get the dollar exchange rate from the API"""

    url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    request = requests.get(url)
    response = request.json()
    print(f"R${float(response['USDBRL']['bid']):.2f}")


get_dollar_exchange()
