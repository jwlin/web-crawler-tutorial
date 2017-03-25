import requests
import json
from datetime import datetime, timedelta


def get_stock(query):
    # query 可以是多支股票, 如 TPE:2330,TPE:2498, 不同股票以 , 分開
    resp = requests.get('http://finance.google.com/finance/info?client=ig&q=' + query)
    if resp.status_code == 200:
        # 移除回傳資料開頭的 //
        # 剩下的資料是一個 list of dict, 每個 dict 是一支股票的資訊
        return json.loads(resp.text.replace('//', ''))
    else:
        return None


def get_stock_history(stock_id, stock_mkt):
    resp = requests.get('http://www.google.com/finance/getprices?q=' + stock_id + '&x=' + stock_mkt + '&i=86400&p=1M')
    ''' e.g.,
    EXCHANGE%3DTPE
    MARKET_OPEN_MINUTE=540
    MARKET_CLOSE_MINUTE=810
    INTERVAL=86400
    COLUMNS=DATE,CLOSE,HIGH,LOW,OPEN,VOLUME
    DATA=
    TIMEZONE_OFFSET=480
    a1488346200,186,188.5,186,188.5,46176000
    1,186,188.5,185,188,39914000
    2,184,185,184,184.5,28085000
    5,183.5,184.5,183.5,184,12527000
    ...
    '''
    index = -1
    lines = resp.text.split('\n')
    for line in lines:
        # 'a' 開頭表示股價資訊起始列
        if line.startswith('a'):
            index = lines.index(line)
            break
    if index > 0:
        lines = lines[index:]
        # 找出起始行日期
        unix_time = int(lines[0].split(',')[0][1:])
        init_time = datetime.fromtimestamp(unix_time)
        rows = list()
        # 處理第一列
        first_row = lines[0].split(',')
        first_row[0] = init_time
        rows.append(first_row)
        # 處理剩餘列
        for l in lines[1:]:
            if l:
                row = l.split(',')
                delta = int(row[0])
                row[0] = init_time + timedelta(days=delta)
                rows.append(row)
        return rows
    else:
        return None


if __name__ == '__main__':
    query = 'TPE:2330'
    print(query, '即時股價')
    stocks = get_stock('TPE:2330')
    print(stocks[0])
    print('-----')
    stock_id, stock_mkt = '2330', 'TPE'
    print(stock_mkt, stock_id, '歷史股價 (Date, Close, High, Low, Open, Volume)')
    rows = get_stock_history('2330', 'TPE')
    for row in rows:
        print(row[0].strftime("%Y/%m/%d"), row[1:])
