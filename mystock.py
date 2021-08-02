

__version__ = 20191124


from pprint import pprint
import requests
import json
import functools
import time
import datetime
from functools import lru_cache

from mydec import timethis

def stock_day():
    '''Get stock open last day'''
    # day = time.strftime('%Y-%m-%d %w',time.localtime())
    today = datetime.date.today()
    while datetime.datetime.weekday(today) > 4:
        today -= datetime.timedelta(days=1)
    # print(today)
    return today


def stock_ifzq(stock_code,start_date,end_date,limit=None)->list:
    '''Get stock price from ifzq'''
    if not limit:
        limit = 5
    url = f'http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?\
        param={stock_code},day,{start_date},{end_date},{limit},qfq'
    r = requests.get(url)  
    # pprint(r.text)
    # print('=================================================')
    data_json = json.loads(r.text)
    # pprint(data_json)
    try:
        price = data_json['data'][stock_code]['day']
    except KeyError:
        price = data_json['data'][stock_code]['qfqday']
    print(f'{stock_code} price is {price}')
    return price
    '''开盘，收盘，最高，最低，量'''


stock_today = functools.partial(stock_ifzq,start_date=stock_day(),end_date=stock_day())

@timethis
@lru_cache(maxsize=32)
def today_close(stock_code):
    '''Get today stock close price'''
    return stock_today(stock_code)[0][2]

 
if __name__ == '__main__':
    # stock_code = 'sz510510'
    # a = today_close(stock_code)
    # print(a)
    stock_day()