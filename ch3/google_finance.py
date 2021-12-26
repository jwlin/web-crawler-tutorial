import requests
from bs4 import BeautifulSoup


# 網址後方加上 MARKET:STOCK_ID 即為個股資訊. e.g, TPE:2330
G_FINANCE_URL = "https://www.google.com/search?q="
G_FINANCE_HIS_URL = 'https://finance.google.com/finance/historical?q='


def get_web_page(url, stock_id):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'}
    resp = requests.get(url + stock_id, headers=headers)
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_stock_info(dom):
    soup = BeautifulSoup(dom, 'html5lib')
    stock = dict()
    
    # 取出公司名及即時股價資訊
    stock['name'] = soup.find("span", {"data-attrid": "Company Name"}).text
    price_spans = soup.find("div", {"data-attrid": "Price"}).find_all("span", recursive=False)
    stock['current_price'] = price_spans[0].text
    stock['current_change'] = list(price_spans[1].stripped_strings)[:2]

    # 第 4 個 g-card-section, 有左右兩個 table 分別存放股票資訊
    sections = soup.find_all('g-card-section')    
    for table in sections[3].find_all('table'):
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

    # 20180520: Google 已經移除歷史股價網頁，故程式碼無法運作
    # 取得個股歷史股價資料
    #page = get_web_page(G_FINANCE_HIS_URL, 'TPE:2330')
    #if page:
    #    get_stock_history(page)
