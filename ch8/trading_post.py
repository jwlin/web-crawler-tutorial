import requests
from bs4 import BeautifulSoup


TWSE_URL = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAYMAIN.php'


def get_data(stock_id, year, month):
    year = str(year)
    month = '0' + str(month) if month < 10 else str(month)
    data = {
        'query_year': year,
        'query_month': month,
        'CO_ID': stock_id,
    }
    info = list()
    resp = requests.post(TWSE_URL, data=data)
    soup = BeautifulSoup(resp.text, 'html.parser')
    for tr in soup.find('table').tbody.find_all('tr'):
        # 日期, 成交股數, 成交金額, 開盤價, 最高價, 最低價, 收盤價, 漲跌價差, 成交筆數
        tds = tr.find_all('td')
        info.append((tds[0].text, tds[3].text, tds[6].text, tds[7].text, tds[8].text))
    return info


if __name__ == '__main__':
    y = 2016
    stock_id = '2330'
    all_info = list()
    for m in range(9, 13):
        print('Processing', y, m)
        all_info.append(get_data(stock_id, y, m))
    print('日期, 開盤價, 收盤價, 漲跌價差, 成交筆數')
    for l in all_info:
        for t in l:
            print(t)
