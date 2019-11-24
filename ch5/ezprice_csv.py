import requests
import urllib.parse
import csv
import re
from bs4 import BeautifulSoup


if __name__ == '__main__':
    query = 'ps4主機'
    q = urllib.parse.quote(query)
    # e.g. https://ezprice.com.tw/s/ps4%E4%B8%BB%E6%A9%9F/price/
    page = requests.get('https://ezprice.com.tw/s/' + q + '/price/').text
    soup = BeautifulSoup(page, 'html5lib')
    items = list()
    for div in soup.find_all('div', 'search-rst clearfix'):
        item = list()
        item.append(div.h2.a.text.strip())
        # 先取得價格字串，再移除其中的非數字部份(以空白字串取代非0-9的字元)
        price = div.find('span', 'num').text
        price = re.sub(r'[^0-9]', '', price)
        item.append(price)
        if div.find('span', 'platform-name'):
            item.append(div.find('span', 'platform-name').text.strip())
        else:
            item.append('無')
        items.append(item)
    print('共 %d 項商品' % (len(items)))
    for item in items:
        print(item)

    # 讓 Excel 開啟不會亂碼的方式
    # 1.
    # with open('ezprice.csv', 'wb') as f:
    #     f.write(b'\xEF\xBB\xBF')  # 在檔頭加上 UTF-8 編碼的 BOM
    # with open('ezprice.csv', 'a', encoding='utf-8', newline='') as f:
    #
    # 2.
    # with open('ezprice.csv', 'w', encoding='utf-8-sig', newline='') as f:

    with open('ezprice.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('品項', '價格', '商家'))
        for item in items:
            writer.writerow((column for column in item))
    '''
    print('讀取 csv 檔')
    with open('ezprice.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['品項'], row['價格'], row['商家'])
    '''
