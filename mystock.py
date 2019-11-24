from pprint import pprint
import requests
import json
import functools
import time

today = time.strftime('%Y-%m-%d',time.localtime())


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
    return price
    '''开盘，收盘，最高，最低，量'''


stock_today = functools.partial(stock_ifzq,start_date=today,end_date=today)


def today_close(stock_code):
    '''Get today stock close price'''
    return stock_today(stock_code)[0][2]

 
if __name__ == '__main__':
    stock_code = 'sz510510'
    a = today_close(stock_code)
    print(a)