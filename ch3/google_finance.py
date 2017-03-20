import requests
from bs4 import BeautifulSoup


# 網址後方加上 MARKET:STOCK_ID 即為個股資訊. e.g, TPE:2330
G_FINANCE_URL = 'https://www.google.com/finance?q='
G_FINANCE_HIS_URL = 'https://www.google.com/finance/historical?q='


def get_web_page(url, stock_id):
    resp = requests.get(url + stock_id)
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_stock_info(dom):
    soup = BeautifulSoup(dom, 'html5lib')
    stock = dict()
    stock['name'] = soup.title.text.split(':')[0]
    stock['current_price'] = soup.find(id='price-panel').span.span.text
    stock['current_change'] = soup.find(id='price-panel').find('div', 'id-price-change').text.strip().replace('\n', ' ')
    for table in soup.find('div', 'snap-panel').find_all('table'):
        for tr in table.find_all('tr')[:3]:
            key = tr.find_all('td')[0].text.lower().strip()
            value = tr.find_all('td')[1].text.strip()
            stock[key] = value
    return stock


def get_stock_history(dom):
    soup = BeautifulSoup(dom, 'html5lib')
    table = soup.find('table', 'historical_price')
    header_row = table.find('tr', 'bb')
    headers = [s for s in header_row.stripped_strings]
    print(headers)
    for th in table.find_all('tr')[1:]:  # 第一列是標題, 故略過
        print([s for s in th.stripped_strings])


if __name__ == '__main__':
    page = get_web_page(G_FINANCE_URL, 'TPE:2330')
    if page:
        stock = get_stock_info(page)
        for k, v in stock.items():
            print(k, v)

    # 取得個股歷史股價資料
    #page = get_web_page(G_FINANCE_HIS_URL, 'TPE:2330')
    #if page:
    #    get_stock_history(page)
