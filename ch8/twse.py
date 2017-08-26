# source: https://github.com/yotsuba1022/web-crawler-practice/blob/master/ch4/tw_stock_exchange.py

import requests
import time


TWSE_URL = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json'


def get_web_content(stock_id, current_date):
    resp = requests.get(TWSE_URL + '&date=' + current_date + '&stockNo=' + stock_id)
    if resp.status_code != 200:
        return None
    else:
        return resp.json()


def get_data(stock_id, current_date):
    info = list()
    resp = get_web_content(stock_id, current_date)
    if resp is None:
        return None
    else:
        if resp['data']:
            for data in resp['data']:
                record = {
                    '日期': data[0],
                    '開盤價': data[3],
                    '收盤價': data[6],
                    '成交筆數': data[8]
                }
                info.append(record)
        return info


def main():
    stock_id = '2330'
    current_date = time.strftime('%Y%m%d')
    current_year = time.strftime('%Y')
    current_month = time.strftime('%m')
    print('Processing data for %s %s...' % (current_year, current_month))
    collected_info = get_data(stock_id, current_date)
    for info in collected_info:
        print(info)


if __name__ == '__main__':
    main()